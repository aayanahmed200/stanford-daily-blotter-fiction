# Stanford Daily: Blotter Fiction

**Live:** [aayanahmed200.github.io/stanford-daily-blotter-fiction](https://aayanahmed200.github.io/stanford-daily-blotter-fiction/)

**Series:** [The Price of Prestige](https://aayanahmed200.github.io/stanford-daily-price-of-prestige/) · [PlasticList](https://aayanahmed200.github.io/stanford-daily-plasticlist-eda/) · [ICE pipeline](https://aayanahmed200.github.io/stanford-daily-biglocal-ice-pipeline/)

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Hugging Face](https://img.shields.io/badge/hugging%20face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)

A short fictional story inspired by patterns in a dataset of 139 Stanford Daily police-blotter articles published between 2021 and 2026.

## Overview

Lot 95 uses the recurring categories and locations in the public dataset as a starting point for fiction, and the gap between a short written summary and the structured labels attached to it as its subject.

## Highlights

- Uses the difference between written summaries and structured category labels as inspiration.
- Ships the story as both Markdown and a typeset reading page, generated from a single source.
- Includes dataset notes and scripts for loading and exploring the source material.

## Repository contents

- `STORY.md` - the canonical story text; edit this, not the page.
- `site/` - the published reading page and the shared series stylesheet.
- `scripts/build_site.py` - regenerates `site/index.html` from `STORY.md`.
- `scripts/load_dataset.py`, `scripts/explore_taxonomy.py` - load the dataset and inspect its categories.
- `notes/dataset-notes.md` - what the dataset contains and how it was filtered.
- `tests/` - checks for the taxonomy script.

## Run locally

```bash
pip install datasets beautifulsoup4
python scripts/load_dataset.py
python scripts/explore_taxonomy.py
python scripts/build_site.py
```

Run tests with:

```bash
pip install pytest
pytest tests/
```

## Notes and limitations

Lot 95 is fiction, not a report or reconstruction of an actual case. The story is inspired by patterns in the dataset; its characters, dialogue and events are not claims about real people or incidents. The published page is generated from `STORY.md`, so re-run `scripts/build_site.py` after any edit.

## License

MIT - see `LICENSE`.
