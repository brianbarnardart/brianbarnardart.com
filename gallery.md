---
layout: page
title: Gallery
permalink: /gallery/
description: Paintings by Fernandina Beach artist Brian Barnard — acrylics and mixed media available for purchase.
nav: 2
---

The most accessible way to become a member of the [Brian Barnard Art Collector's Club](https://www.facebook.com/groups/BrianBarnardArtCollectorsClub/) is to come to a **[live painting event](/events/)**, where one or two unique 11x17 pieces are made every weekend!  Larger studio pieces are most often done by commission, but occasionally some will be available for sale here.

*This page is under construction.  Waterfront Jamboree is sold, so it's not actually for sale for a million dollars...though the owner might be willing to part with it if you offer that! 😁  This is just a test of how pieces that are for sale will work when they are added!*

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
