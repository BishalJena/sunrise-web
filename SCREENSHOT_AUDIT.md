# Bento Card Screenshot Audit

## Expected Layout
- **Bento layout:** ["third", "two-thirds", "half", "half", "two-thirds", "third", "full"]
- **Shots per size:** third=1, half=1, two-thirds=2, full=3
- **Expected files per app:**
  - hero.png (1)
  - card-1.png (1 - third)
  - card-2-1.png, card-2-2.png (2 - two-thirds)
  - card-3.png (1 - half)
  - card-4.png (1 - half)
  - card-5-1.png, card-5-2.png (2 - two-thirds)
  - card-6.png (1 - third)
  - card-7-1.png, card-7-2.png, card-7-3.png (3 - full)

## Current State by App

### ✅ bersih
- **Status:** All screenshots present (12/12)
- **Dimensions:** 680x1474 (ratio: 0.4611 ≈ 9:19.5)
- **Sizes:** 464KB to 1.3MB
- **Issues:** Many files exceed 300KB target, need compression

### ✅ hush
- **Status:** All screenshots present (12/12)
- **Dimensions:** 684x1484 (ratio: 0.4609 ≈ 9:19.5)
- **Sizes:** 40KB to 104KB
- **Issues:** Good file sizes, all under 300KB ✓

### ✅ kesha
- **Status:** All screenshots present (12/12)
- **Dimensions:** 708x1536 (ratio: 0.4609 ≈ 9:19.5)
- **Sizes:** 232KB to 476KB
- **Issues:** Some files exceed 300KB target (card-2-2, card-4, card-5-2, card-6, card-7-1, card-7-3)

### ✅ listo
- **Status:** All screenshots present (12/12)
- **Dimensions:** 684x1484 (ratio: 0.4609 ≈ 9:19.5)
- **Sizes:** 68KB to 172KB
- **Issues:** All under 300KB ✓

### ✅ tldr-news
- **Status:** All screenshots present (12/12)
- **Dimensions:** 684x1482 (ratio: 0.4615 ≈ 9:19.5)
- **Sizes:** 88KB to 472KB
- **Issues:** Several files exceed 300KB (card-1, card-2-1, card-2-2, card-3, card-4, card-5-2, card-7-1, card-7-2, hero)

### ❌ lotus-g-1
- **Status:** NO SCREENSHOTS (0/12) - all showing placeholders
- **Issues:** Entire directory missing

### ❌ lotus-e-2
- **Status:** NO SCREENSHOTS (0/12) - all showing placeholders
- **Issues:** Entire directory missing

## CSS Issues to Fix

### Current problems:
1. `.shot > img` needs proper `object-fit: cover` with `object-position: top center`
2. `.mini-phone .shot` needs proper aspect ratio maintenance
3. Screenshots may stretch or overflow cards at different breakpoints
4. Need to ensure proper alignment at desktop (~1000px), tablet (~768px), and mobile (~390px)

### Affected CSS classes:
- `.shot` (lines 1560-1571)
- `.shot > img` (line 1572)
- `.mini-phone` (lines 1590-1599)
- `.mini-phone .shot` (line 1600)
- `.card-media.peek` (lines 1609-1615)
- `.phone-screen.has-shot` (lines 1585-1587)

## Actions Required

1. ✅ Create screenshot directories for lotus-g-1 and lotus-e-2
2. ✅ Fix CSS for proper screenshot display
3. ✅ Optimize oversized images (compress to <300KB where possible)
4. ✅ Rebuild sites and verify no placeholders remain
5. ✅ Test at multiple viewport sizes
6. ✅ Create before/after screenshots
7. ✅ Submit PR with detailed description
