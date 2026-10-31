# brianbarnardart.com — Caretaker's Guide

This is the manual for whoever looks after **brianbarnardart.com**: Brian, a
family member, a friend, or someone hired to help. You don't need to be a
programmer. Everything here can be done in a web browser.

> **If you only read one section, read [Start here](#1-start-here).**
> It explains the few things that actually keep the site alive. Everything
> else is about making changes, and the site keeps running fine even if
> nobody changes anything for years.

**Contents**

1. [Start here](#1-start-here)
2. [Accounts and who holds the keys](#2-accounts-and-who-holds-the-keys)
3. [How the site works (in one picture)](#3-how-the-site-works-in-one-picture)
4. [Making a change in your browser](#4-making-a-change-in-your-browser)
5. [Undoing a mistake](#5-undoing-a-mistake)
6. [Recipes: common tasks](#6-recipes-common-tasks)
7. [Preparing images](#7-preparing-images)
8. [When the build fails (red X)](#8-when-the-build-fails-red-x)
9. [Messages from the contact and print forms](#9-messages-from-the-contact-and-print-forms)
10. [Search engines (Google and Bing)](#10-search-engines-google-and-bing)
11. [Selling prints: now and later](#11-selling-prints-now-and-later)
12. [Getting help (including from AI assistants)](#12-getting-help-including-from-ai-assistants)
13. [Reference: front matter fields](#13-reference-front-matter-fields)
14. [Reference: Markdown cheat sheet](#14-reference-markdown-cheat-sheet)

---

## 1. Start here

### The site stays up on its own

The website is a set of finished pages hosted free by GitHub. There is no
server to patch and no monthly hosting bill. If nobody touches it, it keeps
working. **Only two things can take it offline:**

| Risk | What happens | How to prevent it |
|---|---|---|
| **The domain name expires** | `brianbarnardart.com` stops working, and someone else could buy the name | Keep auto-renew ON with a valid card at the registrar (see below). **Current expiration: February 2, 2027.** |
| **Nobody can log into the GitHub account** | The site stays up, but nobody can change it | Make sure more than one trusted person has access (see [section 2](#2-accounts-and-who-holds-the-keys)) |

The **contact/print forms** are a third, smaller dependency. If the forms
service lapses, the site still works but messages stop arriving (see
[section 9](#9-messages-from-the-contact-and-print-forms)).

### You can't break the live site by editing

Every change goes through an automatic check before it's published. If the
check fails, **the previous version stays live** and nothing is lost. The
worst outcome of a bad edit is that your change doesn't appear until it's
fixed. Experiment freely.

### Once a year

- [ ] Confirm the domain auto-renew is on and the card on file hasn't expired.
- [ ] Log into GitHub, the forms service, and analytics, just to confirm the
      passwords and two-factor codes still work.
- [ ] Send a test message through the [contact form](https://brianbarnardart.com/contact/)
      and confirm it arrives.

---

## 2. Accounts and who holds the keys

Keep the logins for these in a password manager (Bitwarden, 1Password, etc.)
or written down somewhere safe. **Fill in the ✏️ blanks** and keep this list
current. A password nobody can find is as bad as a lost one.

| Service | What it controls | Details | Who has access ✏️ |
|---|---|---|---|
| **Network Solutions** (where the name was bought) | Ownership of the name `brianbarnardart.com` | Registered Feb 2026, expires **Feb 2, 2027**. Most important account. ✏️ *Brian: confirm this is still where the name is registered.* | Brian only |
| **Bluehost** (the "address book", called DNS) | Entries that point the name at GitHub | The name is set to use `ns1/ns2.bluehost.com`. You rarely need this. Don't delete the entries that point to GitHub (see `HOWTO.md`, "Connect your domain"). | Brian only |
| **GitHub**, account `brianbarnardart` | All site text, images, and design: [github.com/brianbarnardart/brianbarnardart.com](https://github.com/brianbarnardart/brianbarnardart.com) | Owned by Brian. **AE1020** can edit the site but can't change settings. Save the **two-factor recovery codes** somewhere safe. | Brian (owner), AE1020 (editing only) |
| **FormSpark** ([formspark.io](https://formspark.io)) | Delivers contact/print form messages by email | Form ID `AvqUDoWyl`. Forwards to: ✏️ ____________ | |
| **GoatCounter** ([goatcounter.com](https://www.goatcounter.com)) | Visitor counts (no cookies, no tracking) | Site code is `brianbarnardtest` (left over from setup; it works fine) | |
| **Google Search Console** / **Bing Webmaster Tools** | How the site appears in search results | See [section 10](#10-search-engines-google-and-bing) | |
| **Facebook / Instagram / YouTube** (`@brianbarnardart`) | Social profiles linked from the site footer | Linked from `_includes/footer.html` and `_includes/custom-head.html` | |
| **Sticker Mule** | T-shirt store linked from the Frog King and Green Turtle pages | | |

### Making sure the site outlives any one person

- **Give a second person full access to the GitHub project.** AE1020 can
  already edit pages. To let someone also fix settings if Brian is
  unavailable, Brian goes to **Settings → Collaborators**, finds that person
  and raises their role to **Admin**. Doing this together with Brian sitting
  at the keyboard is the point: he should know what each button does.
- **Write down the "who knows what" gap.** Right now the domain and DNS
  logins are known only to Brian. Put them in a shared password manager
  (such as Bitwarden's family or organization plan) so a trusted person can
  get in if needed.
- **Name a GitHub successor.** Logged in as `brianbarnardart`, go to the
  account **Settings → Account → Successor settings** and invite someone.
  GitHub will let that person take over the repositories if the account
  owner can no longer manage them.
- **The domain registrar is the account that matters most.** Whoever controls
  it can always point the name at a new copy of the site, even if everything
  else were lost.

---

## 3. How the site works (in one picture)

```
  You edit a text file on github.com
              │
              ▼
  GitHub runs automatic checks ──► fail? Red ✗, old site stays live, nothing lost
              │ pass
              ▼
  GitHub builds the pages and publishes them (about 2 minutes)
              │
              ▼
  A second check visits the live site to confirm it looks right,
  then tells Bing that pages changed (IndexNow)
```

- Each **page** is a plain text file ending in `.md` (Markdown).
- **Lists** (prints, YouTube shorts) live in `_data/*.yml` files, one entry per item.
- **Paintings** each have a small file in `_works/`.
- **Images** live in `assets/` (paintings in `assets/paintings/`, print photos
  in `assets/prints/`, and so on).
- The free tool that assembles it all is called **Jekyll**. You never need
  to run it. GitHub does it for you.

A picture version of this is in [START-HERE.md](START-HERE.md) and
[docs/site-overview.svg](docs/site-overview.svg).

**Where things are:**

| To change… | Edit this file |
|---|---|
| Home page text | `index.md` |
| Events page | `events.md` |
| FAQ | `faq.md` |
| Contact page | `contact.md` |
| Prints page text | `prints.md` |
| List of prints | `_data/prints.yml` (Lebowski prints: `_data/lebowski_prints.yml`) |
| YouTube shorts on the home page | `_data/shorts.yml` |
| A painting's page | `_works/<painting-name>.md` |
| A venue page | `_venues/<venue-name>.md` |
| Frog King page | `_characters/frog-king.md` |
| Footer social links | `_includes/footer.html` |
| Browser-tab title wording, site description | `_config.yml` (`title`, `tagline`, `description`) |
| Privacy page | `privacy.md` |

---

## 4. Making a change in your browser

### Editing a file

1. Sign in at [github.com](https://github.com) and open
   [the repository](https://github.com/brianbarnardart/brianbarnardart.com).
2. Click into the file (for example `events.md`).
3. Click the **pencil icon** ✏️ (top right of the file).
4. Make your edit. Use the **Preview** tab to see the formatting.
5. Click **Commit changes…**, write a short note like "Add December events",
   leave **Commit directly to the main branch** selected, and confirm.
6. Wait about 2 minutes, then reload [brianbarnardart.com](https://brianbarnardart.com).
   If you don't see the change, press `Ctrl+F5` (Windows) or `Cmd+Shift+R` (Mac).

### Uploading images

1. Open the folder (for example `assets/paintings/`).
2. **Add file → Upload files**, then drag the image in and commit.
3. **Shrink the image first.** See [section 7](#7-preparing-images).

### Editing several files at once

On the repository page, press the **`.`** (period) key. This opens a full
editor in your browser (called github.dev) where you can change several files
and save them together. Use the **Source Control** icon on the left to commit.

### Checking that it published

Open the [**Actions** tab](https://github.com/brianbarnardart/brianbarnardart.com/actions).
The top run is your change:

- 🟡 yellow dot: still building, wait a minute.
- ✅ green check: it's live.
- ❌ red X: something needs fixing, and the old site is still up. See [section 8](#8-when-the-build-fails-red-x).

Yellow ⚠️ **warnings** (for example "image is 4,000 KB") don't block
publishing. They're suggestions.

---

## 5. Undoing a mistake

Every version of every file is kept forever, so nothing is ever truly lost.

**To put a file back the way it was:**

1. Open the file on GitHub and click **History** (top right).
2. Find the version from before the mistake and click it, then click
   **View file** (or the `<>` "Browse" button).
3. Click **Raw**, then select all and copy.
4. Go back to the current file, click the pencil, replace everything with
   what you copied, and commit with a note like "Restore events page".

**To bring back a deleted file:** open the [commit history](https://github.com/brianbarnardart/brianbarnardart.com/commits/main),
find the commit that deleted it, view the file as it was in the commit
*before* that, and re-create it with the same name and contents.

---

## 6. Recipes: common tasks

> **The golden rule for every page:** each page file starts with a small
> settings box between two `---` lines (the technical name is "front matter").
> It holds the page's title, description and picture. Copy an existing file's
> box as your starting point, and see [section 13](#13-reference-front-matter-fields)
> for what each setting means.

### Update the events page

Edit `events.md`. Write it like a short letter, e.g. "Friday Dec 5 and
Saturday Dec 6: painting live at [The Green Turtle](/venues/the-green-turtle/)".
Concrete dates and venue names also help people find the page in search.

### Add a YouTube Short to the home page

1. Copy the Short's link, e.g. `https://www.youtube.com/shorts/AbCdEf12345`.
   The **id** is the part after `/shorts/`: `AbCdEf12345`.
2. Edit `_data/shorts.yml` and add, at the top of the list:
   ```yaml
   - id: AbCdEf12345
     title: w/[Band Name](https://link-to-band)
   ```
   The `title` appears as the caption under the video.

### Add a print

1. Upload the photo to `assets/prints/` ([shrink it first](#7-preparing-images)).
2. Edit `_data/prints.yml` (or `_data/lebowski_prints.yml`) and add:
   ```yaml
   - title: Wild Mountain Fox Jam
     url: /works/wild-mountain-fox-jam/   # optional: link to the painting's page
     image: /assets/prints/fox-jam-print.jpg
     alt: Brian holding a signed Wild Mountain Fox Jam print
     notes: 11x14 signed print
   ```
3. To remove a print, delete its block (from its `- title:` line through the
   end of that entry).

Optional extras for each print:

| Field | What it does |
|---|---|
| `thumb:` | A smaller image for the grid (the full `image` opens when clicked) |
| `buy_url:` | Shows a **Buy Print** button linking to a payment page (see [section 11](#11-selling-prints-now-and-later)) |
| `price:` | Shown on the Buy button, e.g. `price: "$45"` |

### Add a new print category (like the Lebowski page)

1. Copy `prints/the-big-lebowski.md` to a new file, e.g. `prints/turtles.md`.
2. Change `title`, `permalink` (`/prints/turtles/`), `description`, `image`,
   and the wording.
3. Create a matching list, e.g. `_data/turtle_prints.yml`, and change the
   include line in the new page to `items=site.data.turtle_prints`.

The main `/prints/` page lists every category automatically. And if any page
on the site has the same final URL word (e.g. a page at `/interests/turtles/`),
its **Get Prints** ribbon will point at `/prints/turtles/` automatically.

### Add a painting to the Gallery

1. Upload the image to `assets/paintings/` with a lowercase, hyphenated name,
   e.g. `moonlight-shrimp-boat.jpg` ([shrink it first](#7-preparing-images)).
2. In `_works/`, choose **Add file → Create new file**, name it
   `moonlight-shrimp-boat.md`, and paste:
   ```yaml
   ---
   layout: artwork
   title: Moonlight Shrimp Boat
   image: /assets/paintings/moonlight-shrimp-boat.jpg
   medium: Acrylic on canvas
   dimensions: '24" x 36"'
   year: 2026
   price: "$850"
   order: 5
   description: Original acrylic painting of a Fernandina Beach shrimp boat under moonlight by Brian Barnard.
   ---

   A few sentences about the painting. Quotes from Brian are lovely here.
   ```
3. Commit. It appears in the Gallery and gets its own page at
   `/works/moonlight-shrimp-boat/`.

**Notes:**
- `price:` present → the page shows an "Interested in this piece?" form.
  `price:` absent → it shows "This piece has found a home."
- `order:` controls position in the Gallery (lower numbers first). Paintings
  without `order` go at the end.
- Measurements contain `"`, so wrap them in **single quotes**: `'24" x 36"'`.

### Mark a painting as sold

Delete the `price:` line from its file in `_works/`.

### Take a painting out of the Gallery without deleting its page

Move its file into `_works/archive/` (on GitHub: edit the file and change the
filename box to `archive/its-name.md`). The page keeps working at the same
address, so old links don't break, but it no longer appears in the Gallery or
its previous/next arrows.

### Add a page to the top menu

Add `nav: 4` (any number) to the page's front matter. Menu items are sorted by
this number. Remove the line to take it out of the menu.

### Work on a page that isn't ready yet

Add these two lines to its front matter:
```yaml
noindex: true
sitemap: false
```
Search engines are asked to ignore it, but anyone with the address can still
see it. To hide it completely, use `published: false` instead (the page isn't
built at all).

### Change a social media link

Social links appear in **two** places. Update both:
1. `_includes/footer.html`: the icons at the bottom of every page.
2. `_includes/custom-head.html`: the `sameAs` list, which tells search
   engines "these profiles are the same Brian Barnard."

### Change the browser-tab title or site description

Edit `_config.yml`:
- `title:` is "Brian Barnard Art", used everywhere.
- `tagline:` is added to the home page title only: *Brian Barnard Art | Fernandina Beach Artist & Live Painter*.
- `description:` is the default summary used by search engines.

---

## 7. Preparing images

**Thumbnails are automatic.** Each time the site publishes, GitHub makes a
small copy of every picture for the Gallery and Prints grids, and shrinks any
picture wider than 2000 pixels. Your original file is never changed. So you
no longer have to fuss over exact sizes, but smaller uploads still publish
faster and keep the project light.

Phone and camera photos are often **3–10 MB**. That's far too big to keep
in GitHub, because every file stays in the project history forever, even
if deleted later. **Aim for under 500 KB per image.**

**Easiest way, free and in your browser:** [squoosh.app](https://squoosh.app)

1. Drop the image onto the page.
2. On the right, tick **Resize** and set the width (or height, for tall
   images) to **2000** pixels.
3. Choose **MozJPEG** and set quality to about **75**.
4. Check the file size shown at the bottom right, then click the download button.

**Naming:** lowercase, words separated by hyphens, no spaces:
`pink-sky-terrapin.jpg`, not `Pink Sky Terrapin.JPG`. On the web,
`Painting.JPG` and `painting.jpg` are *different files*.

**Print photos:** "in-hand" shots (Brian holding the print) work best. They
show it really comes from him.

The automatic check shows a yellow ⚠️ warning for any image over 1 MB.

---

## 8. When the build fails (red X)

Remember: **the old site is still live.** Nothing is broken for visitors.

1. Open the [Actions tab](https://github.com/brianbarnardart/brianbarnardart.com/actions),
   click the failed run, then click **build** to see the step that failed.
2. Read the message. It usually names the file. Common ones:

| Message says… | What it means | Fix |
|---|---|---|
| `missing description for indexable page` | A public page has no `description:` | Add a one or two sentence `description:` to its front matter (or mark it draft, see [section 6](#work-on-a-page-that-isnt-ready-yet)) |
| `missing image for indexable page` | A public page has no `image:` | Add `image: /assets/...` (the picture shown when the link is shared) |
| `broken absolute internal link /something` | A link or image points to something that doesn't exist | Check spelling and capitalization of the path; make sure the image was uploaded |
| `invalid YAML front matter` / `did not find expected key` / `mapping values are not allowed` | The settings box at the top of a page is typed wrong | See below |
| An error mentioning `Liquid` | A bit of code in `{% … %}` or `{{ … }}` is mistyped | Compare with the same bit in another file |

**Settings-box formatting tips** (front matter, also called YAML):
- If a value contains a colon followed by a space (`: `), wrap it in quotes:
  `description: "Meet Frog King: the mascot"`
- If a value contains `"`, wrap it in single quotes: `dimensions: '24" x 36"'`
- Use spaces, never tabs, for indentation.
- Both `---` lines must be present, each on its own line.

**Still stuck?** Undo the last change ([section 5](#5-undoing-a-mistake)) to
get back to a working state, then ask for help ([section 12](#12-getting-help-including-from-ai-assistants)).

**If it fails and you didn't change anything relevant**, GitHub's free tools
may have been updated. The live site isn't affected. Ask a technical friend
or an AI assistant, and show them the error message.

---

## 9. Messages from the contact and print forms

1. A visitor fills in a form on the site.
2. **FormSpark** receives it and emails it to the address configured in the
   FormSpark dashboard.
3. As a backup, a note that a form was sent (including the sender's email
   address) is also logged in **GoatCounter**, so a lost message can be traced.

**If messages stop arriving:**
- Check the spam/junk folder.
- Log into [formspark.io](https://formspark.io) and look at **Submissions**.
  If messages are there, the email forwarding is the problem. Check the
  notification settings.
- Check the FormSpark plan's remaining submission allowance.
- In GoatCounter, look for events named `…#form-submit`, `…#form-success`,
  and `…#form-failure`.

**To send form messages to a different email address,** change it in the
FormSpark dashboard. No website edit is needed.

**To switch to a different form service,** the form's address is set in one
place: the `action="https://api.formspark.io/…"` line in `_includes/contact-form.html`.

---

## 10. Search engines (Google and Bing)

The full plan is in [`SEO-STRATEGY.md`](SEO-STRATEGY.md). What a caretaker
needs to know:

- **Already automatic:** a sitemap (list of pages for search engines), page
  descriptions, preview images for shared links, and structured data that
  tells search engines who Brian is, where he works, and which social profiles
  are his. After each publish, Bing is notified automatically (IndexNow).
- **Every public page needs `description:` and `image:`.** The automatic
  check enforces this.
- **Write descriptions for people.** One or two natural sentences about what
  the page is, ideally mentioning Fernandina Beach where it fits. Don't stuff
  keywords.
- **Real content wins.** Concrete event dates, painting stories, venue names,
  and band names are what search engines (and people) reward.

**A few times a year:**
- [ ] Log into [Google Search Console](https://search.google.com/search-console)
      and [Bing Webmaster Tools](https://www.bing.com/webmasters). Look for
      warnings and confirm the sitemap shows as "Success".
- [ ] Check that the **Google Business Profile** and **Bing Places** listings
      are still accurate.
- [ ] Ask venues, event organizers, and local news to link to
      `https://brianbarnardart.com` when they mention Brian. Links from local
      sites are the best way to make search engines connect *this* Brian
      Barnard with Fernandina Beach.

---

## 11. Selling prints: now and later

The print pages (`/prints/` and `/prints/the-big-lebowski/`) are designed to
grow in stages, with **no monthly costs** at any stage.

### Stage 1: Personal requests (current)

Visitors use the form to say which prints they want, how many, and their ZIP
code. Brian (or a helper) replies with the total including shipping, collects
payment directly (Venmo, Zelle, check), and mails the print.

**Shipping tips:**
- Small prints (5×7, 8×10): plastic sleeve plus a rigid cardboard "photo
  mailer" envelope.
- Larger prints (11×14 and up): sleeve plus a 3-inch mailing tube.
- Discounted USPS labels at home: [PirateShip.com](https://www.pirateship.com) (free account).
- A signature on the print adds a lot of value to the buyer.

### Stage 2: "Buy" buttons (when replying to every request gets tiring)

No store software is needed. A payment service hosts the checkout page:

1. Create a free account at [stripe.com](https://stripe.com) (Square has the
   same feature). There's no monthly fee, only a per-sale card fee.
2. In Stripe: **Payment Links → New**. Enter the print name and price (include
   shipping in the price for simplicity) and turn on **Collect shipping address**.
3. Copy the link it gives you (like `https://buy.stripe.com/abc123`).
4. In `_data/prints.yml`, add two lines to that print:
   ```yaml
     buy_url: https://buy.stripe.com/abc123
     price: "$45"
   ```
5. A **Buy Print ($45)** button appears. Stripe emails you each order with the
   buyer's address and deposits the money.

### Stage 3: Print-on-demand (when packing and shipping isn't practical)

A fine-art print lab (e.g. Prodigi, FinerWorks, or a local giclée printer
offering drop-shipping) keeps high-resolution scans and prints, packs, and
ships each order directly to the buyer. Their product links can go in
`buy_url:` exactly like Stage 2.

---

## 12. Getting help (including from AI assistants)

AI assistants (ChatGPT, Claude, GitHub Copilot, Gemini) are genuinely good at
helping with this kind of site.

- **For a build error:** paste the error message from the Actions page *and*
  the contents of the file you changed, and ask "How do I fix this Jekyll
  build error?"
- **For bigger changes**, use an assistant that can read the whole repository
  (e.g. Claude Code, GitHub Copilot, or Codex). The file [`AGENTS.md`](AGENTS.md)
  tells AI assistants this site's rules, so they don't undo deliberate choices.
- **Always look at what an AI changed before committing.** If something looks
  wrong, the automatic checks and [undo](#5-undoing-a-mistake) are your safety net.

**More documentation in this repository:**

| File | For |
|---|---|
| [`README.md`](README.md) | Technical overview |
| [`SEO-STRATEGY.md`](SEO-STRATEGY.md) | Search engine plan and status |
| [`HOWTO.md`](HOWTO.md) | Building a site like this for yourself (domains, DNS, hosting) |
| [`_layouts/README.md`](_layouts/README.md) | Page templates (technical) |
| [`_includes/README.md`](_includes/README.md) | Reusable pieces (figures, forms, etc.) (technical) |

---

## 13. Reference: front matter fields

| Field | Used on | Meaning |
|---|---|---|
| `layout` | all | Template: `page` (normal pages), `artwork` (paintings), `article` (venues, characters, interests), `home` (home page only) |
| `title` | all | Page name. Shown in the browser tab as "Title \| Brian Barnard Art" |
| `description` | public pages | One or two sentences for search results and link previews. **Required** on public pages. |
| `image` | public pages | Picture shown when the link is shared (texts, Facebook). **Required** on public pages. On paintings, it's also the main image. |
| `permalink` | pages | The address, e.g. `/events/`. Collection items (paintings, venues) get theirs automatically. |
| `nav` | pages | Number to put the page in the top menu (sorted ascending) |
| `noindex` / `sitemap` | any | `noindex: true` plus `sitemap: false` keeps a draft out of search engines |
| `published` | any | `published: false` means the page isn't built at all |
| `prints_url` | any | Where this page's **Get Prints** ribbon points (normally automatic) |
| `medium`, `dimensions`, `year` | paintings | Details shown beside the painting |
| `price` | paintings | Shows the price and an inquiry form. Remove the line when sold. |
| `order` | paintings | Position in the Gallery (lower first) |
| `subtitle` | articles | Line under the heading (venues use it for address and phone) |
| `cover_image` | articles | Not currently displayed. Kept for possible future use. |

---

## 14. Reference: Markdown cheat sheet

Pages are written in **Markdown**, plain text with a few symbols for
formatting. [Full reference](https://kramdown.gettalong.org/quickref.html).

```markdown
# Big heading
## Section heading
### Smaller heading

*italic*   **bold**   ~~strikethrough~~

[link text](https://example.com)      ← link to another site
[Contact Brian](/contact/)            ← link within this site

- bullet item
- another

1. numbered item
2. another

> A quote, shown indented.

---   ← a horizontal line (on its own line, with blank lines around it)
```

**Images with captions** use the site's figure helper (it also makes the image
open larger when clicked):

```liquid
{% include figure.html image="/assets/paintings/example.jpg" caption="Caption with **bold** allowed" side="right" %}
```

`side` can be `left`, `right`, or left out for full width. Other options
(`alt`, `maxwidth`, `link`, `lightbox="no"`) are described in
[`_includes/README.md`](_includes/README.md).

**Pull quotes:**

```liquid
{% include callout.html quote="Words worth highlighting" side="right" %}
```

Anything inside `{% … %}` or `{{ … }}` is a template instruction. Copy
these from existing pages rather than writing them from scratch.
