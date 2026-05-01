# _layouts

Page templates for Jekyll. Every `.md` file picks a layout with `layout: name`
in its front matter.

> **For AI assistants and human editors:** if you modify a file in this
> directory, please update this README to match — it is the authoritative
> user guide for these files.

---

## Layout hierarchy

```
default.html          ← base shell: <html>, <head>, <header>, <footer>, lightbox, external-link script
├── home.html         ← home page: wraps content in <article>; hides the back-to-home footer link
├── article.html      ← collection items: prev/next nav + article header + body
├── artwork.html      ← _works/: hero image, metadata panel, inquiry form or sold note
└── 404.html          ← error page: bare shell (no site header/nav/footer), just head + content
```

Every layout except `default.html` sets `layout: default` in its own front
matter, so the chain is handled automatically — you never nest layouts manually.

---

## File reference

### `404.html`

Minimal error page shell — just `<html>`, `<head>` (via `head.html` so fonts,
favicon, and CSS still load), and a centred content card. No site header, nav,
or footer. Used only by `404.md`.

**Analytics:** Unlike the other layouts, `404.html` includes `analytics.html`
directly (in production only) rather than inheriting it from `default.html`.
However, `404.md` sets `window.goatcounter = { no_onload: true }` *before*
`count.js` loads, which suppresses GoatCounter's automatic pageview. Instead,
`404.md` fires a single custom **event** on `window.load` with:

- `path`: `404: /the/bad/path` (the pathname that was not found)
- `title`: the full URL
- `event: true` (marks it as an event, not a pageview)

This keeps 404 hits out of your regular page-traffic stats while still making
them visible in the GoatCounter events list, where broken links can be spotted
and fixed.

### `default.html`

The outermost shell rendered for every page. It:

- includes `head.html`, `header.html`, and `footer.html`
- wraps `{{ content }}` in `<main>`
- includes `lightbox.html` once (so individual layouts and pages never need to)
- runs a JavaScript snippet at `DOMContentLoaded` that automatically adds
  `target="_blank"` and `rel="noopener noreferrer"` to any link whose hostname
  differs from the site's hostname

  **Consequence:** you do not need to write `target="_blank"` yourself in
  Markdown or HTML for external links — it is handled for you.

  **Exception:** links injected into the DOM *after* `DOMContentLoaded`
  (currently only the FormSpark success/error messages in `contact-form.html`)
  are not reached by the script and must carry their own `target` and `rel`
  attributes.

### `home.html`

Used by `index.md`. Wraps page content in an `<article>` tag and hides the
back-to-home link that appears in the footer on inner pages.

### `article.html`

General-purpose layout for collection items: bands, venues, events, charities,
interests, and characters. Renders:

- Previous/next navigation arrows (skipped for the `characters` and `interests`
  collections, which are not browsed sequentially)
- An article header with `title` and optional `subtitle`
- The page body (`{{ content }}`)

### `artwork.html`

Layout for items in the `_works/` collection. Renders:

- Previous/next navigation between artworks
- A hero area: the full image (lightbox-enabled on click) beside a metadata
  panel showing `medium`, `dimensions`, `year`, and `price`
- If `price:` is set in front matter: an inquiry form via `contact-form.html`
- If `price:` is absent: a "this piece has found a home" note with a link to
  the commissions page

**Front matter fields for `_works/` items:**

| Field | Required | Description |
|---|---|---|
| `title` | yes | Artwork title |
| `image` | yes | Path to the image, e.g. `/assets/paintings/my-piece.jpg` |
| `medium` | no | E.g. `Acrylic on canvas` |
| `dimensions` | no | E.g. `'24" x 36"'` (use single quotes when the value contains `"`) |
| `year` | no | Year created |
| `price` | no | If set, the piece is for sale and an inquiry form is shown; if absent, the sold note is shown instead |
| `order` | no | Integer that controls position in the gallery grid. Lower numbers appear first. Works without `order` appear after all ordered ones, in undefined order. Duplicate values produce undefined relative ordering between those items. |
| `description` | no | Short description used for SEO (`og:description` / meta description) |
