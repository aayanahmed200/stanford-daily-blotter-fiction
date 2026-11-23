"""Build the published story page from STORY.md.

    python scripts/build_site.py

STORY.md is the canonical text. The site page is generated from it so the two cannot
drift; re-run this after editing the story.
"""
import html
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parents[1]
SOURCE = ROOT / "STORY.md"
OUTPUT = ROOT / "site" / "index.html"

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700'
    '&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap"'
    ' rel="stylesheet">\n'
)

NAV = """      <a href="https://aayanahmed200.github.io/stanford-daily-price-of-prestige/">The Price of Prestige</a>
      <a href="https://aayanahmed200.github.io/stanford-daily-plasticlist-eda/">PlasticList</a>
      <a href="./" aria-current="page">Blotter fiction</a>
      <a href="https://aayanahmed200.github.io/stanford-daily-biglocal-ice-pipeline/">ICE pipeline</a>"""

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Lot 95 — a short story from the Stanford Daily blotter — Stanford Daily</title>
<meta name="description" content="A short story built from recurring categories and locations in a dataset of 139 Stanford Daily police-blotter articles.">
<link rel="canonical" href="https://aayanahmed200.github.io/stanford-daily-blotter-fiction/">
<meta property="og:type" content="article">
<meta property="og:title" content="Lot 95">
<meta property="og:description" content="A short story built from patterns in 139 Stanford Daily police-blotter articles.">
<meta property="og:url" content="https://aayanahmed200.github.io/stanford-daily-blotter-fiction/">
<meta name="twitter:card" content="summary_large_image">
{fonts}<link rel="stylesheet" href="series.css">
</head>
<body>

<header class="masthead">
  <div class="wrap masthead__inner">
    <a class="masthead__series" href="https://github.com/aayanahmed200">Stanford Daily · Data</a>
    <nav class="masthead__nav" aria-label="Series">
{nav}
    </nav>
  </div>
</header>

<main class="wrap report">
  <p class="kicker">Fiction from data</p>
  <h1>Lot 95</h1>
  <p class="standfirst">A short story built from recurring categories and locations in 139 Stanford Daily police-blotter articles.</p>
  <p class="byline">Aayan Ahmed · Fiction · 2026</p>

  <article class="prose">
{story}
  </article>

  <div class="aside">
    <p><strong>What this is built from.</strong> The story draws on a dataset of 139 Stanford Daily police-blotter articles published between 2021 and 2026: the categories the paper files each item under, the locations that recur, and the gap between a short written summary and the structured labels attached to it. The dataset notes and the taxonomy scripts live in the repository.</p>
    <p>Lot 95 is fiction, not a report or a reconstruction of a case. Its characters, dialogue and central case are invented; no event, arrest or investigation described here corresponds to an incident on record.</p>
  </div>

  <div class="actions">
    <a class="button" href="https://github.com/aayanahmed200/stanford-daily-blotter-fiction">Story source and notes</a>
    <a class="button button--ghost" href="https://aayanahmed200.github.io/stanford-daily-plasticlist-eda/">Next: PlasticList analysis</a>
  </div>
</main>

<footer class="site-footer">
  <div class="wrap site-footer__inner">
    <span>Stanford Daily Tech Bootcamp · data journalism</span>
    <span><a href="https://github.com/aayanahmed200/stanford-daily-blotter-fiction">Repository</a> · <a href="https://github.com/TheStanfordDaily/tech-practicum">Practicum</a></span>
  </div>
</footer>

</body>
</html>
"""


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", text)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", text)


def render(markdown):
    """Headings, rules and paragraphs of STORY.md; the title lives in the template."""
    blocks, paragraph = [], []

    def flush():
        if paragraph:
            blocks.append("<p>" + inline(" ".join(paragraph)) + "</p>")
            paragraph.clear()

    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            flush()
        elif line in {"---", "***", "___"}:
            flush()
            blocks.append("<hr>")
        elif line.startswith("## "):
            flush()
            blocks.append("<h2>" + inline(line[3:]) + "</h2>")
        elif line.startswith("# "):
            flush()
        else:
            paragraph.append(line)
    flush()
    return "\n\n".join(blocks)


def main():
    story = render(SOURCE.read_text(encoding="utf-8"))
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(
        TEMPLATE.format(fonts=FONTS, nav=NAV, story=story), encoding="utf-8"
    )
    print(f"Wrote {OUTPUT.relative_to(ROOT)} from {SOURCE.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
