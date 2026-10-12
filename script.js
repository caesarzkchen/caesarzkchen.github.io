'use strict';
const controls = document.querySelector('.publication-controls');
const buttons = [...document.querySelectorAll('[data-filter]')];
const papers = [...document.querySelectorAll('.paper')];
const search = document.querySelector('#search');
let selected = 'all';
function filterPapers() {
  const query = search.value.trim().toLocaleLowerCase();
  let count = 0;
  papers.forEach(paper => {
    const matches = (selected === 'all' || paper.dataset.topic.split(' ').includes(selected)) && paper.textContent.toLocaleLowerCase().includes(query);
    paper.hidden = !matches;
    count += Number(matches);
  });
  document.querySelector('#result-count').textContent = `${count} publication${count === 1 ? '' : 's'} · newest first`;
  document.querySelector('#empty').hidden = count !== 0;
}
buttons.forEach(button => button.addEventListener('click', () => {
  selected = button.dataset.filter;
  buttons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
  filterPapers();
}));
search.addEventListener('input', filterPapers);
controls.hidden = false;
