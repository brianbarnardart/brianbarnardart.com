# Notes for AI assistants working on this repository

This is the website of Fernandina Beach artist Brian Barnard: a small Jekyll
site on GitHub Pages. The people maintaining it are often **not programmers**.
Optimize for changes they can understand, review, and undo.

## Read first

- `USER-GUIDE.md`: the caretaker's manual. If you change how a task is done,
  update the matching recipe there.
- `_layouts/README.md` and `_includes/README.md` are the authoritative docs
  for templates and includes. **If you edit a layout or include, update its
  README in the same change.** Each file's header comment says so too.
- `SEO-STRATEGY.md`: search plan, and why things are the way they are.

## Hard rules (CI enforces some of these)

- Every indexable `.md` with a `layout` needs `description` and `image` front
  matter, or the deploy fails. Drafts use `noindex: true` + `sitemap: false`
  (or `published: false` to skip building entirely).
- Internal links and image paths on sitemap pages must exist. Paths are
  case-sensitive.
- Use **LF line endings only** (`.gitattributes` enforces this on commit).
- Keep images under ~1 MB (target < 500 KB, ~2000 px long edge). Never commit
  raw camera originals: git history keeps them forever.
- **No invasive tracking**: no Google Analytics, ad pixels, or cookie-based
  analytics. GoatCounter is deliberate. See `privacy.md` and `SEO-STRATEGY.md`.
- Don't hand-edit `_site/`. It's build output.

## Conventions

- Social profile URLs live in two places: `_includes/footer.html` and the
  `sameAs` list in `_includes/custom-head.html`. Keep them in sync.
- JSON-LD values go through Liquid's `jsonify` filter (not `escape`).
- The Person entity has `"@id": "https://brianbarnardart.com/#person"`, and
  other structured data (e.g. `VisualArtwork` in `_layouts/artwork.html`)
  references it.
- Print lists are `_data/*prints.yml`, rendered by `_includes/prints-grid.html`.
- External links get `target="_blank"` automatically (script in
  `_layouts/default.html`). Don't add it by hand, except in HTML injected
  after page load.
- Match the existing writing voice on content pages: warm, a little playful,
  third person about Brian, with Brian's own words in block quotes.
- The live-site checks in `.github/workflows/site-validation.yml` assert
  specific strings. If you change titles or metadata, update those
  assertions in the same change.

## Verifying changes

There may be no Ruby on the maintainer's machine. Pushing to `main` runs the
full CI (see README), and a failed build leaves the previous site live.
Don't commit or push without the maintainer's go-ahead.
