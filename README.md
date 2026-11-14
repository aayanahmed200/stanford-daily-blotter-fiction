# Stanford Daily: Blotter Fiction

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Hugging Face](https://img.shields.io/badge/hugging%20face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)

A short fictional story inspired by patterns in a dataset of 139 Stanford Daily police-blotter articles published between 2021 and 2026.

**Full story:** [`STORY.md`](STORY.md)

## Overview

Lot 95 uses the repetitive categories and locations in the public dataset as a starting point for fiction. It is a story, not a report or a reconstruction of an actual case.

## Fiction disclaimer

Characters, the investigation, and the events in the story are invented. The recurring vehicle-burglary pattern associated with Lot 95 is present in the source dataset; the story built around that pattern is fictional. Other campus locations are used as setting, not as claims about real incidents.

## Data and approach

The source dataset contains article metadata, raw HTML, and category/tag taxonomies. The project uses the differences between the written summaries and their structured labels as inspiration. The story does not copy a specific incident, date, or case.

## Technology

Python, Hugging Face `datasets`, and Beautiful Soup for loading and examining the source material.

## Run locally

```bash
pip install datasets beautifulsoup4
python scripts/load_dataset.py
python scripts/explore_taxonomy.py
```

Run the tests with `pip install pytest` followed by `pytest tests/`.

## Project files

- `STORY.md` — the short story, Lot 95.
- `notes/dataset-notes.md` — dataset structure and research notes.
- `scripts/` — dataset loading and taxonomy exploration.
- `tests/` — location-deduplication tests.
- `assets/campus-map.svg` — schematic of recurring dataset locations.

## Contributors

- [@timofeywheat-wq](https://github.com/timofeywheat-wq)

## License

MIT — see `LICENSE`. The underlying dataset is available as [`stanforddams/daily`](https://huggingface.co/datasets/stanforddams/daily) and remains subject to its own terms.
