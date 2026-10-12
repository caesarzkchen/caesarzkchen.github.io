'use strict';
const controls = document.querySelector('.publication-controls');
const papers = [...document.querySelectorAll('.paper')];
const search = document.querySelector('#search');
function filterPapers() {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  papers.forEach(paper => {
    const matches = paper.textContent.toLocaleLowerCase().includes(query);
    paper.hidden = !matches;
    count += Number(matches);
  });
  document.querySelector('#result-count').textContent = `${count} selected publication${count === 1 ? '' : 's'} · newest first`;
  document.querySelector('#empty').hidden = count !== 0;
}
search.addEventListener('input', filterPapers);
controls.hidden = false;
