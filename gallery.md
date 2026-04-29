---
layout: page
title: Gallery
permalink: /gallery/
description: Paintings by Fernandina Beach artist Brian Barnard — acrylics and mixed media available for purchase.
nav: 2
---

Due to a busy live painting schedule, studio pieces are most often done [by commission](/commissions/).  But occasionally some will be available for sale here, displayed among the historical greatest hits!

<div class="gallery-grid">
{% for artwork in site.artworks %}
  {% assign path_parts = artwork.relative_path | split: '/' %}
  {% if path_parts.size == 2 %}
  <a href="{{ artwork.url }}" class="gallery-item">
    <div class="gallery-thumb">
      <img src="{{ artwork.image }}" alt="{{ artwork.title }}" loading="lazy">
    </div>
    <p class="gallery-title">{{ artwork.title }}</p>
    {% if artwork.price %}
      <span class="gallery-badge gallery-badge--price">{{ artwork.price }}</span>
    {% endif %}
  </a>
  {% endif %}
{% endfor %}
</div>

*Note that the most accessible way to become a member of the [Brian Barnard Art Collector's Club](https://www.facebook.com/groups/BrianBarnardArtCollectorsClub/) is to come to **[an event](/events/)**, where one or two unique 11"x17" pieces are made just about every weekend!*
