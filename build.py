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
    return f'''<article class="paper" data-year="{p['year']}">
    <div class="paper-media"><div class="paper-year">{p['year']}</div>{figure}</div><div><span class="venue">{e(p['venue'])}</span>
    <h3><a href="{e(p['links']['Paper'], quote=True)}">{e(p['title'])}</a></h3>
    <p class="authors">{authors}</p><div class="paper-links">{links(p)}</div></div></article>'''

html = '''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Zhuokun Chen | Efficient Generative AI</title>
<meta name="description" content="Zhuokun (Caesar) Chen's research on efficient image and video generation and large language models, including sparse and linear attention and token reduction.">
<meta name="theme-color" content="#f8f9fb"><meta property="og:title" content="Zhuokun Chen | Efficient Generative AI"><meta property="og:description" content="Efficient generative models through sparse and linear attention, token reduction, and related techniques."><meta property="og:type" content="website">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="styles.css"></head>
<body><a class="skip-link" href="#main">Skip to content</a><div class="layout">
<aside class="sidebar"><a href="#about" class="monogram" aria-label="Zhuokun Chen home"><img src="assets/avatar-square.jpg" alt="Gengar avatar" width="88" height="88" decoding="async"></a><a class="side-name" href="#about">Zhuokun Chen</a><p class="side-description">Efficient generative AI<br>Language · Vision · Video</p>
<nav aria-label="Main navigation"><a href="#about">About <span>01</span></a><a href="#publications">Selected Publications <span>02</span></a><a href="#service">Service <span>03</span></a></nav>
<p class="sidebar-note">Research & selected work<br>2023 — 2026</p></aside>
<main id="main"><section id="about" class="intro"><div class="eyebrow intro-label"><span class="dot"></span> Generative AI & efficient computation</div><h1>Zhuokun Chen<span class="name-dot">.</span></h1><p class="lead">Making generative models<br><em>more efficient.</em></p><p class="bio">I am Zhuokun Chen, and I also go by Caesar. I received my master's degree from South China University of Technology in 2025, supervised by <a href="https://tanmingkui.github.io/">Mingkui Tan</a>. In the same year, I began my PhD at Monash University, supervised by <a href="https://bohanzhuang.github.io/">Bohan Zhuang</a> and <a href="https://jianfei-cai.github.io/">Jianfei Cai</a>.</p><p class="bio">My research focuses on improving the efficiency of generative models, including image and video generation models and large language models (LLMs). I am particularly interested in sparse and linear attention, token reduction, and related techniques.</p><p class="bio">Contact: <a href="mailto:caesard216@gmail.com">caesard216@gmail.com</a></p><div class="intro-links"><a class="primary-link" href="#publications">Explore my research <span>↓</span></a></div><div class="interests"><span>Sparse / linear attention</span><span>Token reduction</span><span>Efficient generative models</span></div></section>
<section id="publications"><div class="section-heading"><div><span class="eyebrow">02 / Publications</span><h2>Selected Publications</h2></div></div><p class="publication-more">For more publications, see <a href="https://scholar.google.com/citations?user=UT9aJX0AAAAJ&amp;hl=en">Google Scholar ↗</a>.</p><p class="result-count">* Equal contribution (co-first author).</p><div class="papers">''' + ''.join(paper(p) for p in data) + '''</div></section>
<section id="service" aria-labelledby="service-heading"><div class="section-heading"><div><span class="eyebrow">03 / Academic service</span><h2 id="service-heading">Academic Service</h2></div></div><div class="service-list"><div><h3>Journal Reviewer</h3><p>TPAMI · IJCV · TIP</p></div><div><h3>Conference Reviewer</h3><p>ICML 2026 · NeurIPS 2026 · ICLR 2026</p></div></div></section>
<footer><span>© 2026 Zhuokun Chen</span><a href="#about">Back to top ↑</a></footer></main></div></body></html>'''
(ROOT / 'index.html').write_text(html)
print(f'Built index.html with {len(data)} publications.')
