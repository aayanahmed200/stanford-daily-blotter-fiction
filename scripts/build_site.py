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
    <div class="masthead__right">
      <nav class="masthead__nav" aria-label="Series">
{nav}
      </nav>
      <a class="masthead__gh" href="https://github.com/aayanahmed200" rel="me">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
        <span>aayanahmed200</span>
      </a>
    </div>
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

  <section class="refs" aria-labelledby="references">
    <h2 id="references">References</h2>
    <ol>
      <li>Stanford Daily police-blotter dataset, <code>stanforddams/daily</code> (139 articles, September 2021 to June 2026). <a href="https://huggingface.co/datasets/stanforddams/daily">huggingface.co/datasets/stanforddams/daily</a></li>
      <li>The Stanford Daily. SUDPS blotter summaries, published weekly. <a href="https://stanforddaily.com/">stanforddaily.com</a></li>
      <li>Dataset notes and the taxonomy exploration that produced the location counts: <a href="https://github.com/aayanahmed200/stanford-daily-blotter-fiction">github.com/aayanahmed200/stanford-daily-blotter-fiction</a></li>
    </ol>
  </section>

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
    <span class="site-footer__series">Series: <a href="https://aayanahmed200.github.io/stanford-daily-price-of-prestige/">The Price of Prestige</a> · <a href="https://aayanahmed200.github.io/stanford-daily-plasticlist-eda/">PlasticList</a> · <a href="https://aayanahmed200.github.io/stanford-daily-biglocal-ice-pipeline/">ICE pipeline</a></span>
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
