# Want to use this site's method?

This repository is for [brianbarnardart.com](https://brianbarnardart.com), but the
approach it uses — GitHub Pages + Jekyll + a custom domain — is something anyone
can adopt. This document explains how it works, what it costs, what the risks are,
and how to decide whether it's a good fit for you.

The audience for this document is someone who has heard of GitHub and is comfortable
learning by doing — maybe with some help from an AI assistant. Deep technical
knowledge is not required.

---

## Is this approach right for you?

**Good fit:**

- A portfolio, artist site, small business website, or personal blog
- Content is mostly text and images; video can be embedded from YouTube or Vimeo
- You're comfortable with the site's source code being public (your art and your
  words stay copyright-protected regardless of whether the HTML around them is
  visible)
- You want ongoing costs as low as possible — essentially just the domain name,
  around $10–15 per year

**Not a good fit:**

- E-commerce with a shopping cart (you need server-side code and a payment
  processor like Shopify or Stripe — GitHub Pages can't do that)
- Real-time features — live chat, booking systems, user accounts, comment threads
- You need the site's code kept private
- You expect very high traffic with large media files served directly (video should
  live elsewhere — see [Media hosting](#media-hosting) below)

---

## What are all these pieces?

### Domain name

A **domain name** is the address people type to reach your site — for example,
`yourdomain.com`. You don't buy a domain name outright; you *rent* it year to year
from a company called a **registrar**, usually for about $10–15 per year. If you
stop paying, the name becomes available for someone else to register.

**The domain name is the one asset you truly control in this arrangement.** The
hosting, the files, the build pipeline — all of that can be moved in an afternoon.
The domain is your address, and you can redirect it anywhere if you ever switch
hosts. Pick a registrar you trust, keep your billing information current, and set
a calendar reminder to renew before the expiration date.

### DNS

**DNS** (Domain Name System) is the part of the internet that translates
`yourdomain.com` into a numeric address so browsers can find the right server.
Think of it as the internet's phonebook. When you own a domain, you control its
DNS records. A couple of those records will say "this domain points to GitHub
Pages." You'll set those up in [Step 4](#step-4-connect-your-domain-to-github-pages).

### GitHub and GitHub Pages

**[GitHub](https://github.com)** is a platform for storing and sharing code —
owned by Microsoft. **GitHub Pages** is a free service within GitHub that turns a
repository (a project folder) into a live website. It has been free since 2008
and is used by millions of people for exactly this kind of site.

### Jekyll

**[Jekyll](https://jekyllrb.com/)** is a program that reads plain text files —
Markdown, HTML, CSS, YAML — and produces a finished website. There is no database
and no server-side code to maintain or keep secure. You write your content; Jekyll
assembles the pages.

### GitHub Actions

**GitHub Actions** is a free automation system built into GitHub. The repository
includes a small workflow file that tells GitHub: "whenever a change is pushed,
run Jekyll and publish the result." You don't need to run anything on your own
computer to deploy — just push your changes.

---

## Setting up the pieces

### Step 1: Register a domain name

1. Search for the name you want at one of the registrars below.
2. Check that the name isn't trademarked or already closely associated with
   something well-known.
3. Register it. A `.com` is still the most universally recognized, but `.art`,
   `.studio`, `.net`, `.co`, and many others work fine.
4. Write down your registrar login credentials and store them somewhere safe.
   You'll need them periodically to renew and to update DNS settings.

Registrars worth considering:

| Registrar | Notes |
|---|---|
| [Cloudflare Registrar](https://www.cloudflare.com/registrar/) | Sells at cost — no markup; you pay the wholesale price |
| [Namecheap](https://www.namecheap.com/) | Straightforward, reasonable prices, long track record |
| [Squarespace Domains](https://domains.squarespace.com/) | The former Google Domains, still works fine |

Avoid registrars that bundle the domain with expensive hosting packages you
don't need. Aggressive upselling during checkout is a red flag.

### Step 2: Create a GitHub account and repository

1. Create a free account at [github.com](https://github.com) if you don't have one.
2. Create a new **repository** (a project folder on GitHub). The name can be
   anything.
3. Set the repository to **Public** — this is required for free GitHub Pages
   hosting. (Your art and words are still copyrighted; the *code structure* is
   what's visible.)

### Step 3: Put your site files in the repository

The fastest starting point is to copy a working Jekyll site and replace the
content with your own. This repository is open source (the code, not the art or
text), and you are welcome to use it as a template — just:

- Replace all the content (text, images, artist-specific details) with your own
- Change the visual style so the two sites don't look identical
- Update `_config.yml` with your site's title, URL, and description
- Update the `CNAME` file with your own domain name

At a minimum the repository needs:

- `_config.yml` — site-wide settings (title, URL, theme)
- `index.md` — the home page
- `Gemfile` — lists Jekyll and its dependencies
- `.github/workflows/` — a GitHub Actions workflow that builds and publishes the
  site automatically

If you start from a copy of this repository, all of those are already in place.

### Step 4: Enable GitHub Pages

1. In your repository on GitHub, go to **Settings → Pages**.
2. Under **Source**, choose **GitHub Actions**.
3. Push a change to trigger the first build. After a minute or two the site will
   be live at `https://yourusername.github.io/your-repository-name/`.

### Step 5: Connect your domain to GitHub Pages

This is the step that makes `yourdomain.com` point to your GitHub Pages site
instead of the `yourusername.github.io` URL.

**In your GitHub repository:**

1. Go to **Settings → Pages**.
2. Under **Custom domain**, enter your domain name (e.g. `yourdomain.com`) and
   save. GitHub will warn you that DNS isn't configured yet — that's expected.
3. GitHub adds a file called `CNAME` to your repository containing your domain
   name. Don't delete it.

**At your domain registrar:**

Log in and find the DNS settings for your domain. Add these four **A records**
(they are GitHub Pages' IP addresses and have been stable for years):

| Type | Host/Name | Value |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |

`@` means the root domain itself (`yourdomain.com`).

If you also want `www.yourdomain.com` to work, add one **CNAME record**:

| Type | Host/Name | Value |
|---|---|---|
| CNAME | `www` | `yourusername.github.io` |

DNS changes take anywhere from a few minutes to a few hours to propagate. You
can check progress at [dnschecker.org](https://dnschecker.org). Once GitHub
detects the DNS is correct it provisions your HTTPS certificate automatically —
usually within an hour.

### HTTPS: the padlock in the browser

GitHub Pages automatically provisions a free HTTPS certificate through
**[Let's Encrypt](https://letsencrypt.org/)**, a nonprofit that provides free
certificates to make the web more secure. You don't need to do anything. Once
your DNS is working and GitHub confirms it, the certificate appears and
`https://` is live. This used to cost money; now it's automatic.

---

## The risks — and why they're manageable

### "GitHub is owned by Microsoft. What if they charge for Pages?"

GitHub Pages has been free since 2008. Microsoft acquired GitHub in 2018 and kept
the free tier. Nothing stays free forever, but this has been stable for a long
time and there are no announced changes.

More importantly: **your files are plain text files and Jekyll runs anywhere.**
If GitHub Pages ever became paid, injected ads, or did something you didn't like,
you could move the site in an afternoon to one of several alternatives:

- **[Netlify](https://www.netlify.com/)** — free tier, deploys directly from
  GitHub
- **[Cloudflare Pages](https://pages.cloudflare.com/)** — free tier, global
  content delivery network
- **[Render](https://render.com/)** — free static site hosting

The move: update a DNS record at your registrar, point it at the new host, done.
Your domain stays yours. Your content stays yours.

**This is why owning your domain name separately from your host matters so much.**
The domain is the one thing they can't take away. If the host changes, you just
update the phonebook entry.

### "Anyone can see my code"

Yes, the HTML, CSS, and site structure are public. For an artist's portfolio
this is fine:

- Your **art** is copyright-protected regardless of whether someone can see the
  HTML page that shows it.
- Your **text** is copyright-protected.
- The code — layouts, CSS, JavaScript — is the architecture of the building, not
  the artwork inside.

Being public is the tradeoff for free hosting. If you'd prefer your code to stay
private, GitHub, Netlify, and Cloudflare Pages all offer paid plans that support
private repositories with the same free Pages-style hosting.

### "What about ads, or serving content differently to different people?"

GitHub Pages does not inject ads. You control exactly what gets served — the
output is the HTML files Jekyll builds from your source.

The concern that a host might show different content to different visitors (based
on geography, logged-in state, etc.) is real for dynamic platforms. For a static
site served from GitHub Pages, the files are the files. Everyone gets the same
thing.

And again: if GitHub ever did something like that, the escape hatch is just a DNS
change away.

### "Does it matter which top-level domain I choose — .com vs .art vs .tv?"

Yes, and the difference matters more than most people realize.

Every domain name ends in a **top-level domain** (TLD) — the part after the last
dot. They fall into two broad categories:

**Generic TLDs** (gTLDs) like `.com`, `.net`, `.org`, `.art`, `.studio`, `.co`
are administered under contract with
**[ICANN](https://www.icann.org/)**, an international nonprofit that coordinates
the internet's naming system. ICANN is imperfect and sometimes controversial, but
its governance is multilateral and public. The rules for who can register these
names are set in those contracts and are relatively stable.

**Country-code TLDs** (ccTLDs) like `.tv`, `.io`, `.ai`, `.fm`, `.me`, `.co.uk`
are a different story. Each one is assigned to a specific country — the country's
government has ultimate authority over it. When you register a `.tv` domain you
are renting a name in Tuvalu's namespace. When you register `.io` you are in the
British Indian Ocean Territory's namespace.

The risk: a country can change its registration policies, restrict who can hold
names, impose new fees, or — in an extreme case — lose administrative control
over its TLD entirely. In 2024 the U.S. government revoked control of `.io` from
its contracted registry following a political dispute over the status of the
British Indian Ocean Territory; the long-term fate of existing `.io` domains
became genuinely uncertain for a period. `.tv` is owned by Tuvalu, a small island
nation whose long-term existence is threatened by rising sea levels. `.ai` is
Anguilla, a British overseas territory. These are real places with real politics.

This doesn't mean you should never use a ccTLD. Many are so entrenched in their
industry that the brand value outweighs the risk (`.io` in tech, `.fm` in
podcasting). But you should go in with eyes open:

| TLD | Jurisdiction | Notes |
|---|---|---|
| `.com` / `.net` / `.org` | ICANN generic | Most stable; universally recognized |
| `.art` / `.studio` / `.co` | ICANN generic | Fine; newer but governed the same way |
| `.ai` | Anguilla | Popular in AI industry; ccTLD risk applies |
| `.io` | British Indian Ocean Territory | Widespread in tech; governance recently disrupted |
| `.tv` | Tuvalu | Popular in streaming; ccTLD risk applies |
| `.fm` | Micronesia | Common in podcasting; ccTLD risk applies |
| `.me` | Montenegro | Common for personal sites; ccTLD risk applies |

**The practical advice:** for a portfolio or small business site where the domain
is your long-term address, start with a generic TLD. `.com` remains the default
expectation for most people. `.art`, `.studio`, and similar newer generics are
legitimate alternatives. Use a ccTLD only if the branding benefit is compelling
and you're willing to keep an eye on the news.

---

## Media hosting

GitHub Pages is not designed for large media files. The free tier has storage and
bandwidth limits, large binary files bloat your repository's history, and slow
assets hurt your visitors' experience.

**For video:** embed from **[YouTube](https://youtube.com)** or
**[Vimeo](https://vimeo.com)**. They handle delivery, transcoding, and bandwidth.
You keep your original files.

**For audio:** embed from **[SoundCloud](https://soundcloud.com)** or
**[Bandcamp](https://bandcamp.com)**.

**For large images or downloadable files:** consider an object-storage service
under a subdomain like `media.yourdomain.com`:

| Service | Notes |
|---|---|
| [Cloudflare R2](https://www.cloudflare.com/products/r2/) | No egress fees, generous free tier |
| [Backblaze B2](https://www.backblaze.com/cloud-storage) | Very cheap; pairs well with Cloudflare |
| [Bunny.net](https://bunny.net/) | CDN and storage, competitive pricing |

The general pattern: host the *website* — HTML, CSS, small images — on GitHub
Pages, and point large media at a separate service under a subdomain. This keeps
your repository small, your build fast, and your bandwidth costs low.

---

## Summary

| What you pay for | What you get for free |
|---|---|
| Domain name (~$10–15/year) | Hosting |
| Large media storage, if you need it | HTTPS certificate |
| | Build and deploy pipeline |
| | Version history of every change |

The domain name is the only essential ongoing cost. Everything else is free unless
your needs grow beyond the free tiers.

This approach works well for **artists, musicians, writers, and small local
businesses** who want a professional presence on the web without paying for hosting
they don't actually need — and who value being able to pick up and move if
circumstances change.

---

*This document describes the approach used at
[brianbarnardart.com](https://brianbarnardart.com). The site's source code is
released under [Creative Commons CC-0](https://creativecommons.org/). The artwork
and text on the site are copyright Brian Barnard, All Rights Reserved.*
