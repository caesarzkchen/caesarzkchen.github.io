#!/usr/bin/env python3
"""Build the dependency-free homepage: python build.py."""
import json
from hashlib import sha256
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
<nav aria-label="Main navigation"><a href="#about">About <span>01</span></a><a href="#news">News <span>02</span></a><a href="#publications">Selected Publications <span>03</span></a><a href="#service">Service <span>04</span></a></nav>
<p class="sidebar-note">Research & selected work<br>2023 — 2026</p></aside>
<main id="main"><section id="about" class="intro"><div class="eyebrow intro-label"><span class="section-icon" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><circle cx="12" cy="8" r="3"/><path d="M5 21v-2a7 7 0 0 1 14 0v2"/></svg></span> About me</div><h1>Zhuokun Chen<span class="name-dot">.</span></h1><p class="lead">Making generative models<br><em>more efficient.</em></p><p class="bio">I am Zhuokun Chen, and I also go by Caesar. I received my master's degree from South China University of Technology in 2025, supervised by <a href="https://tanmingkui.github.io/">Mingkui Tan</a>. In the same year, I began my PhD at Monash University, supervised by <a href="https://bohanzhuang.github.io/">Bohan Zhuang</a> and <a href="https://jianfei-cai.github.io/">Jianfei Cai</a>.</p><p class="bio">My research focuses on improving the efficiency of generative models, including image and video generation models and large language models (LLMs). I am particularly interested in sparse and linear attention, token reduction, and related techniques.</p><p class="bio">Contact: <a href="mailto:caesard216@gmail.com">caesard216@gmail.com</a></p><div class="interests"><span>Sparse / linear attention</span><span>Token reduction</span><span>Efficient generative models</span></div></section>
<section id="news" aria-labelledby="news-heading"><div class="section-heading"><div><span class="eyebrow">02 / Updates</span><h2 id="news-heading"><span class="section-icon" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="m4 10 14-5v14L4 14zM18 10h3v4h-3M6 15l2 6h3l-2-5"/></svg></span>News</h2></div></div>
<ul class="news-list">
<li><span class="news-icon" aria-hidden="true"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="#418da4" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="m12 8-5 1-4 5 6 1M16 12l-1 5-5 4-1-6" fill="#dceef3"/><path d="M9 15C9 9 14 3 21 3c0 7-6 12-12 12Z" fill="#e7f2ff"/><circle cx="16" cy="8" r="2" fill="#a4cce7"/><path d="M7 17c-2-1-4 1-4 4 3 0 5-2 4-4Z" fill="#ffdc86" stroke="#bd7730"/></svg></span><p>The <strong>HLA series</strong> projects have been released (first author). <time datetime="2026-10">Oct 2026</time></p></li>
<li><span class="news-icon" aria-hidden="true"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="#418da4" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="m12 8-5 1-4 5 6 1M16 12l-1 5-5 4-1-6" fill="#dceef3"/><path d="M9 15C9 9 14 3 21 3c0 7-6 12-12 12Z" fill="#e7f2ff"/><circle cx="16" cy="8" r="2" fill="#a4cce7"/><path d="M7 17c-2-1-4 1-4 4 3 0 5-2 4-4Z" fill="#ffdc86" stroke="#bd7730"/></svg></span><p>The <strong>SAF</strong> project has been released (co-first author). <time datetime="2026-10">Oct 2026</time></p></li>
<li><span class="news-icon" aria-hidden="true"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="m3 21 4-13 10 9z" fill="#ffdc86" stroke="#bd7730"/><path d="m5 15 5 4M7 10l7 7" stroke="#e09a3d"/><path d="M13 3c3 3-3 4 0 7M18 6c-3-2 0-4 2-3M17 12c3-3 3 2 5 0" stroke="#9b70c4"/><path d="m7 3 1 1M21 7l-1 1M20 18l1 1" stroke="#418da4"/></svg></span><p><strong>DASA</strong> has been accepted to <strong>NeurIPS 2026</strong> (co-first author). <time datetime="2026-09">Sep 2026</time></p></li>
<li><span class="news-icon" aria-hidden="true"><svg width="21" height="21" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="m3 21 4-13 10 9z" fill="#ffdc86" stroke="#bd7730"/><path d="m5 15 5 4M7 10l7 7" stroke="#e09a3d"/><path d="M13 3c3 3-3 4 0 7M18 6c-3-2 0-4 2-3M17 12c3-3 3 2 5 0" stroke="#9b70c4"/><path d="m7 3 1 1M21 7l-1 1M20 18l1 1" stroke="#418da4"/></svg></span><p><strong>FlashBlock</strong> has been accepted to <strong>ICML 2026</strong> (first author). <time datetime="2026-05">May 2026</time></p></li>
</ul></section>
<section id="publications"><div class="section-heading"><div><span class="eyebrow">03 / Publications</span><h2><span class="section-icon" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="M12 6C9 4 5 4 2 5v15c3-1 7-1 10 1 3-2 7-2 10-1V5c-3-1-7-1-10 1zm0 0v15M5 9h4M15 9h4M5 13h4M15 13h4"/></svg></span>Selected Publications</h2></div></div><p class="publication-more">For more publications, see <a href="https://scholar.google.com/citations?user=UT9aJX0AAAAJ&amp;hl=en">Google Scholar ↗</a>.</p><p class="result-count">* Equal contribution (co-first author).</p><div class="papers">''' + ''.join(paper(p) for p in data) + '''</div></section>
<section id="service" aria-labelledby="service-heading"><div class="section-heading"><div><span class="eyebrow">04 / Academic service</span><h2 id="service-heading"><span class="section-icon" aria-hidden="true"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" focusable="false"><path d="m2 9 4-4 5 2 3-2 8 5-4 8-5 3-8-6zM11 7l-3 4 3 2 3-3 6 5M5 15l3-3M8 18l3-3M11 20l3-3"/></svg></span>Academic Service</h2></div></div><div class="service-list"><div><h3>Journal Reviewer</h3><p>TPAMI · IJCV · TIP</p></div><div><h3>Conference Reviewer</h3><p>ICML 2026 · NeurIPS 2026 · ICLR 2026</p></div></div></section>
<footer><span>© 2026 Zhuokun Chen</span><a href="#about">Back to top ↑</a></footer></main></div></body></html>'''
# Change the stylesheet URL whenever its content changes to avoid stale CSS.
css_version = sha256((ROOT / 'styles.css').read_bytes()).hexdigest()[:12]
html = html.replace('href="styles.css"', f'href="styles.css?v={css_version}"')
(ROOT / 'index.html').write_text(html)
print(f'Built index.html with {len(data)} publications.')
