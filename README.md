# brianbarnardart.com source

This is the Jekyll repository for Fernandina Beach artist Brian Barnard.

All Artwork and English Text is Copyright by Brian Barnard, All Rights Reserved.

Website source code (things like CSS, HTML, JavaScript) is governed by
[Creative Commons CC-0](https://creativecommons.org/) license--which means if
you find a useful trick here and want to put that on your own site, feel free
to do so!  (Creative Commons is a great resource for artists who have work they
want to share, so check that out if you have not heard of it before!)

---

## How this site works

This site is hosted on **[GitHub Pages](https://pages.github.com/)** using a
**GitHub Actions** workflow. Every time a change is pushed to the `main` branch,
the workflow installs dependencies, runs **Jekyll**, and publishes the result at
`https://brianbarnardart.com`.

---

## Jekyll

[Jekyll](https://jekyllrb.com/) is a **static site generator**: it reads a
folder of plain text files (Markdown, HTML, CSS, YAML) and produces a finished
website. There is no database and no server-side code to maintain.

### How a page gets to the browser

1. You write content in a `.md` file (Markdown).
2. Jekyll wraps it in the layout named in that file's front matter (`layout: page`).
3. The layout lives in `_layouts/` — either a file you create there or one
   inherited from the theme.
4. Jekyll writes the finished HTML to `_site/` (never commit that folder;
   GitHub Pages rebuilds it automatically).

### Key files and folders

| Path | Purpose |
|---|---|
| `Gemfile` | Ruby gem versions — Jekyll, minima, plugins |
| `_config.yml` | Site-wide settings (title, URL, theme, etc.) |
| `_data/*.yml` | Structured data files (e.g. the Shorts video list) |
| `_includes/*.html` | Reusable HTML fragments, inserted with `{% include name.html %}` |
| `_layouts/*.html` | Page templates. Markdown files pick one with `layout: X` in front matter |
| `assets/main.scss` | Custom CSS/SCSS that extends the theme |
| `index.md` | The home page |
| `contact.md` | The `/contact/` page |
| `CNAME` | Tells GitHub Pages to serve this repo at `brianbarnardart.com` |

### Useful references

- [Jekyll documentation](https://jekyllrb.com/docs/)
- [Jekyll front matter](https://jekyllrb.com/docs/front-matter/) — the `---` block at the top of every page
- [Jekyll includes](https://jekyllrb.com/docs/includes/)
- [Jekyll data files](https://jekyllrb.com/docs/datafiles/)
- [GitHub Pages documentation](https://docs.github.com/en/pages)

---

## The Minima theme

Minima is Jekyll's default bundled theme: a clean, minimal design with a
header navigation bar, a main content area, and a footer.

### Theme overrides

Jekyll always prefers files in the project folder over the theme's copies,
which lets you customise individual pieces without forking the entire theme:

| This project's file | Replaces theme file | Why |
|---|---|---|
| `_includes/head.html` | Minima's `head.html` | Custom title format, favicon, web manifest |
| `_includes/footer.html` | Minima's `footer.html` | Custom social links layout and copyright |

- [Minima source](https://github.com/jekyll/minima)
- [Minima README](https://github.com/jekyll/minima/blob/master/README.md)

---

## Writing content: Kramdown Markdown

Pages are written in **Markdown**, specifically the
[Kramdown](https://kramdown.gettalong.org/quickref.html) flavour that Jekyll
uses by default. Markdown is plain text with simple symbols that become
formatted HTML.

### Headings

```markdown
# Heading 1  — big title
## Heading 2 — section
### Heading 3 — sub-section
```

### Emphasis

```markdown
*italic* or _italic_
**bold** or __bold__
~~strikethrough~~
```

### Links

```markdown
[link text](https://example.com)               — external link
[Contact me](/contact/)                         — internal link
```

### Images

```markdown
![Description of image](/assets/images/my-photo.jpg)
```

Images should be placed in `assets/images/` and committed to the repository.

### Lists

```markdown
- unordered item
- another item

1. First ordered item
2. Second item
```

### Horizontal rule

```markdown
---
```

### Blockquote

```markdown
> This text appears indented as a quote.
```

### Code (inline and block)

````markdown
Use `backticks` for inline code.

```
A fenced block for
multiple lines of code.
```
````

### Front matter

Every `.md` page starts with a **front matter** block between `---` lines.
This is YAML, not Markdown, and it tells Jekyll how to build the page:

```yaml
---
layout: page
title: My Page Title
permalink: /my-page/
---
```

- `layout` — which template to wrap the content in (almost always `page`)
- `title` — the page title, shown as a heading and in the browser tab
- `permalink` — the URL path; if omitted, Jekyll derives it from the filename

Anything below the closing `---` is the page content, written in Markdown.

### Liquid templating

Jekyll passes Markdown files through a templating language called
**[Liquid](https://shopify.github.io/liquid/)** before converting to HTML.
This is how `{% include shorts-grid.html %}` works, and how `_data/shorts.yml`
gets looped over. Most content authors won't need to write Liquid, but
recognising `{{ }}` (output) and `{% %}` (logic) tags explains what those
lines in the files mean.

---

## Images Shown By Chat Apps and iMessage

`jekyll-seo-tag` reads `image:` from front matter and outputs it as `og:image`.
Chat apps and iMessage use that to pull the preview thumbnail.

---

## Adding a new page

1. Create a new `.md` file in the project root, e.g. `gallery.md`.
2. Give it front matter:
   ```yaml
   ---
   layout: page
   title: Gallery
   permalink: /gallery/
   ---
   ```
3. Write content below the `---`.
4. Commit and push. The page appears at `https://brianbarnardart.com/gallery/`
   and Minima automatically adds it to the navigation bar.

## Adding a new Short

1. Open `_data/shorts.yml`.
2. Copy a YouTube Shorts URL, e.g. `https://www.youtube.com/shorts/AbCdEf12345`.
3. Add an entry:
   ```yaml
   - id: AbCdEf12345
     title: A description of the video
   ```
4. Commit and push. The video appears on the home page automatically.
