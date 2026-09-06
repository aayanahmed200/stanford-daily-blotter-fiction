# Stanford Daily: Blotter Fiction

[![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Hugging Face](https://img.shields.io/badge/hugging%20face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)](https://huggingface.co/)

A short story of crime at Stanford, written from [`stanforddams/daily`](https://huggingface.co/datasets/stanforddams/daily), a dataset of 139 police blotter articles published by the Stanford Daily between 2021 and 2026. The dataset covers weekly incident summaries reported to the Stanford University Department of Public Safety (SUDPS), across campus residences, academic buildings, and parking lots.

Full story: [`STORY.md`](STORY.md)

## Before you read: this is fiction

**"Lot 95" is a short story, not a piece of reporting.** No character, event, arrest, or investigation in it corresponds to any actual incident, person, or case on record. Any resemblance to real individuals is coincidental.

One important caveat on top of the usual disclaimer: the story's setting — repeat vehicle burglaries clustering at a lot called "Lot 95" (295 Galvez Street, next to the Track House) — is not purely invented background. It's a real, recurring pattern in the dataset: burglary from a motor vehicle is reported at that exact real address multiple times across the 139 articles, including two same-day incidents. The *character* (Priya), the *investigation*, the *coaches-at-a-meet* explanation, and the *arrest* are all invented. The *fact that Lot 95 sees repeat vehicle burglaries* is not — it's what's actually in the public record. If you're familiar with the Daily's blotter, don't read this as a dramatization of a real case; the specific story built on top of that real pattern is fiction.

## Why this exists

The Daily's blotter turns campus crime into a fixed, repetitive vocabulary - bike theft, vehicle burglary, petty theft from a building - tagged day by day, location by location, week after week. Reading enough of it in one sitting, the pattern of the format starts to feel like a story on its own: a narrator who only ever sees crime through categories and codes, and has to notice what the categories miss. "Lot 95" is that idea worked into fiction rather than an EDA writeup. The characters and case are invented; the campus geography is real.

## The data

The dataset ships three files: `index.json` for per-article metadata (title, author, url, date, category and tag IDs), `train.jsonl` for the raw HTML body of each article, and `taxonomy.json`, which resolves the numeric category and tag IDs into labels like "bike theft" or "hate violence." The article HTML needs to be parsed (BeautifulSoup, per the dataset card) before the actual blotter text is usable - most of each page is site navigation and footer links.

One quirk that shaped the story: the human-readable blotter text and the underlying category/tag codes are separate layers. A location or incident type can repeat across the numeric metadata in a way the prose doesn't call attention to. That gap - between what the blotter says and what the taxonomy shows if you go looking - is the device the story is built around.

No article's specific incidents, dates, or content were copied into the story - no invented incident reuses a real one's date, time window, or exact detail. But this is a narrower claim than "used only as setting": Escondido Village, Wilbur Hall, and Cobb Track are backdrop, invented case aside. Lot 95 is different - it's a real, recurring vehicle-burglary location in the dataset, and the story's central pattern (repeat burglaries clustering there) reflects that real recurrence rather than inventing it from scratch. See the disclaimer above for the distinction between what's real and what's invented at Lot 95 specifically.

### Dataset at a glance

- **Articles:** 139 police blotter posts
- **Time period:** September 2021 - June 2026, roughly one per week during the academic year
- **Recurring locations:** residential lots (including Lot 95), Escondido Village, Wilbur Hall, and athletic facilities around Cobb Track and Angell Field, alongside scattered department and dorm parking areas
- **Incident types:** a fixed taxonomy of categories and tags - petty theft, bike theft, burglary from a motor vehicle, vandalism, grand theft, and hate violence among them - resolved from `taxonomy.json`

## Campus map

The places that recur across the dataset, and that anchor the story's setting:

<img src="assets/campus-map.svg" alt="Schematic map of recurring dataset locations: Lot 95, Wilbur Hall, Escondido Village, Cobb Track / Angell Field, and department/dorm parking" width="700">

This is a schematic for orientation, not a to-scale campus map - it exists to show how often the same handful of places recur in the blotter, not to map incidents precisely.

## Tech stack

Python · [`datasets`](https://pypi.org/project/datasets/) (Hugging Face, dataset loading) ·
`beautifulsoup4` (HTML parsing)

## Project structure

- `STORY.md` - the short story, "Lot 95"
- `notes/dataset-notes.md` - what from the dataset's structure and geography informed the story
- `scripts/load_dataset.py` - reference script for loading and parsing the dataset
- `scripts/explore_taxonomy.py` - reference script reproducing the location-frequency exploration that inspired the story
- `tests/test_explore_taxonomy.py` - tests for the location-dedup logic in `scripts/explore_taxonomy.py`
- `assets/campus-map.svg` - schematic map of the dataset's recurring locations
- `LICENSE`

## Setup

```bash
pip install datasets beautifulsoup4
python scripts/load_dataset.py
python scripts/explore_taxonomy.py
```

To run the tests for the location-dedup logic (no network access required):

```bash
pip install pytest
pytest tests/
```

## Limitations

See [Before you read: this is fiction](#before-you-read-this-is-fiction) above - same disclaimer, including the note on Lot 95 specifically.

## Contributors

- [@timofeywheat-wq](https://github.com/timofeywheat-wq)

## License

MIT — see [LICENSE](LICENSE). The underlying dataset is
[`stanforddams/daily`](https://huggingface.co/datasets/stanforddams/daily) on
Hugging Face; see its own license/terms for reuse of the raw data.
