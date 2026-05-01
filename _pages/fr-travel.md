---
layout: page
permalink: /fr/travel/
title: Voyages
description: Instantanés d'aventures de randonnée et de cyclisme longue distance.
nav: false
---

<style>
.travel-section {
  margin-bottom: 3rem;
}
.travel-section h2 {
  font-size: 1.35rem;
  font-weight: 600;
  border-bottom: 2px solid var(--global-theme-color, #333);
  padding-bottom: 0.4rem;
  margin-bottom: 0.5rem;
}
.travel-section .trip-meta {
  font-size: 0.88rem;
  color: #888;
  margin-bottom: 1.2rem;
}
.photo-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
  margin-bottom: 0.5rem;
}
@media (min-width: 768px) {
  .photo-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
.photo-cell {
  position: relative;
  overflow: hidden;
  border-radius: 4px;
  background: #f0f0f0;
}
.photo-cell img {
  width: 100%;
  height: 180px;
  object-fit: cover;
  display: block;
  transition: transform 0.3s ease;
  cursor: zoom-in;
}
.photo-cell img:hover {
  transform: scale(1.03);
}
.photo-caption {
  font-size: 0.78rem;
  color: #666;
  text-align: center;
  padding: 4px 4px 0;
  line-height: 1.3;
}
</style>

## Quelques histoires du passé

<div class="travel-section">
<h2>🇵🇹 Chemin de Saint-Jacques-de-Compostelle — Portugal</h2>
<p class="trip-meta">Octobre – Novembre 2021 · Voies côtière et centrale portugaises · ~600 km</p>
<div class="photo-grid">
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-portugal_01.jpg" alt="Ponte de Lima, Portugal" zoomable=true loading="lazy" %}
    <div class="photo-caption">Ponte de Lima, Portugal</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-portugal_02.jpg" alt="Viana do Castelo, Portugal" zoomable=true loading="lazy" %}
    <div class="photo-caption">Viana do Castelo, Portugal</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-portugal_03.jpg" alt="Viana do Castelo, Portugal" zoomable=true loading="lazy" %}
    <div class="photo-caption">Viana do Castelo, Portugal</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-portugal_04.jpg" alt="Barcelos, Portugal" zoomable=true loading="lazy" %}
    <div class="photo-caption">Barcelos, Portugal</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-portugal_05.jpg" alt="Ourense, Galice, Espagne" zoomable=true loading="lazy" %}
    <div class="photo-caption">Ourense, Galice</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-portugal_06.jpg" alt="Chaves, Portugal" zoomable=true loading="lazy" %}
    <div class="photo-caption">Chaves, Portugal</div>
  </div>
  {% for photo_number in (7..15) %}
    {% if photo_number < 10 %}
      {% assign photo_suffix = photo_number | prepend: '0' %}
    {% else %}
      {% assign photo_suffix = photo_number %}
    {% endif %}
    {% assign photo_path = 'assets/img/travel/camino-portugal_' | append: photo_suffix | append: '.jpg' %}
    <div class="photo-cell">
      {% include figure.liquid path=photo_path alt="Chemin portugais" zoomable=true loading="lazy" %}
      <div class="photo-caption">Chemin portugais</div>
    </div>
  {% endfor %}
</div>
</div>

---

<div class="travel-section">
<h2>🇪🇸 Chemin de Saint-Jacques-de-Compostelle — Espagne</h2>
<p class="trip-meta">Septembre – Novembre 2021 · Camino Francés · ~800 km, de Saint-Jean-Pied-de-Port à Saint-Jacques</p>
<div class="photo-grid">
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-spain_01.jpg" alt="León, Espagne" zoomable=true loading="lazy" %}
    <div class="photo-caption">León, Espagne</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-spain_02.jpg" alt="León, Espagne" zoomable=true loading="lazy" %}
    <div class="photo-caption">León, Espagne</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-spain_03.jpg" alt="León, Espagne" zoomable=true loading="lazy" %}
    <div class="photo-caption">León, Espagne</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-spain_04.jpg" alt="Zubiri, Navarre, Espagne" zoomable=true loading="lazy" %}
    <div class="photo-caption">Zubiri, Navarre</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/camino-spain_05.jpg" alt="Logroño, La Rioja, Espagne" zoomable=true loading="lazy" %}
    <div class="photo-caption">Logroño, La Rioja</div>
  </div>
  {% for photo_number in (6..8) %}
    {% assign photo_suffix = photo_number | prepend: '0' %}
    {% assign photo_path = 'assets/img/travel/camino-spain_' | append: photo_suffix | append: '.jpg' %}
    <div class="photo-cell">
      {% include figure.liquid path=photo_path alt="Camino Francés" zoomable=true loading="lazy" %}
      <div class="photo-caption">Camino Francés</div>
    </div>
  {% endfor %}
</div>
</div>

---

<div class="travel-section">
<h2>🏔️ Tour du Mont-Blanc</h2>
<p class="trip-meta">Juin 2021 · Boucle de 100 km à travers la France, l'Italie et la Suisse</p>
<div class="photo-grid">
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_01.jpg" alt="Champex-Lac, Suisse" zoomable=true loading="lazy" %}
    <div class="photo-caption">Champex-Lac, Suisse</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_02.jpg" alt="Col de Balme, France/Suisse" zoomable=true loading="lazy" %}
    <div class="photo-caption">Col de Balme</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_03.jpg" alt="Champex-Lac, Suisse" zoomable=true loading="lazy" %}
    <div class="photo-caption">Champex-Lac, Suisse</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_04.jpg" alt="Champex-Lac, Suisse" zoomable=true loading="lazy" %}
    <div class="photo-caption">Champex-Lac, Suisse</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_05.jpg" alt="Argentière, vallée de Chamonix, France" zoomable=true loading="lazy" %}
    <div class="photo-caption">Argentière, Chamonix</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_06.jpg" alt="Le Tour, vallée de Chamonix, France" zoomable=true loading="lazy" %}
    <div class="photo-caption">Le Tour, Chamonix</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_07.jpg" alt="Chamonix, France" zoomable=true loading="lazy" %}
    <div class="photo-caption">Chamonix, France</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_08.jpg" alt="Les Houches, vallée de Chamonix, France" zoomable=true loading="lazy" %}
    <div class="photo-caption">Les Houches, Chamonix</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/mont-blanc_09.jpg" alt="Tour du Mont-Blanc" zoomable=true loading="lazy" %}
    <div class="photo-caption">Tour du Mont-Blanc</div>
  </div>
</div>
</div>

---

<div class="travel-section">
<h2>🇨🇭 Traversée des cols des Alpes suisses</h2>
<p class="trip-meta">Septembre 2021 · Haute Route et Alpes vaudoises</p>
<div class="photo-grid">
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/swiss-alps_01.jpg" alt="Aigle, Vaud" zoomable=true loading="lazy" %}
    <div class="photo-caption">Aigle, Vaud</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/swiss-alps_02.jpg" alt="Château-d'Oex" zoomable=true loading="lazy" %}
    <div class="photo-caption">Château-d'Oex</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/swiss-alps_03.jpg" alt="Nyon, lac Léman" zoomable=true loading="lazy" %}
    <div class="photo-caption">Nyon, lac Léman</div>
  </div>
  {% for photo_number in (4..17) %}
    {% if photo_number < 10 %}
      {% assign photo_suffix = photo_number | prepend: '0' %}
    {% else %}
      {% assign photo_suffix = photo_number %}
    {% endif %}
    {% assign photo_path = 'assets/img/travel/swiss-alps_' | append: photo_suffix | append: '.jpg' %}
    <div class="photo-cell">
      {% include figure.liquid path=photo_path alt="Alpes suisses" zoomable=true loading="lazy" %}
      <div class="photo-caption">Alpes suisses</div>
    </div>
  {% endfor %}
</div>
</div>

---

<div class="travel-section">
<h2>🚴 Traversée du Canada à vélo</h2>
<p class="trip-meta">Août – Septembre 2023 · Montréal → Calgary · ~3 800 km</p>
<div class="photo-grid">
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_01.jpg" alt="Winnipeg, Manitoba" zoomable=true loading="lazy" %}
    <div class="photo-caption">Winnipeg, Manitoba</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_02.jpg" alt="Winnipeg, Manitoba" zoomable=true loading="lazy" %}
    <div class="photo-caption">Winnipeg, Manitoba</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_03.jpg" alt="Winnipeg, Manitoba" zoomable=true loading="lazy" %}
    <div class="photo-caption">Winnipeg, Manitoba</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_04.jpg" alt="Winnipeg, Manitoba" zoomable=true loading="lazy" %}
    <div class="photo-caption">Winnipeg, Manitoba</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_05.jpg" alt="Sault-Sainte-Marie, Ontario" zoomable=true loading="lazy" %}
    <div class="photo-caption">Sault-Sainte-Marie, Ontario</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_06.jpg" alt="Thunder Bay, Ontario" zoomable=true loading="lazy" %}
    <div class="photo-caption">Thunder Bay, Ontario</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_07.jpg" alt="Rive du lac Supérieur, Ontario" zoomable=true loading="lazy" %}
    <div class="photo-caption">Rive du lac Supérieur</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_08.jpg" alt="Calgary, Alberta" zoomable=true loading="lazy" %}
    <div class="photo-caption">Calgary, Alberta</div>
  </div>
  <div class="photo-cell">
    {% include figure.liquid path="assets/img/travel/cross-canada_09.jpg" alt="Prairies canadiennes" zoomable=true loading="lazy" %}
    <div class="photo-caption">Prairies canadiennes</div>
  </div>
</div>
</div>
