# brianbarnardart.com source

This is the Jekyll repository for Fernandina Beach artist Brian Barnard.

All Artwork and English Text is Copyright by Brian Barnard, All Rights Reserved.

Website source code (things like CSS, HTML, JavaScript) is governed by
[Creative Commons CC-0](https://creativecommons.org/) license--which means if
you find a useful trick here and want to put that on your own site, feel free
to do so!  (Creative Commons is a great resource for artists who have work they
want to share, so check that out if you have not heard of it before!)

---

## Where to start

| You are… | Read |
|---|---|
| **Looking after this website** (updating events, adding paintings and prints, keeping accounts current) | **[USER-GUIDE.md](USER-GUIDE.md)**: plain-language caretaker's manual, no programming needed |
| Working on search visibility | [SEO-STRATEGY.md](SEO-STRATEGY.md) |
| An AI assistant (or someone directing one) | [AGENTS.md](AGENTS.md) |
| Wanting to build your own site this way | [HOWTO.md](HOWTO.md): GitHub Pages + Jekyll + custom domain, costs and risks |
| Changing templates or reusable components | [`_layouts/README.md`](_layouts/README.md), [`_includes/README.md`](_includes/README.md) |

---

## How this site works

The site is built by **[Jekyll](https://jekyllrb.com/)** (a static site
generator) with the **[Minima](https://github.com/jekyll/minima)** theme, and
hosted on **[GitHub Pages](https://pages.github.com/)**. There's no database
and no server-side code. The only external services are
[FormSpark](https://formspark.io) (form delivery) and
[GoatCounter](https://www.goatcounter.com) (cookie-free analytics).

Every push to `main` runs [`.github/workflows/jekyll-gh-pages.yml`](.github/workflows/jekyll-gh-pages.yml):

1. **SEO front-matter check** (blocking): every indexable `.md` with a
   `layout` must have `description` and `image`. Pages with `noindex: true`
   or `sitemap: false` are exempt.
2. **Oversized image warning** (non-blocking): flags images over 1 MB.
3. **Jekyll build** (`JEKYLL_ENV=production`).
4. **Internal link check** (blocking): every `href`/`src` on sitemap pages
   must resolve to a built file.
5. **External link audit** (non-blocking): warnings only, since many sites
   block CI requests.
6. **Deploy** to GitHub Pages.

A failed check means nothing is deployed, so the previous version stays live.

After a successful deploy, [`.github/workflows/site-validation.yml`](.github/workflows/site-validation.yml)
fetches the live site (with retry/backoff for propagation delay), checks
robots/sitemap/title/canonical/meta/structured data and noindex exclusions,
then submits the sitemap URLs to **IndexNow** (Bing and others). The
IndexNow key is the `<hex>.txt` file in the repo root and must match
`INDEXNOW_KEY` in that workflow.

### Key files and folders

| Path | Purpose |
|---|---|
| `_config.yml` | Site settings: `title`, `tagline` (home `<title>` suffix), `description`, collections |
| `Gemfile` | Ruby gems: Jekyll, Minima, `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed` |
| `_layouts/` | Page templates ([README](_layouts/README.md)) |
| `_includes/` | Reusable fragments and theme overrides ([README](_includes/README.md)) |
| `_data/*.yml` | Lists: `shorts.yml` (home-page videos), `prints.yml`, `lebowski_prints.yml` |
| `_works/` | One file per painting (`layout: artwork`). `_works/archive/` = has a page, but hidden from the Gallery |
| `_venues/`, `_characters/`, `_interests/`, `_events/`, `_bands/`, `_charities/` | Collections using `layout: article` (several are still drafts with `noindex`) |
| `prints/` | Print category pages, auto-listed on `/prints/` |
| `assets/main.scss` | Site CSS (extends Minima) |
| `assets/` | Images, organized by type (`paintings/`, `prints/`, `venues/`, `icons/`…) |
| `CNAME` | Custom domain for GitHub Pages |
| `robots.txt`, `site.webmanifest`, `favicon.ico` | Crawl rules, PWA manifest, icon |
| `.gitattributes` | Forces LF line endings for all text files |

### Building locally (optional)

Not needed for content edits, since GitHub builds everything. For template
work:

```sh
bundle install
bundle exec jekyll serve      # http://localhost:4000, analytics disabled
```

There's no `Gemfile.lock` committed yet, so CI resolves the newest gem
versions within the `Gemfile` constraints on each build. Committing a lock
file (generated with `bundle lock --add-platform x86_64-linux`) would pin
them.
