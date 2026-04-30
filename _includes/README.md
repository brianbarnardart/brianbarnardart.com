# _includes

Reusable HTML fragments for Jekyll. Insert any of these into layouts or content
pages with:

```liquid
{% include name.html param="value" %}
```

> **For AI assistants and human editors:** if you modify a file in this
> directory, please update this README to match — it is the authoritative
> user guide for these files.

---

## Theme overrides

Jekyll resolves files in the project folder before the theme, so these three
files silently replace their Minima equivalents:

| File | Replaces Minima's… | Why |
|---|---|---|
| `head.html` | `head.html` | Custom title format, favicon, web manifest |
| `header.html` | `header.html` | SVG signature logo; nav built from `nav:` front matter |
| `footer.html` | `footer.html` | Custom social links layout and copyright |

---

## File reference

### `analytics.html`

This interoperates with GoatCounter.  If you want to not count goatcounter
from a particular browser, open the JavaScript console on brianbarnardart.com
and say: 

    localStorage.setItem('skipgc', 't')

### `head.html`

The `<head>` block for every page. Sets charset, viewport, and page title
(`Brian Barnard | Page Title` for inner pages; just the site title on the home
page). Also pulls in SEO meta, the main stylesheet, the RSS feed link, and
`custom-head.html`.

### `header.html`

The site header. Renders the SVG signature as the home link, then builds the
navigation bar from any page that has a `nav:` number in its front matter,
sorted ascending by that number.

### `footer.html`

The site footer. Social icon links (YouTube, Instagram, Facebook, LinkedIn) and
a copyright line with the current year. Icons are pulled from `icons/`.

### `custom-head.html`

Favicon and web manifest `<link>` tags, injected by `head.html`. Kept separate
so favicon assets can be updated without touching the full `<head>`.

### `contact-form.html`

Reusable contact / inquiry form backed by [FormSpark](https://formspark.io).
Handles its own submission via `fetch`, shows a success or error message, and
auto-resizes the textarea.

> **Note:** The FormSpark success message is injected via `innerHTML` *after*
> DOMContentLoaded, so the global external-link handler in `default.html` will
> not see it. Any `<a>` tags in the success message must carry their own
> `target="_blank"` and `rel="noopener noreferrer"` attributes.

| Parameter | Required | Description |
|---|---|---|
| `id` | yes | Unique HTML id for the `<form>`; avoids label collisions when the form appears more than once on a page |
| `is_inquiry` | no | Set to `true` to add a hidden `artwork` field pre-filled with `page.title` |
| `message_placeholder` | no | Placeholder text for the message textarea |
| `submit_text` | no | Button label (default: `Send`) |
| `success_message` | no | Message shown on successful send (default: `Thanks for your message! 😊`) |

### `figure.html`

Floating or full-width image with an optional caption. Clicking the image opens
a lightbox by default.

| Parameter | Required | Description |
|---|---|---|
| `image` | yes | Path to the image |
| `caption` | no | Text shown below the image (supports Markdown) |
| `side` | no | `"left"` or `"right"` to float the figure into the text column |
| `alt` | no | Alt text; falls back to caption text (stripped of HTML), then `""` |
| `maxwidth` | no | Inline CSS max-width override, e.g. `"160px"` or `"40%"` |
| `lightbox` | no | Set to `"no"` to disable the lightbox link |

### `callout.html`

Pull-quote / callout block for article pages.

| Parameter | Required | Description |
|---|---|---|
| `quote` | yes | The text to display (supports Markdown) |
| `side` | no | `"left"` or `"right"` to float into the text column; omit for a full-width centred callout |

### `lightbox.html`

Lightbox overlay and JavaScript. Included once by `default.html` — you never
need to add it manually. Activated by any `<a class="lightbox-trigger">` link,
which `figure.html` adds automatically. No parameters.

### `shorts-grid.html`

YouTube Shorts grid. Reads video ids and titles from `_data/shorts.yml` and
renders them as embedded iframes with a link to the channel. No parameters —
just drop `{% include shorts-grid.html %}` where you want the grid to appear.

### `icons/`

SVG icon files: `youtube.svg`, `instagram.svg`, `facebook.svg`, `linkedin.svg`.
Used by `footer.html`. Include inline with `{% include icons/youtube.svg %}`.
