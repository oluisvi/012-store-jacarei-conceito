const INSTAGRAM = 'https://www.instagram.com/012storesurfwear_';
const PRODUCTS = [
  { id: 'tech-fleece', category: 'Conjuntos', name: 'Conjunto Tech Fleece', note: 'Conjunto esportivo em publicação da loja.', description: 'A legenda da publicação identifica o conjunto Tech Fleece e informa tamanhos do M ao GG naquele post. Isso não confirma estoque ou grade atual.', image: 'assets/catalog-tech-fleece.jpg', post: `${INSTAGRAM}/p/DdeO6BNSPCK/`, tag: 'CONJUNTO', alt: 'Pessoa usando conjunto esportivo escuro publicado pela 012 Store' },
  { id: 'tnf-air', category: 'Conjuntos', name: 'Conjunto TNF Air', note: 'Referência de camiseta e bermuda.', description: 'Composição de camiseta e bermuda apresentada em publicação da loja. Consulte a equipe para confirmar opções disponíveis.', image: 'assets/catalog-tnf-set.jpg', post: `${INSTAGRAM}/p/DdJwMstvz7x/`, tag: 'CONJUNTO', alt: 'Composição de camiseta TNF Air, bermuda e acessórios publicada pela 012 Store' },
  { id: 'quiksilver', category: 'Conjuntos', name: 'Conjunto Quiksilver', note: 'Camiseta e bermuda em uma referência.', description: 'Conjunto gráfico apresentado numa publicação da loja. A imagem serve como referência visual, sem afirmar estoque ou variantes atuais.', image: 'assets/catalog-quiksilver-set.jpg', post: `${INSTAGRAM}/p/DcygMdsnG72/`, tag: 'CONJUNTO', alt: 'Camiseta escura e bermuda clara Quiksilver em referência publicada pela 012 Store' },
  { id: 'polos', category: 'Polos', name: 'Polos em diferentes cores', note: 'Uma publicação reúne opções de polos.', description: 'Referência visual de polos em cores diferentes na mesma publicação. As cores e peças disponíveis devem ser confirmadas diretamente com a loja.', image: 'assets/catalog-polos.jpg', post: `${INSTAGRAM}/p/DdJwMstvz7x/`, tag: 'POLOS', alt: 'Polos em tons neutros e bonés numa publicação da 012 Store' },
  { id: 'tenis', category: 'Calçados', name: 'Tênis New Balance', note: 'Referência de calçados do perfil.', description: 'Publicação com modelos de tênis New Balance. Consulte a equipe para conferir modelos, numerações, preço e disponibilidade atuais.', image: 'assets/catalog-sneakers.jpg', post: `${INSTAGRAM}/p/DcqslmCP1iw/`, tag: 'CALÇADOS', alt: 'Seleção de tênis New Balance publicada pela 012 Store' }
];

const productGrid = document.querySelector('#products');
const filterHost = document.querySelector('#category-filters');
const search = document.querySelector('#search');
const dialog = document.querySelector('#product-dialog');
let currentFilter = 'all';
let selected = new Set();
let activeProduct = null;

function renderFilters() {
  const categories = ['all', ...new Set(PRODUCTS.map(product => product.category))];
  filterHost.innerHTML = categories.map(category => {
    const label = category === 'all' ? 'Tudo' : category;
    const count = category === 'all' ? PRODUCTS.length : PRODUCTS.filter(product => product.category === category).length;
    const active = currentFilter === category;
    return `<button class="filter${active ? ' is-active' : ''}" data-filter="${category}" aria-pressed="${active}">${label} <span>${String(count).padStart(2, '0')}</span></button>`;
  }).join('');
  filterHost.querySelectorAll('[data-filter]').forEach(button => button.addEventListener('click', () => {
    currentFilter = button.dataset.filter;
    renderFilters();
    renderProducts();
  }));
}

function getVisibleProducts() {
  const query = search.value.trim().toLocaleLowerCase('pt-BR');
  const sort = document.querySelector('#sort').value;
  const products = PRODUCTS.filter(product => {
    const matchesCategory = currentFilter === 'all' || product.category === currentFilter;
    const searchable = `${product.name} ${product.category} ${product.note} ${product.description}`.toLocaleLowerCase('pt-BR');
    return matchesCategory && searchable.includes(query);
  });
  if (sort === 'az') products.sort((a, b) => a.name.localeCompare(b.name, 'pt-BR'));
  if (sort === 'za') products.sort((a, b) => b.name.localeCompare(a.name, 'pt-BR'));
  return products;
}

function renderProducts() {
  const products = getVisibleProducts();
  productGrid.innerHTML = products.map(product => {
    const number = String(PRODUCTS.indexOf(product) + 1).padStart(2, '0');
    const added = selected.has(product.id);
    return `<article class="product-card">
      <button class="product-image" type="button" data-details="${product.id}" aria-label="Ver detalhes de ${product.name}">
        <img src="${product.image}" alt="${product.alt}" loading="lazy">
        <span class="product-number">${number} / ${String(PRODUCTS.length).padStart(2, '0')}</span>
        <span class="product-source">${product.tag} · DETALHES ↗</span>
      </button>
      <div class="product-meta"><div><p class="product-category">${product.category}</p><h3>${product.name}</h3><p>${product.note}</p></div>
      <button class="add${added ? ' is-added' : ''}" data-select="${product.id}" aria-label="${added ? 'Remover' : 'Adicionar'} ${product.name} ${added ? 'da' : 'à'} consulta" aria-pressed="${added}">${added ? '✓' : '+'}</button></div>
      <button class="product-details" type="button" data-details="${product.id}">Ver detalhes e publicação <span>↗</span></button>
    </article>`;
  }).join('');
  document.querySelector('.empty').hidden = products.length > 0;
  document.querySelector('#result-count').textContent = `${products.length} ${products.length === 1 ? 'referência' : 'referências'} nesta seleção`;
  productGrid.querySelectorAll('[data-select]').forEach(button => button.addEventListener('click', () => toggleSelection(button.dataset.select)));
  productGrid.querySelectorAll('[data-details]').forEach(button => button.addEventListener('click', () => openDetails(button.dataset.details)));
}

function toggleSelection(id) {
  selected.has(id) ? selected.delete(id) : selected.add(id);
  updateSelection();
  renderProducts();
  if (activeProduct?.id === id && dialog.open) updateDialogAddButton();
}

function updateSelection() {
  const bar = document.querySelector('#selection');
  bar.hidden = selected.size === 0;
  document.querySelector('#selection-count').textContent = selected.size;
  const names = [...selected].map(id => PRODUCTS.find(product => product.id === id).name).join(', ');
  document.querySelector('#selection-link').href = `https://wa.me/5512992323004?text=${encodeURIComponent(`Oi, vim pela vitrine da 012 Store e queria consultar estas referências: ${names}. Vocês podem confirmar valores, tamanhos e disponibilidade?`)}`;
}

function updateDialogAddButton() {
  const added = selected.has(activeProduct.id);
  const button = document.querySelector('#dialog-add');
  button.textContent = added ? 'Remover da consulta ✓' : 'Adicionar à consulta +';
  button.setAttribute('aria-pressed', String(added));
}

function openDetails(id) {
  activeProduct = PRODUCTS.find(product => product.id === id);
  document.querySelector('#dialog-image').src = activeProduct.image;
  document.querySelector('#dialog-image').alt = activeProduct.alt;
  document.querySelector('#dialog-kicker').textContent = `${activeProduct.category.toLocaleUpperCase('pt-BR')} · REFERÊNCIA 012`;
  document.querySelector('#dialog-title').textContent = activeProduct.name;
  document.querySelector('#dialog-description').textContent = activeProduct.description;
  document.querySelector('#dialog-source').href = activeProduct.post;
  updateDialogAddButton();
  dialog.showModal();
}

document.querySelector('.dialog-close').addEventListener('click', () => dialog.close());
dialog.addEventListener('click', event => { if (event.target === dialog) dialog.close(); });
document.querySelector('#dialog-add').addEventListener('click', () => toggleSelection(activeProduct.id));
search.addEventListener('input', renderProducts);
document.querySelector('#sort').addEventListener('change', renderProducts);
document.querySelector('#clear-selection').addEventListener('click', () => { selected.clear(); updateSelection(); renderProducts(); if (dialog.open) updateDialogAddButton(); });

document.querySelectorAll('[data-design-choice]').forEach(button => button.addEventListener('click', () => {
  const design = button.dataset.designChoice;
  document.documentElement.dataset.design = design;
  document.querySelectorAll('[data-design-choice]').forEach(option => {
    const active = option === button;
    option.classList.toggle('is-active', active);
    option.setAttribute('aria-pressed', String(active));
  });
  try { sessionStorage.setItem('012-design', design); } catch {}
}));

try {
  const saved = sessionStorage.getItem('012-design');
  if (saved && ['editorial', 'loja', 'lookbook'].includes(saved)) document.querySelector(`[data-design-choice="${saved}"]`).click();
} catch {}

renderFilters();
renderProducts();
