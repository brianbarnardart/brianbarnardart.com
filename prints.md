---
layout: page
title: Prints
permalink: /prints/
description: Order signed Brian Barnard art prints directly through a personal request form with current offerings listed in one place.
image: /assets/paintings/wild-mountain-fox-jam.jpg
---

# Prints

If you want a print, you're talking to a human — not clicking through an impersonal store checkout.

That is on purpose.

Brian handles print requests personally so he can confirm availability, make sure you're getting the right piece, and coordinate shipping directly.

## Current Print Offerings

{% if site.data.prints and site.data.prints.size > 0 %}
<ul>
{% for print in site.data.prints %}
  <li>
    <strong><a href="{{ print.url | relative_url }}">{{ print.title }}</a></strong>
    {% if print.notes %} — {{ print.notes }}{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<p>Print inventory is being updated right now — please use the form below and describe what you're looking for.</p>
{% endif %}

## How ordering works

1. Send your request through the form below (include print title(s), quantity, and shipping ZIP code).
2. Brian confirms availability and total cost (print + shipping).
3. Payment is coordinated directly (typically Venmo), then the print is packed and mailed.

If you're local, pickup may be possible depending on schedule.

## Request Prints

{% include contact-form.html
  id="prints-form"
  submit_text="Send Print Request"
  message_placeholder="Which print(s) do you want? Include quantity, shipping ZIP code, and any notes."
  success_message="Thanks! Your print request was sent. Brian will follow up with availability and shipping details." %}
