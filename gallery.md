---
layout: page
title: Gallery
permalink: /gallery/
description: Paintings by Fernandina Beach artist Brian Barnard — acrylics and mixed media available for purchase.
nav: 2
---

Due to a busy live painting schedule *(and the risk of spending weeks on an idea no one has put up money for)*, large pieces are [most often done by commission](/commissions/).  But the plan is that any available studio works will be listed for sale here, displayed among the historical greatest hits!

**This new page is skeletal while image hosting gets figured out.  Come see Brian's [Shrimp Fest 2026 booth](https://brianbarnardart.com/events/) (May 2nd & 3rd)  Website development will resume once things die down a bit...**

<div class="gallery-grid">
{% assign ordered_works = "" | split: "" %}
{% assign unordered_works = "" | split: "" %}
{% for artwork in site.works %}
  {% assign path_parts = artwork.relative_path | split: '/' %}
  {% if path_parts.size == 2 %}
    {% if artwork.order %}
      {% assign ordered_works = ordered_works | push: artwork %}
    {% else %}
      {% assign unordered_works = unordered_works | push: artwork %}
    {% endif %}
  {% endif %}
{% endfor %}
{% assign ordered_works = ordered_works | sort: "order" %}
{% assign all_works = ordered_works | concat: unordered_works %}
{% for artwork in all_works %}
  <a href="{{ artwork.url }}" class="gallery-item">
    <div class="gallery-thumb">
      <img src="{{ artwork.image }}" alt="{{ artwork.title }}" loading="lazy">
    </div>
    <p class="gallery-title">{{ artwork.title }}</p>
    {% if artwork.price %}
      <span class="gallery-badge gallery-badge--price">{{ artwork.price }}</span>
    {% endif %}
  </a>
{% endfor %}
</div>

*Note that the most accessible way to become a member of the [Brian Barnard Art Collector's Club](https://www.facebook.com/groups/BrianBarnardArtCollectorsClub/) is to [come to a live painting event](/events/), where one or two unique smaller pieces are made just about every weekend!*
