---
layout: page
title: Gallery
permalink: /gallery/
description: Paintings by Fernandina Beach artist Brian Barnard — acrylics and mixed media available for purchase.
nav: 2
---

Due to a busy live painting schedule, large pieces aren't being made as frequently as they were in the past.  But the plan is that any available studio works will be listed for sale here, displayed among the historical greatest hits!

**This page is skeletal while image hosting gets figured out (brianbarnardart.com launched in a preview state for Shrimp Fest 2026 — web development should resume shortly)**

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

*Brian loves seeing his art popping up in unexpected places...and wants nearly anyone to be able to afford something more than a print.  So the most accessible way to become a member of the [Brian Barnard Art Collector's Club](https://www.facebook.com/groups/BrianBarnardArtCollectorsClub/) is to [come to a live painting event](/events/).  One or two unique smaller pieces are made just about every weekend — while you watch!*
