#!/usr/bin/env python3
"""Build the dependency-free homepage: python build.py."""
import json
from pathlib import Path
from html import escape as e
ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / 'publications.json').read_text())

def links(p):
    return ' '.join(f'<a href="{e(url, quote=True)}">{e(label)} <span aria-hidden="true">↗</span></a>' for label, url in p['links'].items())

def paper(p):
    authors = p['authors'].split(', ')
    authors = [e(a) for a in authors]
    authors[p['self_index']] = '<strong>Zhuokun Chen</strong>'
    for i in p.get('cofirst_indices', []):
        authors[i] += '<sup title="Co-first author (equal contribution)">*</sup>'
    authors = ', '.join(authors)
    figure = (f'<a class="paper-figure" href="{e(p["image"], quote=True)}" target="_blank" rel="noopener" aria-label="View method figure: {e(p["title"], quote=True)}"><img src="{e(p["image"], quote=True)}" alt="{e(p["image_alt"], quote=True)}" loading="lazy" decoding="async"></a>' if p.get('image') else '')
    return f'''<article class="paper" data-topic="{e(p['topic'])}" data-year="{p['year']}">
    <div class="paper-media"><div class="paper-year">{p['year']}</div>{figure}</div><div><span class="venue">{e(p['venue'])}</span>
    <h3><a href="{e(p['links']['Paper'], quote=True)}">{e(p['title'])}</a></h3>
    <p class="authors">{authors}</p><div class="paper-links">{links(p)}</div></div></article>'''

html = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zhuokun Chen | Efficient Generative AI</title>
<meta name="description" content="Zhuokun Chen's research on efficient generative AI, hybrid linear attention, video world models, and language model reasoning.">
<meta name="theme-color" content="#f8f9fb"><meta property="og:title" content="Zhuokun Chen | Efficient Generative AI"><meta property="og:description" content="Research on efficient generation, long-context modeling, and video world models."><meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"><script src="script.js" defer></script></head>
<body><a class="skip-link" href="#main">Skip to content</a><div class="layout">
<aside class="sidebar"><a href="#about" class="monogram" aria-label="Zhuokun Chen home"><img src="assets/avatar-square.jpg" alt="Gengar avatar" width="88" height="88" decoding="async"></a><a class="side-name" href="#about">Zhuokun Chen</a><p class="side-description">Efficient generative AI<br>Language · Vision · Video</p>
<nav aria-label="Main navigation"><a href="#about">About <span>01</span></a><a href="#publications">Selected Publications <span>02</span></a><a href="#service">Service <span>03</span></a></nav>
<div class="side-links"><a href="https://github.com/Caesarhhh">GitHub ↗</a></div><p class="sidebar-note">Research & selected work<br>2023 — 2026</p></aside>
<main id="main"><section id="about" class="intro"><div class="eyebrow intro-label"><span class="dot"></span> Generative AI & efficient computation</div><h1>Zhuokun Chen<span class="name-dot">.</span></h1><p class="lead">Making generative models<br><em>more efficient.</em></p><p class="bio">My research focuses on efficient generative AI, spanning language, images, and video. I am interested in how models allocate computation and retain useful context—from hybrid linear attention and long-horizon video world models to efficient generation and reasoning.</p><div class="intro-links"><a class="primary-link" href="#publications">Explore my research <span>↓</span></a></div><div class="interests"><span>Efficient generation</span><span>Long-context modeling</span><span>Video world models</span></div></section>
<section id="publications"><div class="section-heading"><div><span class="eyebrow">02 / Publications</span><h2>Selected Publications</h2></div></div><p class="publication-more">For more publications, see <a href="https://scholar.google.com/citations?user=UT9aJX0AAAAJ&amp;hl=en">Google Scholar ↗</a>.</p><div class="publication-controls" hidden><div class="filters" role="group" aria-label="Filter publications by research area"><button type="button" data-filter="all" aria-pressed="true">All</button><button type="button" data-filter="generation" aria-pressed="false">Generation</button><button type="button" data-filter="reasoning" aria-pressed="false">Reasoning</button><button type="button" data-filter="vision" aria-pressed="false">Vision</button></div><label class="search-label"><span class="sr-only">Search publications</span><input id="search" type="search" placeholder="Search papers…" autocomplete="off"></label></div><p id="result-count" class="result-count" aria-live="polite">''' + str(len(data)) + ''' selected publications · newest first</p><p class="result-count">* Equal contribution (co-first author).</p><div class="papers">''' + ''.join(paper(p) for p in data) + '''</div><p id="empty" hidden>No publications match your search.</p></section>
<section id="service" aria-labelledby="service-heading"><div class="section-heading"><div><span class="eyebrow">03 / Academic service</span><h2 id="service-heading">Academic Service</h2></div></div><div class="service-list"><div><h3>Journal Reviewer</h3><p>TPAMI · IJCV · TIP</p></div><div><h3>Conference Reviewer</h3><p>ICML 2026 · NeurIPS 2026 · ICLR 2026</p></div></div></section>
<footer><span>© 2026 Zhuokun Chen</span><a href="#about">Back to top ↑</a></footer></main></div></body></html>'''
(ROOT / 'index.html').write_text(html)
print(f'Built index.html with {len(data)} publications.')
