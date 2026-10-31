---
layout: page
title: Prints
permalink: /prints/
description: Order Art Prints Directly from Brian Barnard via personal request.
image: /assets/prints/fox-jam-print-fake.jpg
---

# Prints

Selling prints online is very new for Brian, and his team is handling print
requests personally.  This way we can confirm availability, make sure you're
getting the right piece(s), and coordinate shipping directly.

<sub>(Doing this *might* be because we don't actually know how to make our own
online store. 🙈  *BUT* the personal touch is preferable anyway!)</sub>

## Current Offerings (PROTOTYPE!)

{% include prints-grid.html items=site.data.prints %}

*(The idea is that Brian would have his hand in photographs holding prints in
front of one of his murals, but it is being prototyped with postcards.)*

{% assign _print_sections = site.pages | where_exp: "p", "p.url != '/prints/' and p.url contains '/prints/' and p.title and p.noindex != true and p.sitemap != false" | sort: "title" %}
{% if _print_sections and _print_sections.size > 0 %}
## Print Categories

{% for section in _print_sections %}
- **[{{ section.title }}]({{ section.url | relative_url }})**
{% endfor %}
{% endif %}

## How ordering works

1. Send your request through the form below (include print title(s), quantity, and shipping ZIP code).
2. We confirm availability and total cost (prints + shipping).
3. Payment is coordinated directly (typically Venmo), then the prints are packed and mailed.

## Request Prints

{% include contact-form.html
  id="prints-form"
  submit_text="Send Print Request"
  message_placeholder="Which print(s) do you want? Include quantity, shipping ZIP code, and any notes."
  success_message="Thanks! Your print request was sent. We will follow up with availability and shipping details." %}
