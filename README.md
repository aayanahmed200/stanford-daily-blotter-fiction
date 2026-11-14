# Stanford Daily: Blotter Fiction

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/) [![Hugging Face](https://img.shields.io/badge/hugging%20face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)

A short fictional story inspired by patterns in a dataset of 139 Stanford Daily police-blotter articles published between 2021 and 2026.

**[Read the story](STORY.md)**

## Overview

Lot 95 uses recurring categories and locations in the public dataset as a starting point for fiction.

## Highlights

- Uses the difference between written summaries and structured category labels as inspiration.
- Includes dataset notes and scripts for loading and exploring the source material.

## Technology

Python, Hugging Face `datasets`, and Beautiful Soup.

## Run locally

```bash
pip install datasets beautifulsoup4
python scripts/load_dataset.py
python scripts/explore_taxonomy.py
```

Run tests with:

```bash
pip install pytest
pytest tests/
```

## Notes and limitations

Lot 95 is fiction, not a report or reconstruction of an actual case. The story is inspired by patterns in the dataset; its characters and events are not claims about real people or incidents.

## License

MIT — see `LICENSE`.