# brianbarnardart.com — Webmaster & Caretaker User's Guide

This guide is written for whoever is maintaining **brianbarnardart.com** — whether that is Brian himself, a family member, or a friend helping to look after the site. 

You do **not** need a computer science background or software development experience to keep this website updated and running. This document explains how everything works in plain language, where the important accounts live, how to make updates right in your web browser, and how to avoid common pitfalls.

---

## 1. Quick Overview: How This Website Works

- **Website URL:** [https://brianbarnardart.com](https://brianbarnardart.com)
- **Hosting:** Free on **GitHub Pages** (owned by Microsoft). There is no monthly hosting bill.
- **Technology:** **Jekyll** (a static site generator). All website content is stored in plain text files (Markdown `.md` and YAML `.yml`) and image files (`.jpg`, `.png`).
- **How updates work:** Whenever a change is saved (committed) to the `main` branch on GitHub, an automated robot (GitHub Actions) builds the website and publishes it live within 1 to 2 minutes.

---

## 2. The "Keys to the Kingdom" (Crucial Accounts)

To ensure continuity, keep a secure record (such as in a password manager like 1Password, Bitwarden, or a physical notebook in a safe place) of login credentials for these accounts:

| Service | What It Controls | Why It Matters |
|---|---|---|
| **Domain Registrar** (e.g. Cloudflare, Namecheap, GoDaddy) | The domain name `brianbarnardart.com` | **Most important.** Renewed annually (~$10–$15/yr). If this expires, the website goes down. Ensure auto-renew is ON with a current credit card. |
| **GitHub Account** | The repository `brianbarnardart/brianbarnardart.com` | Contains all site text, pictures, layouts, and deployment workflows. |
| **FormSpark** ([formspark.io](https://formspark.io)) | Contact & Print Request forms (Form ID: `AvqUDoWyl`) | Receives messages from the website and forwards them to Brian's email. |
| **GoatCounter** ([goatcounter.com](https://www.goatcounter.com)) | Privacy-respecting visitor analytics | Shows visitor counts and popular pages without cookies or invasive trackers. |
| **Social Media Accounts** | Facebook, Instagram, YouTube | Connected to the site footer and search engine identity. |
| **Merchandise / Printing** | Sticker Mule (t-shirts), print suppliers | Where physical merch links go. |

---

## 3. How to Make Edits Without Any Technical Tools

You do not need to install git, Ruby, or a terminal on your computer. You can make almost all edits directly on GitHub using a standard web browser:

1. Log into your account on [github.com](https://github.com).
2. Go to the repository: `https://github.com/brianbarnardart/brianbarnardart.com`.
3. Click on the file you want to edit (for example, `events.md` or `_data/prints.yml`).
4. Click the **Pencil icon** (Edit this file) in the upper right.
5. Make your edits to the text.
6. Scroll to the bottom, write a brief note (e.g., "Update event dates"), and click **Commit changes** (ensure "Commit directly to the `main` branch" is selected).
7. Wait ~90 seconds. Refresh [brianbarnardart.com](https://brianbarnardart.com) to see your changes live!

---

## 4. The "Golden Rules" to Keep the Site Building

The site has an automated safety check that runs on every save. If a file breaks these rules, GitHub will show a **Red X** and will **refuse to publish** until it is fixed.

### Rule 1: Every new `.md` page must have front matter
The top of every page file must start and end with three dashes `---`:
```yaml
---
layout: page
title: Title of Page
description: A 1-2 sentence summary for Google search results.
image: /assets/paintings/example.jpg
---
```
- **`layout:`** Must be provided (usually `page`, `article`, or `artwork`).
- **`description:`** Required on all public pages (used by search engines).
- **`image:`** Required on all public pages (used when sharing links on Facebook/iMessage).
- *Exception:* If a page is a draft and not ready for the public, add:
  ```yaml
  noindex: true
  sitemap: false
  ```

### Rule 2: Don't link to files or pages that do not exist
The automated checker scans every internal link and image URL. If you write `[See my art](/gallery-2/)` or `<img src="/assets/missing.jpg">` and that target does not exist, the build will fail.

### Rule 3: Image file paths are case-sensitive
On web servers, `Painting.JPG` is not the same as `painting.jpg`. Always use lowercase names for image files to avoid broken image errors.

---

## 5. Step-by-Step Guides for Common Tasks

### Task A: Updating or Adding an Upcoming Event
- **Where to go:** Open `events.md`.
- **What to do:** Edit the text, dates, venues, or links. If Brian is painting at The Green Turtle on a specific weekend, add the dates under the main heading.
- Click **Commit changes**.

### Task B: Adding a New YouTube Short
- **Where to go:** Open `_data/shorts.yml`.
- **What to do:** If a new Short is published at `https://youtube.com/shorts/AbCdEf12345`, copy the 11-character code at the end (`AbCdEf12345`).
- Add a new block at the top of the file:
  ```yaml
  - id: AbCdEf12345
    title: Live painting at Green Turtle with Smokestack
  ```
- Click **Commit changes**. The Short will immediately appear on the home page.

### Task C: Adding or Updating a Print for Sale
- **Where to go:** Open `_data/prints.yml` (for general prints) or `_data/lebowski_prints.yml` (for Big Lebowski prints).
- **What to do:** Add a new entry:
  ```yaml
  - title: Name of Painting
    url: /works/name-of-piece/ # optional link to full artwork page
    image: /assets/prints/your-print-photo.jpg
    alt: Brian holding signed print of Name of Painting
    notes: 11x14 signed archival print
  ```
- Make sure you upload the photo into `assets/prints/` first (using GitHub's "Upload files" button) so the image path exists!

### Task D: Adding a New Artwork to the Gallery
1. **Upload the image:**
   - In GitHub, navigate into `assets/paintings/`.
   - Click **Add file → Upload files**, drop in your `.jpg` image (e.g. `moonlight-shrimp-boat.jpg`), and commit.
2. **Create the artwork page:**
   - Navigate into `_works/`.
   - Click **Add file → Create new file**.
   - Name it `moonlight-shrimp-boat.md`.
   - Paste in the artwork template:
     ```yaml
     ---
     layout: artwork
     title: Moonlight Shrimp Boat
     image: /assets/paintings/moonlight-shrimp-boat.jpg
     medium: Acrylic on canvas
     dimensions: '24" x 36"'
     year: 2026
     price: $850
     description: Original acrylic painting of a Fernandina Beach shrimp boat under moonlight by Brian Barnard.
     ---

     Painted live during an evening set downtown. Captures the calm waters and working heritage of Amelia Island.
     ```
   - *Note on Price:* If `price:` is included, the page will display an "Interested in this piece?" inquiry form. If `price:` is omitted, the page will show a polite note explaining the original has found a home.
   - Click **Commit changes**. It will now appear in the Gallery and generate its own dedicated page!

---

## 6. How Customer Messages and Print Requests Work

1. **The Visitor:** Fills out a contact form or print request on the website.
2. **FormSpark:** Receives the submission and immediately sends an email notification to the account holder's registered email address with the sender's name, email, phone, and message.
3. **If emails stop arriving:**
   - Log into [formspark.io](https://formspark.io).
   - Check the **Submissions** inbox to see if messages are being recorded there.
   - Check your email's Spam/Junk folder.
   - Verify the email notification settings in the FormSpark dashboard.

---

## 7. Prints & Original Art: Strategy, Scaling & Zero-Risk Evolution

### The Philosophy: Controlling the Artist's Narrative
For many years, Brian operated with no website at all — relying on word of mouth, live shows, Facebook, and YouTube. While social media is great for community buzz, it has severe limitations:
- Algorithms bury posts or demand ad spend.
- It degrades high-resolution images.
- It fails to convey the depth, provenance, and dignity needed when asking $800 to $2,500+ for large, original studio canvases.

This independent website gives Brian an uncompromised anchor where he controls the presentation. The art ecosystem has two main tiers:
1. **Original Works (`/gallery/` and `_works/`):** High-value originals and live commission inquiries. These represent the heart of his artistic reputation.
2. **Art Prints (`/prints/`):** Accessible, affordable pieces ($20–$50) that allow casual fans, tourists, and admirers to take home a piece of the magic without hesitation.

---

### The Three-Phase Evolution for Selling Prints (Zero-Risk & Low-Cost)

The print pages (`/prints/` and `/prints/the-big-lebowski/`) were created as prototypes. The goal is to keep risk and ongoing costs at **absolute zero**. Here is how to scale this gracefully when the time comes:

#### Phase 1: The Personal Request Model (Current State — Zero Cost, Zero Risk)
- **How it works:** Visitors browse the prints and send a request via the contact form with their requested title, quantity, and mailing ZIP code.
- **Why start here:**
  - Cost: **$0.00**. No platform fees, no monthly e-commerce subscriptions.
  - Flexibility: Brian (or his caretaker) confirms print inventory in the studio *before* accepting any money.
  - Personal connection: Allows a warm, human interaction with fans and collectors.
- **Payment & Shipping:**
  - Reply to the inquiry via email with the total cost (print + flat-rate USPS shipping).
  - Collect payment directly via **Venmo** (`@brianbarnardart` or personal handle), **Zelle**, or check.
  - Slip the print into an archival cellophane sleeve with a cardboard backing board, place in a rigid mailer (or poster tube for larger pieces), and mail via USPS Ground Advantage or Priority Mail.

#### Phase 2: Hosted Payment Links (Direct Checkout with Zero Fixed Overhead)
*Activate this phase when manual email correspondence becomes too repetitive or time-consuming, but you still want zero monthly software fees.*

- **The Tool: Stripe Payment Links** (or Square Online Checkout):
  - **No monthly fees.** You only pay standard card processing fees (~2.9% + $0.30 per transaction) *when an actual sale occurs*.
  - You do **not** need Shopify, WooCommerce, or any server backend. The site remains 100% static on GitHub Pages.
- **How to set it up:**
  1. Open a free merchant account at [stripe.com](https://stripe.com).
  2. In the Stripe dashboard, go to **More → Payment Links → New**.
  3. Enter the product title (e.g., *"Wild Mountain Fox Jam — 11x14 Archival Print"*), upload the photo, set the price (e.g., "$45 — includes US shipping"), and check **"Collect customers' shipping addresses"**.
  4. Stripe generates an instant, secure URL like `https://buy.stripe.com/example123`.
  5. In `_data/prints.yml` or on `/prints/`, simply add the link:
     ```yaml
     - title: Wild Mountain Fox Jam
       image: /assets/prints/fox-jam-print.jpg
       notes: 11x14 signed archival print
       buy_url: https://buy.stripe.com/example123
     ```
  6. The template displays a **"Buy Print ($45)"** button.
  7. Customers click and pay using Credit Card, Apple Pay, or Google Pay on Stripe's mobile-optimized hosted checkout.
  8. Stripe automatically deposits the payout into Brian's bank and sends an email receipt containing the customer's full shipping name and address.
  9. Fulfillment: Simply print a USPS shipping label (via PirateShip.com for discounted commercial rates) and drop it in the mailbox.

#### Phase 3: On-Demand Drop-Shipping (Hands-Off Fulfillment)
*Activate this phase if packing, inventory management, or trips to the post office ever become physically taxing or impractical due to health, schedule, or travel.*

- **The Strategy: Partner with an on-demand fine art print lab** (such as **Prodigi**, **FinerWorks**, or a reputable regional fine-art giclée printer):
  - Fine art printers produce high-quality archival giclée prints on demand.
  - High-resolution scans/photographs of the paintings are uploaded once.
  - When an order is placed online, the printer automatically prints, packages, and dropships the print directly to the buyer's doorstep with custom branding labels.
  - **Result:** Income continues, fans get beautiful museum-grade prints, and Brian never has to handle packaging, tape, or post office lines.

---

### Practical Shipping & Presentation Tips for Caretakers
- **Standard Postcard / Small Print Size (5x7 or 8x10):** Rigid photo stay-flat mailers (cardboard envelopes) prevent bending. Always put the print in an acid-free plastic sleeve first to protect against rain/moisture.
- **Medium / Large Prints (11x14 or 12x18):** Heavy-duty kraft mailing tubes (3-inch diameter) are much safer than flat envelopes for larger prints, which postal sorters can easily crease.
- **Signing Prints:** If Brian is available to hand-sign prints with a gold/silver metallic pen or archival pencil on the lower margin, that single touch multiplies the sentimental and collector value tenfold.
- **Cheapest Commercial Postage:** Use [PirateShip.com](https://www.pirateship.com) (100% free account, no monthly fee) to print discounted USPS Priority and Ground Advantage labels right at home.

---

## 8. Search Engines: Google vs. Bing & Fernandina Beach

### Why Google Ranks Brian #1
- The domain name `brianbarnardart.com` exactly matches searches for "Brian Barnard" and "Brian Barnard Art".
- The website is fast, clean, and contains structured data connecting Brian to his Facebook, Instagram, and YouTube channels.

### How to Help Bing and Local Fernandina Beach Searches
Search engines treat national queries differently than local neighborhood searches. To make sure someone standing on Centre Street in Fernandina Beach searching "Brian Barnard" gets this exact local artist:

1. **Google Business Profile (Essential):**
   - If not already done, claim or create a profile at [google.com/business](https://google.com/business).
   - Category: **Artist** or **Art Studio**.
   - Location: Fernandina Beach, FL.
   - Website: `https://brianbarnardart.com`.
   - *This puts Brian directly into the Google Maps "Local 3-Pack" at the top of phone searches.*
2. **Bing Places for Business:**
   - Go to [bingplaces.com](https://www.bingplaces.com).
   - Click "Import from Google Business Profile". Bing will automatically import and verify the profile in under two minutes.
3. **Local Citations:**
   - Ensure local venues (The Green Turtle, The Inkwell, Amelia Island tourist guides) link directly to `https://brianbarnardart.com`.

---

## 9. Troubleshooting & Getting Help

- **"I edited a file, but the website didn't change."**
  - Go to `https://github.com/brianbarnardart/brianbarnardart.com/actions`.
  - Look at the latest run at the top.
  - If it has a **Green Checkmark**, the build succeeded. Hard-refresh your browser (`Ctrl+F5` or `Cmd+Shift+R`) to clear cache.
  - If it has a **Red X**, click into the run, click **build**, and read the error message. It will tell you the exact file and line that caused the issue (e.g., "missing description" or "broken internal link").
- **"I don't know how to fix a build error."**
  - Any AI assistant (like GitHub Copilot or ChatGPT) can solve it in seconds: copy and paste the error message from GitHub Actions and the text of the file you edited, and ask: *"How do I fix this Jekyll build error?"*
