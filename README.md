# xia-geom.github.io

Personal academic website of **Xia Xiao**, PhD candidate in mathematics at [UQAM](https://uqam.ca), working on Kähler geometry, complex analysis, and geometric PDEs under the supervision of Julien Keller (UQAM) and Hugues Auvray (Université Paris-Saclay).

Live site: <https://xia-geom.github.io>

## Stack

Built with [Jekyll](https://jekyllrb.com/) and the [al-folio](https://github.com/alshedivat/al-folio) theme, hosted on GitHub Pages.

## Contents

The site is bilingual (English and French), with a 🇫🇷 / 🇬🇧 toggle in the navbar.

| Section | English | French |
| --- | --- | --- |
| About | `/` | `/fr/` |
| Research | `/research/` | `/fr/research/` |
| Teaching | `/teaching/` | `/fr/teaching/` |
| CV | `/cv/` | `/fr/cv/` |
| Projects | `/projects/` | `/fr/projects/` |
| Travel | `/travel/` | `/fr/travel/` |

Page sources live in [`_pages/`](_pages/); French counterparts are prefixed with `fr-` (e.g. [`fr-travel.md`](_pages/fr-travel.md)) and use `/fr/...` permalinks.

## Local development

Docker is the recommended setup:

```bash
docker compose pull && docker compose up
# Site at http://localhost:8080
```

Rebuild after dependency changes:

```bash
docker compose up --build
```

Stop and free port 8080:

```bash
docker compose down
```

## Pre-commit checklist

1. Format:
   ```bash
   npx prettier . --write
   ```
2. Rebuild and verify at `http://localhost:8080` — check navigation, images, dark mode, and the language toggle.

## Project conventions

- `_config.yml` — site-wide config; `url` and `baseurl` must match the deployment target.
- `_pages/` — top-level pages (about, research, teaching, cv, projects, travel) in English and French.
- `_bibliography/papers.bib` — publications, rendered via [jekyll-scholar](https://github.com/inukshuk/jekyll-scholar).
- `_includes/header.liquid` — navbar, including the language-toggle map (`lang_map_en` / `lang_map_fr`). When adding a new bilingual page, extend **both** arrays in lockstep.
- `assets/img/travel/` — travel photos referenced from [`_pages/travel.md`](_pages/travel.md) and [`_pages/fr-travel.md`](_pages/fr-travel.md).

## Further reading

- [`AGENTS.md`](AGENTS.md) — agent/contributor guide
- [`CUSTOMIZE.md`](CUSTOMIZE.md) — theming and customization
- [`INSTALL.md`](INSTALL.md) — installation and deployment
- [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) — common issues

## License

Theme distributed under the MIT License (see [`LICENSE`](LICENSE)). Site content © Xia Xiao.
