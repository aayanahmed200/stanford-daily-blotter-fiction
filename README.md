# Stanford Daily: Blotter Fiction

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Hugging Face](https://img.shields.io/badge/hugging%20face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)

A short fictional story inspired by patterns in a dataset of 139 Stanford Daily police-blotter articles published between 2021 and 2026.

**Full story:** [`STORY.md`](STORY.md)

## Overview

Lot 95 uses recurring categories and locations in the public dataset as a starting point for fiction. It is a story, not a report or a reconstruction of an actual case.

## Highlights

- Uses the difference between written summaries and structured category labels as inspiration.
- Keeps the fictional events separate from the source reporting.
- Includes dataset notes and scripts for loading and exploring the source material.

## Technology

Python, Hugging Face `datasets`, and Beautiful Soup.

## Run locally

```bash
pip install datasets beautifulsoup4
python scripts/load_dataset.py
python scripts/explore_taxonomy.py
```

Run tests with `pip install pytest` followed by `pytest tests/`.

## Notes and limitations

Characters, the investigation, and the events in the story are invented. The recurring vehicle-burglary pattern associated with Lot 95 appears in the source dataset; the story built around it is fictional. Other campus locations provide setting, not claims about real incidents. The source dataset is available as [`stanforddams/daily`](https://huggingface.co/datasets/stanforddams/daily) and remains subject to its own terms.

## Contributors

- [@timofeywheat-wq](https://github.com/timofeywheat-wq)

## License

MIT — see `LICENSE`.
