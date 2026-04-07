---
layout: page
title: Gallery
permalink: /gallery/
description: Paintings by Fernandina Beach artist Brian Barnard — acrylics and mixed media available for purchase.
---

<div class="gallery-grid">
{% for artwork in site.artworks %}
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
