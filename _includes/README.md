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
| `header.html` | `header.html` | SVG signature logo (with `aria-label`); nav built from `nav:` front matter |
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
(`Page Title | Brian Barnard Art` for inner pages; `Brian Barnard Art | <tagline>`
on the home page, where `tagline` comes from `_config.yml`). Also pulls in SEO
meta, the main stylesheet, the RSS feed link, and `custom-head.html`. If a page sets `noindex: true` in front matter, this include
adds `<meta name="robots" content="noindex, nofollow">`.

### `header.html`

The site header. Renders the SVG signature as the home link (the SVG has no
text, so the link carries an `aria-label` naming Brian for screen readers and
crawlers), then builds the navigation bar from any page that has a `nav:`
number in its front matter, sorted ascending by that number.

### `footer.html`

The site footer. Social icon links (YouTube, Instagram, Facebook) and
a copyright line with the current year. Icons are pulled from `icons/`.

(At time of writing, LinkedIn is pending an account recovery.)

### `custom-head.html`

Favicon and web manifest `<link>` tags, plus `Person` JSON-LD structured data,
injected by `head.html`. Kept separate so head-level metadata can be updated
without touching the full `<head>`.

The Person block has `"@id": "<site.url>/#person"`, so other structured data
can refer to the same entity (the `VisualArtwork` block in `artwork.html`
does). Values are emitted with `jsonify`, not `escape`, because HTML entities
like `&#39;` are not decoded inside JSON. The `sameAs` list must match the
social links in `footer.html`.

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
| `error_message` | no | Message shown on failure (default: `Something went wrong! 😕`) |

#### Double-checking form submissions with GoatCounter

The contact form now integrates with [GoatCounter](https://www.goatcounter.com/) analytics to double-check submissions and help diagnose delivery issues. Three custom events are sent to GoatCounter:

- **form-submit**: Fired when the user clicks submit, before contacting FormSpark.
- **form-success**: Fired if FormSpark responds with success.
- **form-failure**: Fired if FormSpark responds with an error.

Each event includes the email address entered (or 'no email' if blank) in the event title, so you can cross-reference submissions and follow up if needed. This allows you to:

- See the total number of submit attempts.
- Compare successes and failures to the total.
- Identify and contact users whose messages may not have gone through.

All GoatCounter events use unique paths (e.g. `/contact#form-submit`, `/contact#form-success`, `/contact#form-failure`) and the email in the title for easy filtering and review.

While this does mean GoatCounter gets a copy of the email address, it's not clear GoatCounter is any less trustworthy than FormSpark (or the email providers carrying the messages, or the browser itself)...so the added robustness outweighs any privacy concerns.

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

### `prints-grid.html`

Grid of print offerings, used by `prints.md` and each `prints/*.md` category
page. Each entry in the list follows the shape documented in `USER-GUIDE.md`
("Add a print"): `title`, `image`, optional `thumb`, `url`, `alt`, `notes`,
plus optional `buy_url` and `price`, which add a **Buy Print (price)** button
linking to a hosted checkout (e.g. a Stripe Payment Link). Without `thumb`, the
grid uses the automatic `-thumb.jpg` copy (see `thumb-url.html`) and falls back
to the full image if that copy is missing.

| Parameter | Required | Description |
|---|---|---|
| `items` | yes | The list to render, e.g. `site.data.prints` |
| `empty_message` | no | Text shown when the list is empty |

### `thumb-url.html`

Prints the address of the small copy of a picture: `/assets/x/foo.png` becomes
`/assets/x/foo-thumb.jpg`. The copies are made during deployment by
`scripts/make-thumbnails.py` (called from `.github/workflows/jekyll-gh-pages.yml`),
so they don't exist when running `jekyll serve` locally. Callers add an
`onerror` fallback to the full image. Used by `gallery.md` and `prints-grid.html`.
Full `https://` addresses are returned unchanged.

| Parameter | Required | Description |
|---|---|---|
| `image` | yes | Path or URL of the full-size picture |

Use it with `capture`:
`{% raw %}{% capture _thumb %}{% include thumb-url.html image=artwork.image %}{% endcapture %}{% endraw %}`

### `prints-ribbon.html`

The fixed **Get Prints** call-to-action ribbon plus its show/hide script.
Included by both `default.html` and `404.html`. Hidden on `/prints/` and
`/gallery/`.

Link target, in priority order:

1. `prints_url:` in the page's front matter
2. `/prints/` if the page is itself under `/prints/`
3. `/prints/<last URL segment>/` if such a page exists (e.g.
   `/interests/the-big-lebowski/` → `/prints/the-big-lebowski/`)
4. `/prints/`

Visibility: slides in after a delay, stays visible for the rest of the
browsing session (`sessionStorage` key `printsRibbonSeenThisSession`), and is
hidden for one hour after a click (`localStorage` key
`printsRibbonDismissUntil`). `privacy.md` shows and resets that timer, so
keep the key names in sync.

### `shorts-grid.html`

YouTube Shorts grid. Reads video ids and titles from `_data/shorts.yml` and
renders them as embedded iframes with a link to the channel. No parameters —
just drop `{% include shorts-grid.html %}` where you want the grid to appear.

### `icons/`

SVG icon files: `youtube.svg`, `instagram.svg`, `facebook.svg`, `linkedin.svg`.
Used by `footer.html`. Include inline with `{% include icons/youtube.svg %}`.
