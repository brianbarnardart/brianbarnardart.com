# SEO strategy for brianbarnardart.com

This document describes the search strategy for this site, with one hard rule:

> **No invasive tracking.**
>
> SEO improvements should come from content quality, technical correctness,
> crawlability, and clear conversion paths -- not behavioral surveillance.

---

## 1) Strategy in one page

### Primary goal

Rank strongly for:

- **Brian Barnard**
- **Brian Barnard Art**
- local intent terms around Fernandina Beach live painting / murals

### Secondary goal

Convert visitors into actions:

- print requests (`/prints/`)
- contact requests (`/contact/`)

### Tertiary goal

Create a durable content base (venues, bands, stories, influences) that builds
long-tail search visibility over time.

---

## 2) What comes from default Jekyll + plugins vs custom work

### Default / plugin-provided

- `jekyll-seo-tag` provides canonical/meta/OG scaffolding from front matter.
- `jekyll-sitemap` generates `sitemap.xml`.
- `jekyll-feed` generates a feed.

### Site customizations

- Custom title pattern in head:
  - Home: `Brian Barnard Art`
  - Inner pages: `<Page Title> | Brian Barnard Art`
- Site-wide Person JSON-LD in `_includes/custom-head.html`
- `robots.txt` with explicit sitemap pointer
- Front-matter controls for non-index content:
  - `noindex: true`
  - `sitemap: false`
- Print conversion pathway:
  - `/prints/` page + site CTA ribbon + contact-based ordering

---

## 3) Current technical SEO posture

### Crawlability and discovery

- `robots.txt` exists and allows crawl.
- `robots.txt` points to `https://brianbarnardart.com/sitemap.xml`.
- `sitemap.xml` is generated automatically on deploy.

### Metadata quality

- Indexable pages are expected to have:
  - `description`
  - `image`
- Social previews use `og:image` from front matter (`jekyll-seo-tag` behavior).

### Entity clarity

- Person structured data identifies Brian Barnard and social profiles.
- Brand is reinforced in page titles across indexable pages.

### Index hygiene

- Utility/draft/speculative pages can be excluded with:
  - `noindex: true`
  - `sitemap: false`
- `404.md` is intentionally excluded.

---

## 4) CI/CD guardrails

Two workflows protect SEO:

1. **Build/deploy workflow** (`.github/workflows/jekyll-gh-pages.yml`)
   - Enforces required SEO front matter on indexable markdown pages
   - Builds and deploys only if checks pass

2. **Live validation workflow** (`.github/workflows/site-validation.yml`)
   - Runs after deploy with retry/backoff
   - Confirms live `robots.txt`, `sitemap.xml`, key metadata, and noindex/sitemap exclusions

This prevents silent regressions.

---

## 5) Content model rules (important)

### Publish-ready pages (indexable)

Use when the page is complete enough to rank:

- clear narrative content
- real links/media
- strong front matter (`title`, `description`, `image`, permalink as needed)

### Draft/speculative pages

Use for placeholders or outlines still under development:

```yaml
noindex: true
sitemap: false
```

Move to indexable only when the content is genuinely useful.

---

## 6) Non-tracking SEO growth plan

### Phase A -- technical baseline (done)

- sitemap + robots + canonical/title consistency
- structured data
- front-matter coverage
- CI guardrails

### Phase B -- conversion-ready content (in progress)

- Keep `/prints/` clear and personal
- Keep pricing/availability flow explicit through contact form
- Maintain current offerings in `_data/prints.yml`

### Phase C -- authority expansion (next)

- Build real pages for:
  - local venues
  - bands Brian paints with
  - "life and times" stories
- Prioritize depth over volume; avoid thin pages

---

## 7) Editorial checklist for any new indexable page

Before publishing, confirm:

- [ ] Front matter has `layout`, `title`, `description`, `image`
- [ ] Content answers a real visitor question
- [ ] Internal links connect to related pages
- [ ] Outbound links are credible and relevant
- [ ] Page is not speculative placeholder text
- [ ] If draft: set `noindex: true` and `sitemap: false`

---

## 8) Bing/Google operational checklist (manual)

These do **not** require adding tracking scripts:

- Verify site in Bing Webmaster Tools and Google Search Console
- Submit sitemap URL
- Use URL inspection/submission for key pages after major updates
- Monitor indexing and crawl errors

---

## 9) Future conversion enhancement notes

- "Held-in-hand print photos" are a good trust signal for `/prints/`:
  - communicates authenticity ("this comes from Brian directly")
  - supports the non-store, personal-order model
  - can improve click-through and conversion confidence

---

## 10) Boundaries

Out of scope unless strategy changes:

- cross-site behavioral tracking
- ad-tech pixels
- surveillance-heavy analytics

Privacy-respecting measurement and strong content architecture are the default.
