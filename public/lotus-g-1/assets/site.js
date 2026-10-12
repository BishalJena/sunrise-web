// Lotus waitlist sites — small progressive enhancements.
// Generated into each app folder by tools/site-builder/build.py.
// Every page works without this file; forms fall back to plain POSTs.
(function () {
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Deterministic pseudo-random so generated grids look the same on every load.
  function rng(seed) {
    let s = seed >>> 0;
    return function () {
      s = (s * 1664525 + 1013904223) >>> 0;
      return s / 4294967296;
    };
  }

  document.querySelectorAll(".grid[data-cells]").forEach(function (grid, idx) {
    const cells = parseInt(grid.dataset.cells, 10);
    const density = parseFloat(grid.dataset.density || "0.65");
    const rand = rng((parseInt(grid.dataset.seed, 10) || idx + 1) * 9973);
    const frag = document.createDocumentFragment();
    for (let i = 0; i < cells; i++) {
      const cell = document.createElement("i");
      const bias = density + (i / cells) * 0.25;
      if (rand() < bias) cell.style.setProperty("--a", Math.round(45 + rand() * 55) + "%");
      frag.appendChild(cell);
    }
    grid.appendChild(frag);
  });

  // Nav: spread out at the top of the page, a floating pill once you scroll.
  const root = document.documentElement;
  let popTimer;
  function updateNav() {
    const atTop = window.scrollY < 8;
    if (atTop === root.classList.contains("nav-top")) return;
    root.classList.toggle("nav-top", atTop);
    // Pop the capsule as it forms.
    root.classList.remove("nav-pop");
    if (!atTop && !reduceMotion) {
      void root.offsetWidth; // restart the animation
      root.classList.add("nav-pop");
      clearTimeout(popTimer);
      popTimer = setTimeout(function () { root.classList.remove("nav-pop"); }, 700);
    }
  }
  updateNav();
  window.addEventListener("scroll", updateNav, { passive: true });

  // ---------- Waitlist ----------
  // Forms post to api/join in their own folder, handled by functions/[app]/api/join.js (Pages Function).

  let toastHost;
  let toastTimer;

  function ensureToastHost() {
    if (toastHost) return toastHost;
    toastHost = document.createElement("div");
    toastHost.className = "toast-host";
    toastHost.setAttribute("role", "status");
    toastHost.setAttribute("aria-live", "polite");
    document.body.appendChild(toastHost);
    return toastHost;
  }

  function showToast(kind, text) {
    const host = ensureToastHost();
    const icon = kind === "ok" ? "check_circle" : kind === "err" ? "error" : "";
    const toast = document.createElement("div");
    toast.className = "toast toast-" + kind + (reduceMotion ? " toast-no-motion" : "");
    toast.innerHTML =
      (icon ? '<span class="icon" aria-hidden="true">' + icon + "</span>" : "") +
      "<span class=\"toast-text\"></span>";
    toast.querySelector(".toast-text").textContent = text;
    host.replaceChildren(toast);
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () {
      toast.classList.add("toast-out");
      setTimeout(function () {
        if (toast.parentElement) toast.remove();
      }, reduceMotion ? 0 : 280);
    }, 4000);
  }

  document.querySelectorAll("form[data-waitlist]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const data = new FormData(form);
      const email = String(data.get("email") || "").trim();
      if (!email || !form.checkValidity()) {
        showToast("err", "Please enter a valid email address.");
        return;
      }
      if (data.get("company")) return; // honeypot filled: quietly ignore bots
      const button = form.querySelector("button");
      button.disabled = true;
      fetch(form.getAttribute("action"), {
        method: "POST",
        headers: { "Content-Type": "application/json", "Accept": "application/json" },
        body: JSON.stringify({
          email: email,
          source: form.dataset.source || "site",
          page: location.href, // carries any utm_* tags
          referrer: document.referrer,
        }),
      })
        .then(function (res) {
          return res.json().catch(function () { return {}; }).then(function (body) {
            if (!res.ok) throw new Error(body.error || "Something went wrong. Please try again.");
            return body;
          });
        })
        .then(function (body) {
          showToast("ok", body.already
            ? "You're already on the list. We'll be in touch."
            : "You're on the list! We'll email you when it's ready.");
          form.reset();
        })
        .catch(function (err) {
          showToast("err", err.message || "Something went wrong. Please try again.");
        })
        .finally(function () { button.disabled = false; });
    });
  });

  // Returning from a no-JS form post (?joined=1).
  if (/[?&]joined=1/.test(location.search)) {
    document.querySelectorAll("form[data-waitlist]").forEach(function (form) {
      showToast("ok", "You're on the list! We'll email you when it's ready.");
    });
  }

  // ---------- Contact form → mail app ----------
  document.querySelectorAll("form[data-form=contact]").forEach(function (form) {
    if (form.getAttribute("action") !== "#") return;
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const data = new FormData(form);
      const subject = encodeURIComponent((data.get("topic") || "Hello") + " — " + form.dataset.appName);
      const body = encodeURIComponent((data.get("message") || "") + "\n\n— " + (data.get("name") || "") + " <" + (data.get("email") || "") + ">");
      window.location.href = "mailto:" + form.dataset.mailto + "?subject=" + subject + "&body=" + body;
      const ok = form.parentElement.querySelector(".success");
      if (ok) ok.classList.add("show");
    });
  });

  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
