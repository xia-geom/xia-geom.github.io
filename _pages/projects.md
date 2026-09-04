---
layout: page
title: Projects
permalink: /projects/
description: Educational mathematics video projects, including French visual explanations built with Python and Manim.
nav: true
nav_order: 4
horizontal: false
lang: en
---

Selected projects in mathematical visualization and education.

<div class="projects">
{% assign sorted_projects = site.projects | sort: "importance" %}
<div class="row row-cols-1 row-cols-md-3">
  {% for project in sorted_projects %}
    {% include projects.liquid %}
  {% endfor %}
</div>
</div>
