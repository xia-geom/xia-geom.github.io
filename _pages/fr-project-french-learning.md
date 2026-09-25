---
layout: page
permalink: /fr/projects/french-learning/
title: Le français qui vit
description: Le français de la vie quotidienne et de la recherche, avec grammaire en contexte et comptages de fréquence documentés.
nav: false
lang: fr
---

[Tous les projets]({{ '/fr/projects/' | relative_url }})

## Vie quotidienne, récits et recherche

Un café, un colis inattendu, une conversation avec un voisin, une réunion de
recherche : apprendre le français doit préparer à toutes ces situations.
_Le français qui vit_ est un livre d’apprentissage construit autour de situations,
de récits suivis et de formulations réutilisables, avec des explications en anglais
et des notes sur certains usages québécois.

L’objectif est de réagir à une situation en français, plutôt que de composer une
phrase en anglais avant de la traduire. Les expressions constituent un point de
départ utile, mais pas toute la méthode.

## Lire un récit. Repérer une construction. La réutiliser.

L’édition révisée comprend **24 épisodes de fiction reliés entre eux**, avec de
petits malentendus, des personnages récurrents et un parapluie rouge qui réapparaît.
Chaque épisode débouche sur un atelier de langue et une tâche concrète : répondre
à un message, raconter un incident, demander de l’aide ou imaginer une autre fin.

Les situations couvrent les cafés et les achats, le voisinage et le logement,
les transports, les invitations, les rendez-vous, la cuisine, les voyages et
l’amitié. La vie universitaire reste présente : échanges avec les collègues,
discussions mathématiques, enseignement, courriels, exposés et commentaires sur
un texte.

La grammaire est expliquée à côté des exemples et approfondie dans **24 ateliers
grammaticaux**. Le livre conserve aussi **240 familles d’expressions universitaires
et professionnelles**, avec des modèles de textes, des exercices, des corrigés et
un dispositif de révision.

## La fréquence comme donnée, pas comme note de difficulté

Un répertoire distinct reproduit les comptages et rangs publiés de **500 formes
graphiques françaises**, issus d’une liste historique fondée sur des sous-titres.
Il n’y a **ni notes de difficulté ni scores pondérés d’utilité**.

Une forme graphique, un lemme et une expression entière ne sont pas la même unité
de comptage. Le livre ne prétend **pas** classer ses expressions selon une fréquence
mesurée. Les sous-titres ne constituent pas une enquête sur les conversations
québécoises actuelles, et les limites du traitement des sources sont indiquées.

[Consulter la version précise de la source](https://github.com/hermitdave/FrequencyWords/blob/8863f1a993b7b3f1bb3beed50b95525820c3171a/content/2018/fr/fr_50k.txt)

## Édition actuelle

**Révision de septembre 2026.** L’édition comprend un PDF, un fichier LaTeX autonome
et modifiable, ainsi qu’un fichier documentant les données de fréquence.

{% assign book_pdf = site.static_files | where: 'path', '/assets/books/le-francais-qui-vit/le_francais_qui_vit.pdf' | first %}
{% assign book_tex = site.static_files | where: 'path', '/assets/books/le-francais-qui-vit/le_francais_qui_vit.tex' | first %}
{% assign book_data = site.static_files | where: 'path', '/assets/books/le-francais-qui-vit/frequency_evidence.json' | first %}
{% if book_pdf %}
[Lire le PDF]({{ book_pdf.path | relative_url }})
{% endif %}
{% if book_tex %}
[Télécharger le fichier LaTeX]({{ book_tex.path | relative_url }})
{% endif %}
{% if book_data %}
[Consulter les données de fréquence]({{ book_data.path | relative_url }})
{% endif %}
{% unless book_pdf %}
Les fichiers du livre ne sont pas encore hébergés sur ce site.
[Me contacter au sujet de l’édition actuelle]({{ '/fr/' | relative_url }}).
{% endunless %}
