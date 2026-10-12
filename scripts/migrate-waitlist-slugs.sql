-- Run after renaming public site folders (lotus-* → kesha, hush, listo, bersih, tldr-news).
-- Remote D1 (waitlist-db):
--   npx wrangler d1 execute waitlist-db --remote --file=scripts/migrate-waitlist-slugs.sql

UPDATE apps SET slug = 'kesha' WHERE slug = 'lotus-c-1';
UPDATE apps SET slug = 'hush' WHERE slug = 'lotus-f-1';
UPDATE apps SET slug = 'listo' WHERE slug = 'lotus-f-2';
UPDATE apps SET slug = 'bersih' WHERE slug = 'lotus-e-1';
UPDATE apps SET slug = 'tldr-news' WHERE slug = 'lotus-e-3';
