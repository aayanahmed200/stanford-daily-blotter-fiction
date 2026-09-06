"""
Tests for the location-dedup key in scripts/explore_taxonomy.py.

Background: the script's dedup key preferred a parenthetical building
qualifier, e.g. "295 Galvez Street (Lot 95 - Track House)", falling back to
the *entire* location string (including the street address) otherwise. But
STORY.md's own epigraph (line 11) quotes the real blotter format WITHOUT
parentheses, using an em dash instead:

    "... reported at 295 Galvez Street, Lot 95 — Track House."

Live data pulled from the real `stanforddams/daily` dataset on Hugging Face
(via its datasets-server search API, during this investigation) confirms
this un-parenthesized, dash-separated form - and an en-dash variant of it -
both genuinely occur, alongside the parenthetical form. Before the fix,
feeding either the STORY.md sentence or a live-dataset sentence through the
old logic fell back to keying on the whole address-bearing string, so the
same recurring real-world location ("Lot 95" next to the "Track House")
would be counted as several different locations across articles whose
street-address text or dash character happened to differ - silently
breaking the dedup this script exists to do.

These tests pin down both the previously-working parenthetical case and the
newly-fixed dash-separated case, using the exact STORY.md text plus the
verbatim examples pulled from the live dataset.
"""

import importlib.util
import re
import sys
from pathlib import Path

import pytest

MODULE_PATH = Path(__file__).resolve().parent.parent / "scripts" / "explore_taxonomy.py"
_spec = importlib.util.spec_from_file_location("explore_taxonomy", MODULE_PATH)
explore_taxonomy = importlib.util.module_from_spec(_spec)
sys.modules.setdefault("explore_taxonomy", explore_taxonomy)
_spec.loader.exec_module(explore_taxonomy)

LOCATION_PATTERN = explore_taxonomy.LOCATION_PATTERN
location_key = explore_taxonomy.location_key
extract_incidents = explore_taxonomy.extract_incidents


def extract_location(sentence: str) -> str:
    m = LOCATION_PATTERN.search(sentence)
    assert m, f"LOCATION_PATTERN did not match: {sentence!r}"
    return m.group(1).strip()


# Exact text from STORY.md, line 11 (em dash, no parentheses):
STORY_SENTENCE = (
    "Burglary from a motor vehicle, between 11 a.m. and 12 p.m., reported at "
    "295 Galvez Street, Lot 95 — Track House."
)

# Same real location, different week's street-address text - per the
# script's own comment, addresses for the same lot vary across articles
# (e.g. "Galvez Street" vs "Galvez Court").
STORY_SENTENCE_OTHER_ADDRESS = (
    "Burglary from a motor vehicle, between 3 p.m. and 4 p.m., reported at "
    "295 Galvez Court, Lot 95 — Track House."
)

# The pre-existing, parenthetical format (must keep working):
PAREN_SENTENCE = (
    "Burglary from a motor vehicle, between 10 a.m. and 11 a.m., reported at "
    "295 Galvez Street (Lot 95 — Track House)."
)

# Verbatim real examples retrieved live from stanforddams/daily via the HF
# datasets-server search API for query "Lot 95" (config "html", split
# "train"), during this investigation:
REAL_PAREN_EM_DASH = (
    "Burglary from a motor vehicle between 11 a.m. and 12 p.m. on Jan. 25 "
    "was reported at 295 Galvez Street (Lot 95 — Track House)."
)
REAL_PAREN_EN_DASH = (
    "Burglary from a motor vehicle between 10:00 a.m. and 11:00 a.m. was "
    "reported at 295 Galvez Court (Lot 95 – Track House)."
)
# Real examples with no parenthetical AND no dash at all - the prose simply
# doesn't name the qualifier in an extractable way. These are a known,
# separate limitation (not what this fix targets) and are asserted here
# only to document that they still fall back to keying on the whole
# string, unchanged.
REAL_NO_QUALIFIER_1 = (
    "Second-degree burglary from a motor vehicle theft between 10:00 a.m. "
    "and 3:00 p.m. on Oct. 9 was reported at the Track House Lot 95."
)
REAL_NO_QUALIFIER_2 = (
    "Second degree burglary from a motor vehicle at 10:50 a.m. on Sept. 20 "
    "was reported at Lot 95 near the Track House."
)


def test_parenthetical_format_still_keys_on_the_qualifier():
    """Pre-existing behavior: parenthetical qualifier is preferred over the
    full address string."""
    location = extract_location(PAREN_SENTENCE)
    assert location_key(location) == "lot 95 - track house"


def test_em_dash_format_from_story_md_keys_on_the_qualifier():
    """The bug: STORY.md's exact em-dash, no-parens format must key on the
    lot/building qualifier, not the whole address-bearing string."""
    location = extract_location(STORY_SENTENCE)
    assert location_key(location) == "lot 95 - track house"


def test_em_dash_format_dedups_across_different_street_addresses():
    """The concrete symptom: two mentions of the same real location, with
    different street-address text (as happens across real articles), must
    now produce the SAME dedup key."""
    key_a = location_key(extract_location(STORY_SENTENCE))
    key_b = location_key(extract_location(STORY_SENTENCE_OTHER_ADDRESS))
    assert key_a == key_b == "lot 95 - track house"


def test_parenthetical_and_dash_formats_agree_on_the_same_location():
    """A parenthetical mention and a dash-separated mention of the same
    location should key identically, so the two forms merge rather than
    being counted as different locations."""
    paren_key = location_key(extract_location(PAREN_SENTENCE))
    dash_key = location_key(extract_location(STORY_SENTENCE))
    assert paren_key == dash_key


@pytest.mark.parametrize(
    "sentence",
    [REAL_PAREN_EM_DASH, REAL_PAREN_EN_DASH],
    ids=["real-paren-em-dash", "real-paren-en-dash"],
)
def test_real_dataset_examples_key_identically_regardless_of_dash_character(sentence):
    """Live data (fetched from stanforddams/daily on Hugging Face during
    this investigation) shows the SAME real location written with an em
    dash in one article and an en dash in another, both inside parens. Both
    must collapse to the same key, or the recurrence is undercounted."""
    assert location_key(extract_location(sentence)) == "lot 95 - track house"


def test_no_qualifier_present_falls_back_to_whole_string_unchanged():
    """Known, separate limitation (not in scope for this fix): when an
    article names the lot with neither parens nor a dash (e.g. "the Track
    House Lot 95", or "Lot 95 near the Track House"), there's no
    extractable qualifier substring, so the key is still the whole
    location string, same as before this fix. Documented here so a future
    change to this fallback is a deliberate choice, not a silent one."""
    key_1 = location_key(extract_location(REAL_NO_QUALIFIER_1))
    key_2 = location_key(extract_location(REAL_NO_QUALIFIER_2))
    assert key_1 == "the track house lot 95"
    assert key_2 == "lot 95 near the track house"
    # Confirms these two still do NOT merge with each other or with the
    # qualifier-bearing forms above - an existing, pre-fix limitation.
    assert key_1 != key_2
    assert key_1 != "lot 95 - track house"
    assert key_2 != "lot 95 - track house"


def test_end_to_end_through_extract_incidents_with_story_md_html():
    """Full pipeline check: wrap the exact STORY.md sentence in the same
    <li> shape real blotter HTML uses, and confirm extract_incidents ->
    location_key produces the deduped key end to end."""
    html = f"<ul><li>{STORY_SENTENCE}</li><li>{STORY_SENTENCE_OTHER_ADDRESS}</li></ul>"
    results = list(extract_incidents(html))
    assert len(results) == 2
    keys = {location_key(location) for location, _sentence in results}
    assert keys == {"lot 95 - track house"}


def test_dash_qualifier_pattern_does_not_fire_on_bare_hyphen():
    """The em/en-dash fallback should not be tripped by an ordinary ASCII
    hyphen (e.g. a hyphenated address range), to avoid over-eagerly
    reinterpreting unrelated text as a lot/building qualifier."""
    assert explore_taxonomy.DASH_QUALIFIER_PATTERN.search("123-125 Main Street") is None
