# Zhuokun Chen — personal homepage

An English academic homepage, built with plain HTML and CSS. No runtime dependencies, external fonts, tracking, or build service. Open `index.html` directly, or serve this directory:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000 on the same machine. On a remote machine, forward port 8000 over SSH first.

## Editing

- `publications.json`: 7 selected publications, authors, venues, links, research topics. Author order and venue/year follow the user's supplied Scholar list (2026-10-12). `self_index` identifies Zhuokun Chen.
- `cofirst_indices` explicitly lists authors marked with equal-contribution asterisks. Per the user’s correction on 2026-10-12, on the three displayed papers where he is not first, mark everyone from the first author through Zhuokun Chen inclusive; preserve the original author order.
- `build.py`: introduction, News announcements (newest first, dates and authorship supplied by the user), and page structure. Run `python build.py` after editing the data or template. Python standard library only.
- `styles.css`: responsive layout and visual design.

Citation counts are intentionally omitted because they change. The biography and education/supervision details follow the user’s supplied text (2026-10-12). Supervisor names link to their verified personal homepages. The publication list has no search or topic filters. Publication thumbnails use original method figures. Click any thumbnail to open the full-size image. Figure sources and PDF crop coordinates are recorded in `assets/papers/sources.json`.

## Sources

Primary bibliography: the complete list supplied by the user. Author names remain abbreviated except Zhuokun Chen. Venue labels follow that list, including ICML 2026 and NeurIPS 2026; they were not independently revalidated.

- Scholar: https://scholar.google.com/citations?user=UT9aJX0AAAAJ&hl=en
- R-Stitch project / disambiguation of the first author: https://caesarhhh.github.io/R-Stitch/
- SparseVAR paper: https://arxiv.org/abs/2507.20454
- HLA project links: the existing sibling `HLA_publish/README.md`.
- arXiv links for recent papers use IDs supplied by the user. Every publication has a direct Paper link. Confirmed official project pages and implementation repositories appear as Project and Code, in that order; A Google Scholar profile link below Selected Publications points to the complete list.

## Hosting

The directory is ready for static hosting, including GitHub Pages. Publish `index.html`, `styles.css`, `assets/` and `.nojekyll`. Repository: https://github.com/caesarzkchen/caesarzkchen.github.io

Website (after enabling GitHub Pages): https://caesarzkchen.github.io/

In repository Settings → Pages, select Deploy from a branch → main → / (root). Public contact email: caesard216@gmail.com. Optional next edit: CV.
