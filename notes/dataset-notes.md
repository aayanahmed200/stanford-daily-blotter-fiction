# Dataset Notes

Notes on `stanforddams/daily`, taken while preparing "Lot 95."

## Structure

The dataset ships three files:

- `index.json` — one record per article, with `id`, `title`, `author`, `url`, `date`, `categories`, and `tags`
- `train.jsonl` — the raw HTML body for each article, keyed by `id`
- `taxonomy.json` — a lookup table resolving the numeric `categories` and `tags` IDs into readable labels (for example, category 4409 is "Crime & Safety," and tags include labels like "bike theft" and "hate violence")

Each article is a weekly SUDPS bulletin summary, organized by day, listing incident type, a time window, and a campus location. Articles span September 2021 through June 2026, roughly one per week during the academic year.

## What informed the story

- **Cadence and format.** The blotter's weekly, day-by-day structure — a fixed vocabulary of incident types (petty theft, burglary from a motor vehicle, vandalism, grand theft) paired with a building or lot name — shaped both the setting and the narrator's job in the story.
- **Recurring locations.** Certain locations recur across multiple articles in the dataset: residential lots, Escondido Village, Wilbur Hall, athletic facilities near Cobb Track and Angell Field, and parking areas tied to specific dorms or departments. These are real, publicly known Stanford locations used only as backdrop.
- **The taxonomy layer.** The separation between the human-readable blotter text and the underlying `categories`/`tags` codes suggested the story's central device: a narrator who notices a pattern in the metadata that the prose itself doesn't surface.
- **No individual incident was reproduced.** No specific date, time window, or single incident's exact wording from a real article was copied into the story. The case, the coaches, and the investigation are entirely invented.
- **Lot 95 itself is not invented.** "Lot 95" (295 Galvez Street, next to the Track House) is a real address that recurs across the dataset as a location for burglary from a motor vehicle - it shows up this way at least six separate times in the 139 articles, including two same-day incidents. The story's premise (a location worth noticing because vehicle burglary keeps clustering there) is grounded in an actual pattern in the data, not an invented one layered onto a random real place. See the README's disclaimer for how this affects the fiction/reality line.

## Reproducing the exploration

`scripts/load_dataset.py` is a runnable version of the loading snippet from the dataset card.

`scripts/explore_taxonomy.py` is the actual exploration that led here: it parses every article, pulls out vehicle-burglary mentions, and counts recurring locations. Run it and Lot 95 comes out at or near the top of the list - that's the "noticing" the story dramatizes, made reproducible rather than asserted.
