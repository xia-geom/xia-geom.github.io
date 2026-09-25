# Xia Xiao — academic website

Personal academic website, built with Jekyll and the al-folio theme.

## Public content

English and French pages cover research, teaching, projects, the CV and travel.
The two project pages present mathematics/UQAM videos and Conversation Archive.

## Editing

Page sources are in `_pages/`. French pages use `/fr/` permalinks.
The header and language metadata find matching pages automatically; there is no
separate language-toggle map to update.

The CV views read `_data/cv.yml` and `_data/cv_fr.yml` without duplicating records.
`_layouts/academic-cv.liquid` renders both languages. Research pages use
`_layouts/academic-bib.liquid`, with native Abstract and BibTeX disclosures.

## Local checks

Use the Docker setup described in [AGENTS.md](AGENTS.md) to build the site.
After building, prepare and check the same output that will be published:

```sh
python3 -m unittest discover -s bin -p 'test_public_site.py' -v
python3 bin/check_public_site.py _site --prepare --report site-validation.json
```

Run `npm ci --ignore-scripts` and `npx prettier . --check` for formatting.
The validator performs local checks only; it does not test external services,
video playback or full accessibility conformance.

## Publication

The deployment workflow builds the site, removes non-public output, validates
local links and specific regressions, and saves the result as `site-preview`.
Only the main/master deployment job has repository write permission. It publishes
that exact artifact rather than rebuilding it. A `.nojekyll` marker prevents a
second Pages processing pass. The follow-up workflow rechecks the saved artifact.

Repository guides stay in Git but are removed from the public build. Personal
conversation archives are not published.

## License

The theme is distributed under the [MIT License](LICENSE). Site content © Xia Xiao.
