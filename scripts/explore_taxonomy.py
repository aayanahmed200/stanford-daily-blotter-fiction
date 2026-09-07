"""
Reference script for the taxonomy exploration that inspired "Lot 95."

The blotter's prose treats every incident as a one-off. This script
reproduces the actual step that surfaced the pattern: parsing each
article's HTML for location/incident mentions, then counting which
locations recur most often for a given incident type - the kind of
count that never shows up in the prose itself, only in the underlying
data.

Requires: datasets, beautifulsoup4
    pip install datasets beautifulsoup4
"""

import re
from collections import Counter

from bs4 import BeautifulSoup
from datasets import load_dataset

# Incident phrase to look for. "Burglary from a motor vehicle," "vehicle
# burglary," and "burglary of a motor vehicle" are the three phrasings the
# blotter actually uses.
INCIDENT_PATTERN = re.compile(
    r"(burglary from a motor vehicle|vehicle burglary|burglary of a motor vehicle)",
    re.IGNORECASE,
)

# Crude location extractor: blotter items are written as
# "... was reported at <location>." or "... occurred at <location>.",
# with the location sometimes followed by a parenthetical building name.
#
# The location itself can contain periods of its own - campus buildings
# and street abbreviations like "the d.school", "Rm. 214," or "Bldg. 20"
# all show up in real entries. A plain "stop at the first period" capture
# truncates those mid-word, so instead this only treats a period as the
# END of the location when it's followed by whitespace-then-a-capital
# letter (i.e. the start of a new sentence) or by the end of the string;
# a period glued directly to more text or followed by a lowercase word or
# a number is treated as part of the location, not a sentence boundary.
# The capital-letter check is deliberately case-sensitive (via the scoped
# `(?i:...)` on just the leading phrase) so it isn't defeated by the
# pattern's own case-insensitive matching of "reported at"/"occurred at".
LOCATION_PATTERN = re.compile(
    r"(?i:reported at|occurred at)\s+(.+?)(?:\.(?=\s+[A-Z]|\s*$)|$)"
)

# A qualifier that names the specific lot/building without parentheses,
# separated from the street address by an em dash or en dash instead - e.g.
# "295 Galvez Street, Lot 95 — Track House" rather than "295 Galvez Street
# (Lot 95 — Track House)". Both forms show up in the real data. This matches
# the trailing "<lot> - <building>"-style segment (no comma/parens inside
# it) so that form also groups by the lot/building name below, instead of
# falling back to the whole, address-bearing string.
DASH_QUALIFIER_PATTERN = re.compile(r"([^,()]+[–—][^,()]+)$")


def location_key(location: str) -> str:
    """Return the canonical grouping key for a raw extracted location string.

    Prefers an explicit parenthetical qualifier, e.g. "(Lot 95 - Track
    House)". Failing that, prefers a trailing em/en-dash-separated
    qualifier with no parentheses, e.g. ", Lot 95 - Track House" (the
    format used in STORY.md and seen in the real dataset). Otherwise falls
    back to the full location string, same as before.

    The street address for the same physical lot is written inconsistently
    across articles (e.g. "Galvez Street" in one week, "Galvez Court" in
    another), and the same lot/building qualifier is written with different
    dash characters across articles too (an em dash in one week, an en dash
    in another) - both are themselves small examples of why the prose alone
    under-counts a repeat location. So whichever branch above supplies the
    key, en dashes and em dashes in it are unified to a plain hyphen, so the
    same lot/building pairing groups together regardless of which dash
    character a given article happened to use.
    """
    paren_match = re.search(r"\(([^)]+)\)", location)
    if paren_match:
        key = paren_match.group(1)
    else:
        dash_match = DASH_QUALIFIER_PATTERN.search(location)
        key = dash_match.group(1) if dash_match else location
    key = re.sub(r"[–—]", "-", key)
    return key.strip().lower()


def extract_incidents(html: str):
    """Yield (location, sentence) pairs for vehicle-burglary items in one article."""
    soup = BeautifulSoup(html, "html.parser")
    for li in soup.find_all("li"):
        text = li.get_text(" ", strip=True)
        if INCIDENT_PATTERN.search(text):
            loc_match = LOCATION_PATTERN.search(text)
            location = loc_match.group(1).strip() if loc_match else "unknown"
            yield location, text


def main():
    ds = load_dataset("stanforddams/daily", "html")["train"]

    location_counts = Counter()
    examples_by_location = {}

    for row in ds:
        for location, sentence in extract_incidents(row["html"]):
            key = location_key(location)
            location_counts[key] += 1
            examples_by_location.setdefault(key, sentence)

    print("Vehicle-burglary mentions by location (top 10):\n")
    for location, count in location_counts.most_common(10):
        print(f"{count:>3}  {location}")
        print(f"      e.g. \"{examples_by_location[location]}\"\n")


if __name__ == "__main__":
    main()
