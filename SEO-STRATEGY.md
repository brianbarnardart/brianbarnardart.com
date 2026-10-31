# SEO strategy for brianbarnardart.com

One hard rule:

> **No invasive tracking.** SEO improvements come from content quality,
> technical correctness, crawlability, and clear conversion paths, not
> from behavioral surveillance.

---

## 1. Goals

1. **Be the answer for "Brian Barnard" / "Brian Barnard art"**, at minimum
   whenever the search has Fernandina Beach / Amelia Island / Jacksonville
   context (location, or words like "artist", "painter", "mural").
2. **Convert visitors** into print requests (`/prints/`) and contacts (`/contact/`).
3. **Build long-tail visibility** through real pages about paintings,
   venues, bands, and stories.

### The "which Brian Barnard?" problem

Other people share the name. Search engines decide which one you mean by
**entity signals**: consistent facts (name + place + occupation) repeated
across this site, social profiles, business listings, and especially
*other* websites that link here. No single tag decides it. Each consistent
mention adds a little.

**Status (Oct 2026):** Google ranks the site #1 for both names, even
logged-out over VPN. Bing is slower. That's typical: Bing has fewer signals
about a 2026 domain, relies more on literal on-page wording, and gives
weight to Microsoft-owned LinkedIn for person names.

---

## 2. What's in place

### Technical

| Item | Where |
|---|---|
| `sitemap.xml` (auto-generated; drafts excluded via `sitemap: false`) | `jekyll-sitemap` |
| `robots.txt` allowing all, pointing at sitemap | `robots.txt` |
| Canonical URLs, meta description, Open Graph / Twitter cards | `jekyll-seo-tag` from front matter |
| `<title>`: home = `Brian Barnard Art \| Fernandina Beach Artist & Live Painter`; inner = `Page \| Brian Barnard Art` | `_includes/head.html`, `tagline` in `_config.yml` |
| `noindex` robots meta for drafts | `noindex: true` front matter |
| HTTPS, `www` → apex and `http` → `https` 301 redirects | GitHub Pages |
| **IndexNow** ping to Bing etc. after every successful deploy | `site-validation.yml`, key file in repo root |

### Structured data (JSON-LD)

- **Person** on every page (`_includes/custom-head.html`) with
  `"@id": "https://brianbarnardart.com/#person"`: name, image, job title,
  Fernandina Beach address and home location, FSU alumni, `knowsAbout`,
  and `sameAs` → Facebook, Instagram, YouTube.
- **VisualArtwork** on each painting page (`_layouts/artwork.html`): title,
  image, medium, size, year, and `creator` → the Person `@id` above. This
  ties painting images to the artist in image search.
- **WebSite** (emitted automatically by `jekyll-seo-tag`).

Validate with the [Schema Markup Validator](https://validator.schema.org/)
or Google's [Rich Results Test](https://search.google.com/test/rich-results).

### Content signals

- Painting image alt text reads "*Title*, acrylic on canvas by Brian Barnard".
- Home page copy names Brian, Fernandina, The Green Turtle, The Inkwell, and
  Tigre Island Room in natural sentences.
- Venue pages give real addresses and phone numbers.

### CI guardrails

- Deploy is blocked if an indexable page lacks `description`/`image`, or if
  an internal link is broken.
- Post-deploy check confirms live robots, sitemap, titles, canonicals, meta,
  Person structured data, and noindex on drafts.
- Images over 1 MB produce a warning (page speed is a ranking factor, and
  most visitors are on phones).

---

## 3. Action list

Ordered roughly by impact for the effort. Items marked 🔑 need account access
and can't be done in this repository.

### Off-site: the biggest levers for "which Brian Barnard"

- [ ] 🔑 **Bing Webmaster Tools**: verify the site (easiest: "Import from
      Google Search Console"), submit `https://brianbarnardart.com/sitemap.xml`,
      and check the IndexNow page shows submissions arriving.
- [ ] 🔑 **Google Search Console**: confirm verified; sitemap submitted.
- [ ] 🔑 **Google Business Profile**: create as a *service-area* business
      (no public street address needed), category "Artist", area Fernandina
      Beach / Amelia Island, website link. This is the main local signal.
- [ ] 🔑 **Bing Places**: import from the Google Business Profile.
- [ ] 🔑 **Recover LinkedIn** and put `https://brianbarnardart.com` and
      "Artist, Fernandina Beach" on it. Bing leans heavily on LinkedIn for
      person-name searches. Then add the URL to `sameAs` and the footer.
- [ ] 🔑 **Social bios link back.** Facebook, Instagram, and YouTube "About"
      sections should all link to `https://brianbarnardart.com` and say
      "Fernandina Beach". Two-way links confirm the `sameAs` claims.
- [ ] **Ask for links from local sites.** These count far more than anything
      on-site:
  - The Inkwell, Tigre Island Room, and Green Turtle websites/pages (an
    "artist" mention linking here)
  - Fernandina Observer (the right-whale story) and any future press: ask
    that articles link the site
  - Amelia Island tourism / event listings, Shrimp Festival vendor or artist
    pages, local arts organizations
  - Bands Brian paints with: a link from their sites or posts

### On-site

- [ ] **Give the home page a visible `<h1>`.** The page currently has no
      heading text (the signature logo is an image, now with an
      `aria-label`). Something like "Brian Barnard: Fernandina Beach artist
      and live painter" as the first line. Bing weighs `<h1>` text heavily.
- [ ] **Make `/events/` concrete.** A recurring schedule in plain text
      ("Fridays and Saturdays at The Green Turtle, 14 S 3rd St"; "Tuesday
      sketch class at The Inkwell") is useful to visitors and to local search.
      Optional later: `Event` structured data for dated events.
- [ ] **Fill in or unpublish placeholder drafts.** Several `noindex` pages
      (`_bands/*`, `_charities/*`, `_events/*`, two `_interests/*`) are
      publicly reachable with template text ("Add your notes about…") and
      missing images. Search engines won't rank them, but people can find
      them. Switch to `published: false` until they're written (and update
      the `/bands/1blackfrend/` assertion in `site-validation.yml`).
- [ ] **Decide about `/works/waterfront-jamboree/`.** It's in the sitemap but
      nothing links to it (archived), and it has one sentence of text.
      Either expand it or mark it `noindex`/`sitemap: false`.
- [ ] **Resize large images** (see USER-GUIDE §7). The CI warning lists them.
- [ ] Add more painting pages with real stories. Every `_works/` page is a
      new chance to rank for the painting's name and subject.

### Explicitly out of scope

- Cross-site behavioral tracking, ad pixels, surveillance analytics
- Keyword stuffing, doorway pages, buying links
- Hiding text from visitors to show search engines

---

## 4. Checklist for any new public page

- [ ] Front matter has `layout`, `title`, `description` (1–2 natural
      sentences), `image`
- [ ] Content answers a real visitor question. No placeholder text.
- [ ] Links to related pages on the site (venues, paintings, prints)
- [ ] Images resized (< ~500 KB), with descriptive filenames and alt text
- [ ] If not ready: `noindex: true` + `sitemap: false`, or `published: false`

---

## 5. Measuring (privacy-respecting)

- **GoatCounter**: page views, referrers (look for venue/news sites
  sending visitors), 404 events (`404: /path`) to find broken inbound links.
- **Search Console / Bing Webmaster Tools**: which searches show the site,
  click-through, indexing errors. These are aggregate data from the
  search engines, with no scripts on the site.
