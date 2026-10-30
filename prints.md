---
layout: page
title: Prints
permalink: /prints/
description: Order signed Brian Barnard art prints directly through a personal request form with current offerings listed in one place.
image: /assets/paintings/wild-mountain-fox-jam.jpg
---

# Prints

The cheapest *(and most fun)* way to get a print of Brian's work is to come see
a live painting show in Fernandina!  He always has an assortment of prints with
him, so you can avoid shipping costs (and he'll likely cut you a deal if you
buy more than one...) 💸🙂

Selling prints online is very new for Brian, and he is handling print requests
personally.  So he can confirm availability, make sure you're getting the right
piece(s), and coordinate shipping directly.  It's also a chance to say hello
and how you found out about his work.

<sub>(Doing it this way also may be because we don't really know a good way of
making an online store. 🙈  *BUT* the personal touch is preferable anyway!)</sub>

## Current Print Offerings

**NOTE--THIS IS A PROTOTYPE!  Concept is Brian holding the prints in front of
various parts of the Green Turtle mural at various angles with his hand in the
picture.  This is just doing it with a couple of postcards to demo the concept.**

{% if site.data.prints and site.data.prints.size > 0 %}
<div class="gallery-grid">
{% for print in site.data.prints %}
  {% assign _thumb = print.thumb | default: print.image %}
  <div class="gallery-item">
    <div class="gallery-thumb">
      <a class="lightbox-trigger" href="{{ print.image }}" aria-label="View larger print photo">
        <img src="{{ _thumb }}" alt="{{ print.alt | default: print.title }}" loading="lazy">
      </a>
    </div>
    <p class="gallery-title">
      {% if print.url %}
        <a href="{{ print.url | relative_url }}">{{ print.title }}</a>
      {% else %}
        {{ print.title }}
      {% endif %}
    </p>
    {% if print.notes %}<p class="prints-note">{{ print.notes }}</p>{% endif %}
  </div>
{% endfor %}
</div>
{% else %}
<p>Print inventory is being updated right now — please use the form below and describe what you're looking for.</p>
{% endif %}

## How ordering works

1. Send your request through the form below (include print title(s), quantity, and shipping ZIP code).
2. Brian confirms availability and total cost (print + shipping).
3. Payment is coordinated directly (typically Venmo), then the print is packed and mailed.

## Request Prints

{% include contact-form.html
  id="prints-form"
  submit_text="Send Print Request"
  message_placeholder="Which print(s) do you want? Include quantity, shipping ZIP code, and any notes."
  success_message="Thanks! Your print request was sent. Brian will follow up with availability and shipping details." %}
