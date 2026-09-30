---
layout: page
permalink: /projects/math-video/
title: Math Video Project
description: Animated mathematics lessons and videos about studying at UQAM.
nav: false
lang: en
---

[All projects]({{ '/projects/' | relative_url }})

The Math Video Project brings together mathematics teaching and UQAM programme presentations.

<section id="sample-lesson" aria-labelledby="sample-lesson-title">
  <h2 id="sample-lesson-title">Example lesson</h2>
  <h3 lang="fr">Du cercle unité à la fonction sinus</h3>
  <p id="sample-lesson-description">An animated lesson connecting the unit circle with the graph of the sine function. In French · 2 min 43 s.</p>
  <video
    controls
    preload="metadata"
    playsinline
    width="1920"
    height="1080"
    class="w-100 rounded"
    style="height: auto;"
    aria-label="Example lesson: from the unit circle to the sine function, in French"
    aria-describedby="sample-lesson-description"
  >
    <source src="{{ '/assets/video/24_du_cercle_unite_a_la_fonction_sinus.mp4' | relative_url }}" type="video/mp4">
    Your browser does not support embedded video. Use the link below to open the MP4.
  </video>
  <p><a href="{{ '/assets/video/24_du_cercle_unite_a_la_fonction_sinus.mp4' | relative_url }}">Open the video (MP4)</a></p>
</section>

## Mathematics education

Animated lessons explain concepts through examples, visual arguments and counterexamples. The curriculum covers algebra, functions, geometry, counting, vectors and matrices. A separate collection addresses common mathematical errors.

[Curriculum](https://github.com/xia-geom/math_video_project/blob/main/curriculum/programme_principal_fr.yaml) · [Common-error lessons](https://github.com/xia-geom/math_video_project/tree/main/scenes/erreurs_frequentes_fr)

## UQAM programmes and study pathways

This strand presents the mathematics bachelor’s programme, its study pathways and opportunities to combine mathematics or statistics with another discipline. It includes a longer programme overview and short recruitment and orientation videos.

[Programme overview](https://github.com/xia-geom/math_video_project/tree/main/miscellaneous/uqam-baccalaureat-mathematiques-cheminements) · [Studying mathematics at UQAM](https://github.com/xia-geom/math_video_project/tree/main/miscellaneous/bac_math_uqam_fr) · [Interdisciplinary pathways](https://github.com/xia-geom/math_video_project/tree/main/miscellaneous/bac_sciences_ouvertures_fr)

## Source code

The repository contains the scripts, animations, captions and production tools. The curriculum and programme links above lead to project sources; the example lesson can be watched directly on this page.

[GitHub repository](https://github.com/xia-geom/math_video_project)
