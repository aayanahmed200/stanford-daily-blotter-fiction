# Lot 95 — Stanford Daily Blotter Fiction

> A work of fiction inspired by recurring categories and locations in 139 Stanford Daily police-blotter articles published between 2021 and 2026.

**Live story:** [aayanahmed200.github.io/stanford-daily-blotter-fiction](https://aayanahmed200.github.io/stanford-daily-blotter-fiction/)

**Stanford Daily series:** [The Price of Prestige](https://aayanahmed200.github.io/stanford-daily-price-of-prestige/) · [PlasticList EDA](https://aayanahmed200.github.io/stanford-daily-plasticlist-eda/) · [ICE Extraction Pipeline](https://aayanahmed200.github.io/stanford-daily-biglocal-ice-pipeline/)

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Hugging Face](https://img.shields.io/badge/hugging%20face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/) [![GitHub Actions](https://img.shields.io/badge/github%20actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

## Overview

`Lot 95` is a short fictional story that uses patterns in a public Stanford Daily police-blotter dataset as a creative starting point. It draws on recurring categories and locations, and on the gap between a brief written summary and the structured labels attached to it.

The dataset exploration informs the setting and themes; it is not used to reconstruct an actual incident.

## What the repository includes

- The canonical story text in Markdown.
- A generated, typeset reading page published on GitHub Pages.
- Scripts for loading the source dataset and exploring recurring categories and locations.
- Dataset notes explaining what the source contains and how it was filtered.
- A small test suite for the taxonomy exploration code.

## Implementation

The source dataset is loaded from Hugging Face by `scripts/load_dataset.py`. `scripts/explore_taxonomy.py` counts recurring categories and locations. The story itself lives in `STORY.md`; `scripts/build_site.py` generates `site/index.html` from that source so the published page and story text do not need to be edited separately.

The site uses the shared stylesheet from the Stanford Daily data-journalism series. GitHub Actions publishes the contents of `site/` to GitHub Pages on pushes to `main`.

## Repository structure

- `STORY.md` — canonical story text; edit this file rather than the generated page.
- `scripts/build_site.py` — generates the published HTML page from `STORY.md`.
- `scripts/load_dataset.py` and `scripts/explore_taxonomy.py` — load and inspect the source dataset.
- `notes/dataset-notes.md` — source and filtering notes.
- `site/` — generated reading page and shared series stylesheet.
- `tests/` — tests for the taxonomy script.
- `.github/workflows/pages.yml` — GitHub Pages publishing workflow.

## Run locally

Regenerate the reading page after editing `STORY.md`:

```bash
python scripts/build_site.py
```

Then open `site/index.html` in a browser or serve the `site/` directory with a local static web server. The build script uses Python's standard library.

## Status and limitations

This repository contains fiction, not reporting, a case reconstruction, or claims about real people or incidents. Its characters, dialogue, and events are invented. The story is inspired by aggregate patterns in the dataset; no event described in it should be read as a factual account.

## License

MIT. See [LICENSE](LICENSE).
