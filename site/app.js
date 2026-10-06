'use strict';

const repository = 'https://github.com/lucasmachi/projeto-analytics-ecommerce';
const content = {
  en: {
    nav: ['Revenue', 'Customers', 'Forecasting', 'Method'],
    eyebrow: 'Data science case study · Brazil',
    title: 'Behind every order,<br><em>a story in data.</em>',
    intro: 'An exploration of Olist’s e-commerce data: how revenue evolves, where delivery friction appears, and what daily sales models can tell us.',
    explore: 'Explore the analysis', code: 'View on GitHub', by: 'Analysis & development by Lucas Machi',
    panelTitle: 'Daily revenue · test results', days: '60-day test', panelLabel: 'Mean absolute error · Linear Regression',
    panelFoot: 'Reported MAE in BRL. Evaluation setups differ; see the forecasting section.',
    stack: 'The toolkit', revenueLabel: '01 / Revenue & categories', revenueTitle: 'Follow the money.',
    revenueIntro: 'From monthly patterns to category performance. Two revenue definitions, clearly separated.',
    graphLanguage: 'Original charts are in Portuguese. Select a chart to enlarge it.',
    revenueNote: 'The Python chart sums payment_value. The R chart sums item prices for delivered orders. Their definitions and date windows differ, so totals should not be compared directly.',
    insightLabel: 'Category spotlight', insightTitle: 'Health & Beauty<br>leads in item revenue.',
    insightText: 'The category ranks first in the revenue chart, ahead of Watches & Gifts and Bed, Bath & Table.',
    insightDetail: 'The Welch test script compares individual item prices between two categories, not the average total value of an order. Its revised result still needs to be rerun.',
    customerLabel: '02 / Customers & logistics', customerTitle: 'Location changes<br>the picture.',
    customerIntro: 'Explore basket value, shipping costs and the delivery gap between two major markets.',
    logisticsTitle: 'A delivery gap worth investigating.',
    logisticsText: 'Reported late-delivery rates differ by 7.58 percentage points between RJ and SP. The difference invites investigation; it does not identify its cause.',
    logisticsSource: 'Reported historical rates.',
    forecastLabel: '03 / Predictive modeling', forecastTitle: 'Three models.<br>Different perspectives.',
    forecastIntro: 'Daily revenue predictions evaluated against observed values during the final 60 days of the series.',
    forecastChartTitle: 'Actual revenue and model predictions', forecastChartDesc: 'The original comparison, including the sharp decline at the end of the test window.',
    forecastCaption: 'Linear Regression and Random Forest use observed lag values during testing. Prophet forecasts the entire window from a single cutoff.',
    metricsTitle: 'How far were the predictions off?',
    mae: 'MAE is the average absolute error in daily revenue. A lower value means a smaller average miss. It does not show whether forecasts were too high or too low.',
    rmse: 'RMSE gives more weight to large errors and is also expressed in BRL. It is neither a percentage nor the cumulative error over the 60 days.',
    warningTitle: 'Same test period. Different information available.',
    warning: 'Linear Regression and Random Forest receive actual revenue from earlier test days through their lag features, without retraining. Prophet receives none of those observations. The scores describe these setups, rather than proving one algorithm is better under equivalent forecasting conditions.',
    methodLabel: '04 / Method & interpretation', methodTitle: 'From raw data<br>to a clearer decision.',
    methodIntro: 'Cloud processing, statistical comparisons and time-aware evaluation.',
    methods: [
      ['Query & prepare', 'BigQuery and SQL connect orders, items, payments and customers. Python and R aggregate the data for the business question being explored.'],
      ['Explore & compare', 'Visual analysis examines revenue and geography. Welch’s t-test compares item prices; a two-proportion z-test compares delivery delays.'],
      ['Model & evaluate', 'Daily revenue models use calendar features, 1/7/14-day lags and shifted rolling means. The final 60 days are reserved for testing.']
    ],
    limitsTitle: 'What these results say',
    limits: 'These are historical observations, not a view of Olist’s current operations. The ML script selects data between January 2017 and August 2018 and fills absent days with zero, which assumes those dates represent no sales. The final decline should be checked for incomplete coverage before operational use. Statistical comparisons are observational, and item-level tests may contain dependent observations. Forecasts at a new horizon require a matching evaluation.',
    closingTitle: 'Explore the work behind the results.', closingText: 'Python, R, SQL queries and the full project documentation.',
    footer: 'Independent portfolio project · Public Olist dataset', footerRight: 'Lucas Machi / E-commerce analytics',
    enlarge: 'Enlarge chart', close: 'Close', original: 'Original project chart · Portuguese',
    charts: [
      ['sazonalidade_faturamento.png', 'Python · Pandas', 'Monthly payments', 'A historical view of payments associated with delivered orders.', 'Payments rise through much of the series, with a visible peak in November 2017. Early sparse months need care when interpreting growth.', 'graficos.py · sum(payment_value)', 'Line chart of monthly payments, showing growth from 2016 to 2018 and a peak in November 2017.'],
      ['evolucao_faturamento.png', 'R · ggplot2', 'Monthly product revenue', 'Item-price totals for delivered orders, within the selected 2017–2018 window.', 'This view isolates product revenue. Shipping and other payment components are not added to the item-price measure.', 'eda.R · sum(price)', 'Line chart of monthly product revenue in 2017 and 2018, with a November 2017 peak.'],
      ['top10_categorias_receita.png', 'R · dplyr', 'Top 10 categories by revenue', 'Ranking based on the sum of item prices for delivered orders.', 'Health & Beauty takes the top position in the chart; a revenue ranking alone does not explain customer motivation.', 'eda.R · category totals', 'Horizontal bars ranking ten categories; Health & Beauty, Watches & Gifts, and Bed, Bath & Table are the top three.'],
      ['ticket_medio_por_estado.png', 'Python · Geography', 'Average order value by state', 'The ten highest state averages, calculated from item-price totals per delivered order.', 'Paraíba leads this ranking. Bigger baskets to offset shipping costs are a hypothesis to investigate, not a confirmed explanation.', 'graficos.py · mean(order item-price total)', 'Bar chart of ten states by average order value; Paraíba is first, followed by Amapá and Acre.'],
      ['correlacao_preco_frete.png', 'Python · Sample of 5,000 items', 'Product price vs. shipping cost', 'A scatterplot with a fitted line; the displayed axes limit the visible range.', 'The fitted line slopes upward, while individual shipping costs vary widely. This visualization alone does not establish causality.', 'graficos.py · price / freight_value', 'Scatterplot of item price and shipping cost, with an upward fitted line and substantial dispersion.']
    ]
  },
  pt: {
    nav: ['Receita', 'Clientes', 'Previsões', 'Método'],
    eyebrow: 'Estudo de ciência de dados · Brasil',
    title: 'Cada pedido,<br><em>uma história<br>nos dados.</em>',
    intro: 'Uma análise do e-commerce da Olist: como o faturamento evolui, onde aparecem desafios de entrega e o que os modelos de vendas diárias revelam.',
    explore: 'Explorar a análise', code: 'Ver no GitHub', by: 'Análise e desenvolvimento por Lucas Machi',
    panelTitle: 'Receita diária · resultados', days: '60 dias de teste', panelLabel: 'Erro médio absoluto · Regressão Linear',
    panelFoot: 'MAE relatado em reais. As avaliações usam estratégias diferentes; veja a seção de previsões.',
    stack: 'Ferramentas', revenueLabel: '01 / Receita e categorias', revenueTitle: 'O caminho da receita.',
    revenueIntro: 'Dos padrões mensais ao desempenho das categorias. Duas medidas de receita, com definições distintas.',
    graphLanguage: 'Os gráficos originais estão em português. Selecione um gráfico para ampliar.',
    revenueNote: 'O gráfico em Python soma payment_value. O gráfico em R soma os preços dos itens de pedidos entregues. As definições e os períodos diferem; os totais não devem ser comparados diretamente.',
    insightLabel: 'Categoria em destaque', insightTitle: 'Beleza e Saúde<br>lidera a receita de itens.',
    insightText: 'A categoria aparece em primeiro lugar no gráfico de receita, à frente de Relógios e Presentes e Cama, Mesa e Banho.',
    insightDetail: 'O script do teste de Welch compara preços individuais de itens entre duas categorias, não o valor médio total por pedido. O resultado revisado ainda precisa ser recalculado.',
    customerLabel: '02 / Clientes e logística', customerTitle: 'A localização<br>muda o cenário.',
    customerIntro: 'Ticket médio, custos de frete e a diferença de atrasos entre dois grandes mercados.',
    logisticsTitle: 'Uma diferença de entregas a investigar.',
    logisticsText: 'As taxas de atraso relatadas diferem em 7,58 pontos percentuais entre RJ e SP. A diferença indica uma oportunidade de investigação, mas não identifica sua causa.',
    logisticsSource: 'Taxas históricas relatadas.',
    forecastLabel: '03 / Modelagem preditiva', forecastTitle: 'Três modelos.<br>Perspectivas diferentes.',
    forecastIntro: 'Previsões de faturamento diário avaliadas em relação aos valores observados nos últimos 60 dias da série.',
    forecastChartTitle: 'Faturamento real e previsões dos modelos', forecastChartDesc: 'O comparativo original, incluindo a queda acentuada no final da janela de teste.',
    forecastCaption: 'Regressão Linear e Random Forest usam valores reais anteriores durante o teste. O Prophet prevê toda a janela a partir de um único ponto de corte.',
    metricsTitle: 'Quanto as previsões se afastaram do real?',
    mae: 'MAE é a média dos erros absolutos do faturamento diário. Um valor menor significa um desvio médio menor. Não informa se as previsões ficaram acima ou abaixo do real.',
    rmse: 'RMSE dá mais peso aos erros grandes e também é expresso em reais. Não é uma porcentagem nem o erro acumulado nos 60 dias.',
    warningTitle: 'Mesmo período de teste. Informações disponíveis diferentes.',
    warning: 'Regressão Linear e Random Forest recebem o faturamento real de dias anteriores do teste pelas variáveis de defasagem, sem retreinamento. O Prophet não recebe essas observações. Os erros descrevem essas configurações, sem comprovar que um algoritmo é melhor em condições equivalentes de previsão.',
    methodLabel: '04 / Método e interpretação', methodTitle: 'Dos dados brutos<br>à decisão informada.',
    methodIntro: 'Processamento em nuvem, comparações estatísticas e avaliação temporal.',
    methods: [
      ['Consultar e preparar', 'BigQuery e SQL conectam pedidos, itens, pagamentos e clientes. Python e R agregam os dados de acordo com a pergunta de negócio.'],
      ['Explorar e comparar', 'A análise visual examina receita e geografia. O teste t de Welch compara preços de itens; o teste z de proporções compara atrasos nas entregas.'],
      ['Modelar e avaliar', 'Os modelos de receita diária usam calendário, defasagens de 1/7/14 dias e médias móveis deslocadas. Os últimos 60 dias são reservados para teste.']
    ],
    limitsTitle: 'O que os resultados permitem concluir',
    limits: 'As observações são históricas e não descrevem a operação atual da Olist. O script de ML seleciona dados entre janeiro de 2017 e agosto de 2018 e preenche datas ausentes com zero, assumindo ausência de vendas. A queda final exige verificação de cobertura antes de uso operacional. As comparações estatísticas são observacionais; testes por item podem incluir observações dependentes. Não há exportações de dados brutos nesta página: os gráficos são imagens originais do projeto e as métricas vêm do README. Um novo horizonte de previsão exige avaliação correspondente.',
    closingTitle: 'Conheça o trabalho por trás dos resultados.', closingText: 'Python, R, consultas SQL e documentação completa do projeto.',
    footer: 'Projeto independente de portfólio · Dados públicos da Olist', footerRight: 'Lucas Machi / Análise de e-commerce',
    enlarge: 'Ampliar gráfico', close: 'Fechar', original: 'Gráfico original do projeto · Português',
    charts: [
      ['sazonalidade_faturamento.png', 'Python · Pandas', 'Pagamentos por mês', 'Evolução histórica dos pagamentos associados a pedidos entregues.', 'Os pagamentos crescem em boa parte da série, com um pico visível em novembro de 2017. Os meses iniciais esparsos exigem cuidado na interpretação.', 'graficos.py · soma de payment_value', 'Gráfico de linhas dos pagamentos mensais, com crescimento de 2016 a 2018 e pico em novembro de 2017.'],
      ['evolucao_faturamento.png', 'R · ggplot2', 'Receita mensal de produtos', 'Soma dos preços dos itens de pedidos entregues, no recorte selecionado de 2017–2018.', 'Esta visão isola a receita de produtos. Frete e outros componentes do pagamento não são adicionados aos preços dos itens.', 'eda.R · soma de price', 'Gráfico de linhas da receita mensal de produtos em 2017 e 2018, com pico em novembro de 2017.'],
      ['top10_categorias_receita.png', 'R · dplyr', 'Top 10 categorias por receita', 'Ranking pela soma dos preços dos itens de pedidos entregues.', 'Beleza e Saúde ocupa a primeira posição; um ranking de receita, sozinho, não explica a motivação dos consumidores.', 'eda.R · totais por categoria', 'Barras horizontais com dez categorias; Beleza e Saúde, Relógios e Presentes e Cama, Mesa e Banho são as três primeiras.'],
      ['ticket_medio_por_estado.png', 'Python · Geografia', 'Ticket médio por estado', 'As dez maiores médias estaduais, calculadas pelo total de preços dos itens por pedido entregue.', 'A Paraíba lidera o ranking. Carrinhos maiores para compensar o frete são uma hipótese a investigar, não uma explicação comprovada.', 'graficos.py · média do total de itens por pedido', 'Barras de dez estados por ticket médio; Paraíba é a primeira, seguida de Amapá e Acre.'],
      ['correlacao_preco_frete.png', 'Python · Amostra de 5 mil itens', 'Preço do produto vs. frete', 'Dispersão com linha ajustada; os limites dos eixos restringem a faixa exibida.', 'A linha ajustada é crescente, mas os fretes individuais variam bastante. O gráfico, isoladamente, não demonstra causalidade.', 'graficos.py · price / freight_value', 'Dispersão de preço do item e frete, com linha ajustada crescente e ampla variação dos pontos.']
    ]
  }
};

let language = 'en';
let metric = 'mae';
try { const saved = localStorage.getItem('olist-language'); if (saved === 'pt' || saved === 'en') language = saved; } catch {}
const models = [
  { en: 'Linear Regression', pt: 'Regressão Linear', mae: 5163.81, rmse: 6476.80, color: '' },
  { en: 'Random Forest', pt: 'Random Forest', mae: 5206.60, rmse: 6796.30, color: 'orange' },
  { en: 'Prophet', pt: 'Prophet', mae: 8743.44, rmse: 11183.64, color: 'neutral' }
];
const sections = ['revenue', 'customers', 'forecasting', 'method'];
const main = document.querySelector('main');
const dialog = document.querySelector('#lightbox');
const money = value => new Intl.NumberFormat(language === 'pt' ? 'pt-BR' : 'en-US', {minimumFractionDigits:2,maximumFractionDigits:2}).format(value);
const codeLink = label => `<a class="button accent" href="${repository}" target="_blank" rel="noopener noreferrer">${label}</a>`;

function chartButton(file, title, alt, caption) {
  const t = content[language];
  return `<button type="button" class="chart-button" data-image="${file}" data-title="${title}" data-caption="${caption}" aria-label="${t.enlarge}: ${title}"><img src="assets/${file}" alt="${alt}" loading="lazy" decoding="async"><span class="zoom-label">${t.enlarge} ⤢</span></button>`;
}
function chartCard(c) {
  return `<article class="glass chart-card"><div class="card-head"><div class="card-meta">${c[1]}</div><h3>${c[2]}</h3><p>${c[3]}</p></div>${chartButton(c[0],c[2],c[6],c[4])}<div class="card-foot"><p>${c[4]}</p><span class="source">${c[5]}</span></div></article>`;
}
function heading(label, title, intro) {
  return `<div class="section-heading"><div><p class="eyebrow">${label}</p><h2>${title}</h2></div><p>${intro}</p></div>`;
}
function render() {
  const t = content[language];
  document.documentElement.lang = language === 'pt' ? 'pt-BR' : 'en';
  document.title = language === 'pt' ? 'Olist Analytics — Análise por Lucas Machi' : 'Olist Analytics — Lucas Machi';
  document.querySelector('meta[name="description"]').content = t.intro;
  document.querySelectorAll('[data-lang]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.lang === language)));
  document.querySelector('#navigation').innerHTML = sections.map((id, i) => `<a href="#${id}">${t.nav[i]}</a>`).join('');
  document.querySelector('#navigation').setAttribute('aria-label', language === 'pt' ? 'Seções' : 'Sections');
  document.querySelector('#close-dialog').textContent = t.close;
  main.innerHTML = `<div class="wrap" id="top">
    <section class="hero reveal" aria-labelledby="hero-title"><div><p class="eyebrow">${t.eyebrow}</p><h1 id="hero-title">${t.title}</h1><p class="lead">${t.intro}</p><div class="actions"><a class="button accent" href="#revenue">${t.explore}</a><a class="button" href="${repository}" target="_blank" rel="noopener noreferrer">${t.code}</a></div><p class="byline">${t.by}</p></div>
    <aside class="glass hero-panel"><div class="panel-meta"><span>${t.panelTitle}</span><span class="pill">${t.days}</span></div><div class="hero-value"><small>R$</small>${money(models[0].mae)}</div><p>${t.panelLabel}</p>${models.map(m=>`<div class="mini-row"><div class="mini-label"><span>${m[language]}</span><span>${money(m.mae)}</span></div><div class="track" aria-hidden="true"><div class="fill ${m.color}" style="--width:${m.mae/100}%"></div></div></div>`).join('')}<div class="panel-foot">${t.panelFoot}</div></aside></section>
    <div class="tech-strip"><span>${t.stack}</span><span>Python</span><span>SQL / BigQuery</span><span>R</span><span>scikit-learn</span><span>Prophet</span><span>GCP</span></div>
    <section class="section" id="revenue">${heading(t.revenueLabel,t.revenueTitle,t.revenueIntro)}<p class="note">${t.graphLanguage}</p><div class="grid">${chartCard(t.charts[0])}${chartCard(t.charts[1])}</div><p class="note">${t.revenueNote}</p><div class="category-layout">${chartCard(t.charts[2])}<aside class="glass insight-panel"><span class="inline-tag">${t.insightLabel}</span><h3>${t.insightTitle}</h3><p>${t.insightText}</p><p class="insight-rule">${t.insightDetail}</p></aside></div></section>
    <section class="section" id="customers">${heading(t.customerLabel,t.customerTitle,t.customerIntro)}<div class="grid">${chartCard(t.charts[3])}${chartCard(t.charts[4])}</div><article class="glass logistics"><div><p class="eyebrow">SP / RJ</p><h3>${t.logisticsTitle}</h3><p>${t.logisticsText}</p></div><div><div class="state-row"><span>RJ</span><div class="track" aria-hidden="true"><div class="fill orange" style="--width:89.8%"></div></div><strong>${language==='pt'?'13,47':'13.47'}%</strong></div><div class="state-row"><span>SP</span><div class="track" aria-hidden="true"><div class="fill" style="--width:39.2667%"></div></div><strong>${language==='pt'?'5,89':'5.89'}%</strong></div><p class="state-caption">${t.logisticsSource}</p></div></article></section>
    <section class="section" id="forecasting">${heading(t.forecastLabel,t.forecastTitle,t.forecastIntro)}<article class="glass chart-card forecast-card"><div class="card-head"><div><h3>${t.forecastChartTitle}</h3><p>${t.forecastChartDesc}</p></div><span class="pill">${t.days}</span></div>${chartButton('comparativo_modelos.png',t.forecastChartTitle,t.forecastChartDesc,t.forecastCaption)}<div class="card-foot"><p>${t.forecastCaption}</p><span class="source">ml_sales_prediction.py · ${t.original}</span></div></article><article class="glass model-area"><div class="model-header"><h3>${t.metricsTitle}</h3><div class="metric-switch" role="group" aria-label="${language==='pt'?'Métrica de erro':'Error metric'}"><button type="button" data-metric="mae" aria-pressed="${metric==='mae'}">MAE</button><button type="button" data-metric="rmse" aria-pressed="${metric==='rmse'}">RMSE</button></div></div><div class="model-grid" id="model-values" aria-live="polite"></div><p class="metric-description" id="metric-description"></p></article><aside class="comparison-warning"><h3>${t.warningTitle}</h3><p>${t.warning}</p></aside></section>
    <section class="section" id="method">${heading(t.methodLabel,t.methodTitle,t.methodIntro)}<div class="method-grid">${t.methods.map((m,i)=>`<article class="glass method-card"><div class="method-number">0${i+1}</div><h3>${m[0]}</h3><p>${m[1]}</p></article>`).join('')}</div><details class="glass details"><summary>${t.limitsTitle}</summary><p>${t.limits}</p></details></section>
    <section class="glass closing"><div><h2>${t.closingTitle}</h2><p>${t.closingText}</p></div>${codeLink(t.code)}</section></div>`;
  document.querySelector('#footer').innerHTML = `<span>${t.footer}</span><span>${t.footerRight}</span>`;
  renderMetric();
}
function renderMetric() {
  document.querySelector('#model-values').innerHTML = models.map(m => `<div class="model-item"><div class="model-name">${m[language]}</div><div class="model-value"><small>R$</small> ${money(m[metric])}</div><div class="track" aria-hidden="true"><div class="fill ${m.color}" style="--width:${m[metric]/120}%"></div></div></div>`).join('');
  document.querySelector('#metric-description').textContent = content[language][metric];
  document.querySelectorAll('[data-metric]').forEach(b => b.setAttribute('aria-pressed', String(b.dataset.metric === metric)));
}
document.querySelectorAll('[data-lang]').forEach(button => button.addEventListener('click', () => {
  language = button.dataset.lang;
  try { localStorage.setItem('olist-language',language); } catch {}
  render();
}));
main.addEventListener('click', event => {
  const metricButton = event.target.closest('[data-metric]');
  if (metricButton) { metric = metricButton.dataset.metric; renderMetric(); return; }
  const button = event.target.closest('[data-image]');
  if (!button) return;
  const img = document.querySelector('#dialog-image');
  img.src = `assets/${button.dataset.image}`;
  img.alt = button.querySelector('img').alt;
  document.querySelector('#dialog-title').textContent = button.dataset.title;
  document.querySelector('#dialog-caption').textContent = button.dataset.caption;
  dialog.showModal();
  document.body.style.overflow = 'hidden';
});
document.querySelector('#close-dialog').addEventListener('click',()=>dialog.close());
dialog.addEventListener('click',e=>{if(e.target===dialog){const r=dialog.getBoundingClientRect();if(e.clientX<r.left||e.clientX>r.right||e.clientY<r.top||e.clientY>r.bottom)dialog.close();}});
dialog.addEventListener('close',()=>{document.body.style.overflow='';});
render();
