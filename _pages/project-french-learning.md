---
layout: page
permalink: /projects/french-learning/
title: Le français qui vit
description: French for everyday life, stories and research, with grammar beside use and documented word-frequency counts.
nav: false
lang: en
---

[All projects]({{ '/projects/' | relative_url }})

## Everyday life, stories and research

A café, an unexpected parcel, a conversation with a neighbour, a research meeting:
learning French should prepare us for all of them. *Le français qui vit* is a
French-learning book developed around situations, connected stories and reusable
language, with English explanations and selected Québec usage notes.

The aim is to respond to a situation in French, rather than first compose an
English sentence and translate it. Phrases are a useful starting point, not the
whole method.

## Read a story. Notice a pattern. Use it.

The revised edition includes **24 connected fictional episodes**, with everyday
misunderstandings, recurring characters and a red umbrella that keeps returning.
Each episode leads into a language workshop and a practical task: answer a message,
retell an incident, ask for help or change the ending.

Everyday situations include cafés and shopping, neighbours and housing, transport,
invitations, appointments, cooking, travel and friendship. University situations
remain part of the book: working with colleagues, discussing mathematics, teaching,
writing emails, presenting research and giving feedback.

Grammar is explained beside the examples and revisited in **24 grammar clinics**.
The book also retains **240 academic and professional expression families**, with
writing models, exercises, answer keys and a review system.

## Frequency is evidence, not a difficulty score

A separate reference reproduces published counts and source ranks for **500 French
word forms** from a historical subtitle-derived list. There are **no difficulty
ratings or weighted usefulness scores**.

A word form, a lemma and a whole expression are different counting units. The book
does **not** claim that its phrases are empirically frequency-ranked. Subtitle
counts are not a survey of present-day Québec conversation, and source-processing
limitations are documented.

[Inspect the pinned frequency source](https://github.com/hermitdave/FrequencyWords/blob/8863f1a993b7b3f1bb3beed50b95525820c3171a/content/2018/fr/fr_50k.txt)

## Current edition

**Revised September 2026.** The edition consists of a PDF, self-contained editable
LaTeX source and a frequency-evidence file.

{% assign book_pdf = site.static_files | where: 'path', '/assets/books/le-francais-qui-vit/le_francais_qui_vit.pdf' | first %}
{% assign book_tex = site.static_files | where: 'path', '/assets/books/le-francais-qui-vit/le_francais_qui_vit.tex' | first %}
{% assign book_data = site.static_files | where: 'path', '/assets/books/le-francais-qui-vit/frequency_evidence.json' | first %}
{% if book_pdf %}
[Read the PDF]({{ book_pdf.path | relative_url }})
{% endif %}
{% if book_tex %}
[Download the LaTeX source]({{ book_tex.path | relative_url }})
{% endif %}
{% if book_data %}
[Inspect the frequency evidence]({{ book_data.path | relative_url }})
{% endif %}
{% unless book_pdf %}
The book files are not yet hosted on this website.
[Contact me about the current edition]({{ '/' | relative_url }}).
{% endunless %}
