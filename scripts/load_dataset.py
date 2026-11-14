"""
Reference script for loading and exploring stanforddams/daily.

Requires: datasets, beautifulsoup4
    pip install datasets beautifulsoup4
"""

from datasets import load_dataset
from bs4 import BeautifulSoup


def collect(example):
    soup = BeautifulSoup(example["html"], "html.parser")
    example["text"] = soup.get_text(" ", strip=True)
    example["title"] = soup.title.string if soup.title else None
    return example


def main():
    ds = load_dataset("stanforddams/daily", "html")
    ds = ds.map(collect)

    print(f"Rows: {len(ds['train'])}")
    print(ds["train"][0]["title"])
    print(ds["train"][0]["text"][:500])


if __name__ == "__main__":
    main()
