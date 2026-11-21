# Lot 95 — Stanford Daily Blotter Fiction

A fictional short story shaped by recurring patterns in Stanford Daily public-safety blotter data.

**[Read the story](STORY.md)**

## Overview

"Lot 95" follows a student journalist who notices a recurring location pattern while working with the paper's weekly police-blotter summaries. The story was inspired by an exploration of 139 Stanford Daily blotter articles published between 2021 and 2026.

The repository includes the story and small scripts that load the public dataset and explore recurring incident and location terms.

## Repository contents

- `STORY.md` — the fictional story.
- `notes/dataset-notes.md` — source-dataset structure and the analysis that informed the story.
- `scripts/load_dataset.py` — loads the `stanforddams/daily` dataset and extracts article text from HTML.
- `scripts/explore_taxonomy.py` — counts recurring locations associated with vehicle-burglary wording.
- `tests/` — tests for the taxonomy exploration.

## Technology

Python, Hugging Face `datasets`, Beautiful Soup and pytest. The scripts load the dataset from Hugging Face, so running the exploration requires an internet connection.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install datasets beautifulsoup4 pytest
python scripts/load_dataset.py
python scripts/explore_taxonomy.py
pytest tests/
```

## Scope and limitations

The story is fiction, not a reconstruction of an actual case. The Lot 95 location itself is real and appears in the source dataset; the characters, coaches, sequence of events and investigation in the story are invented. The analysis is based on the dataset snapshot described in the notes, and the remote dataset may change over time. No individual in the story is intended to represent a real person.

## License

MIT. See [LICENSE](LICENSE).
