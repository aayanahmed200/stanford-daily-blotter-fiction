# Stanford Daily: Blotter Fiction

**Live:** [aayanahmed200.github.io/stanford-daily-blotter-fiction](https://aayanahmed200.github.io/stanford-daily-blotter-fiction/)

**Series:** [The Price of Prestige](https://aayanahmed200.github.io/stanford-daily-price-of-prestige/) · [PlasticList](https://aayanahmed200.github.io/stanford-daily-plasticlist-eda/) · [ICE pipeline](https://aayanahmed200.github.io/stanford-daily-biglocal-ice-pipeline/)

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Hugging Face](https://img.shields.io/badge/hugging%20face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/) [![GitHub Actions](https://img.shields.io/badge/github%20actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)](https://github.com/features/actions)

A short fictional story inspired by patterns in a dataset of 139 Stanford Daily police-blotter articles published between 2021 and 2026.

## Overview

Lot 95 uses the recurring categories and locations in the public dataset as a starting point for fiction, and the gap between a short written summary and the structured labels attached to it as its subject.

## How it was made

The dataset came first. `scripts/load_dataset.py` pulls the Stanford Daily police-blotter set from Hugging Face, and `scripts/explore_taxonomy.py` counts the recurring categories and locations to find the patterns worth writing around, with notes on what the set contains and how it was filtered in `notes/dataset-notes.md`.

The story itself is written in `STORY.md`, which is the canonical text. `scripts/build_site.py` turns that file into the typeset reading page in `site/`, so the prose is only ever edited in one place and the page is generated rather than hand-maintained. The page uses the shared series stylesheet, and a GitHub Actions workflow publishes `site/` on every push to `main`. A small pytest file covers the taxonomy script.

## Highlights

- Uses the difference between written summaries and structured category labels as inspiration.
- Ships the story as both Markdown and a typeset reading page, generated from a single source.
- Includes dataset notes and scripts for loading and exploring the source material.

## Repository contents

- `STORY.md` — the canonical story text; edit this, not the page.
- `site/` — the published reading page and the shared series stylesheet.
- `scripts/build_site.py` — regenerates `site/index.html` from `STORY.md`.
- `scripts/load_dataset.py`, `scripts/explore_taxonomy.py` — load the dataset and inspect its categories.
- `notes/dataset-notes.md` — what the dataset contains and how it was filtered.
- `tests/` — checks for the taxonomy script.

## Notes and limitations

Lot 95 is fiction, not a report or reconstruction of an actual case. The story is inspired by patterns in the dataset; its characters, dialogue and events are not claims about real people or incidents. The published page is generated from `STORY.md`, so it has to be rebuilt after any edit to the story.

## License

MIT — see `LICENSE`.
