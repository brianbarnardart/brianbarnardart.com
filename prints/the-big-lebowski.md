---
layout: page
title: The Big Lebowski Prints
permalink: /prints/the-big-lebowski/
description: Order Brian Barnard's The Big Lebowski inspired prints through a personal request process.
image: /assets/prints/dude-in-grocery-store-fake.jpg
---

# The Big Lebowski Prints

If The Dude is your vibe, you're in the right place.

This page is for print requests tied to Brian's **The Big Lebowski** series.
For all other work, see **[all print offerings](/prints/)**.

## Current Offerings (PROTOTYPE!)

{% if site.data.lebowski_prints and site.data.lebowski_prints.size > 0 %}
<div class="gallery-grid">
{% for print in site.data.lebowski_prints %}
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
<p>Lebowski print inventory is being updated right now — please use the form below and describe what you're looking for.</p>
{% endif %}

*(The idea is that Brian would have his hand in photographs holding prints in
front of one of his murals, but it is being prototyped here with AI grafting
JPGs of photos of his prints onto a blank piece of paper held in front of one
of his paintings.)*

## How ordering works

1. Send a request below with the print title(s), quantity, and shipping ZIP code.
2. Brian confirms availability and total (print + shipping).
3. Payment is coordinated directly (usually Venmo), then shipped.

## Request Lebowski Prints

{% include contact-form.html
  id="lebowski-prints-form"
  submit_text="Send Lebowski Print Request"
  message_placeholder="Which Lebowski print(s) are you interested in? Include quantity and shipping ZIP code."
  success_message="Thanks! Your Lebowski print request was sent. Brian will follow up with availability and shipping details." %}
