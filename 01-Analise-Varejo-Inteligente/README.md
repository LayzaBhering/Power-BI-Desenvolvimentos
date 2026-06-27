# 📊 DataPlus: Varejo Inteligente — Dashboard de Performance Comercial

![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![DAX](https://img.shields.io/badge/DAX-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)
![Data_Analytics](https://img.shields.io/badge/Data_Analytics-333333?style=for-the-badge&logo=analytics&logoColor=white)

Este repositório contém a documentação e os fundamentos estratégicos do painel **DataPlus Varejo Inteligente**, um dashboard executivo desenvolvido no Microsoft Power BI para monitoramento analítico de faturamento, volumetria de vendas e comportamento de categorias de produtos ao longo do tempo.

---

## 🎯 Desafio de Negócio & Objetivos Estratégicos

Em cenários comerciais dinâmicos, a liderança executiva necessita de respostas rápidas para tomar decisões de abastecimento, precificação e direcionamento de campanhas de marketing. Este projeto foi desenhado sob a metodologia de **User Experience (UX) focada em Data Analytics**, transformando dados brutos em decisões táticas imediatas.

**Objetivos do Dashboard:**
* **Monitoramento Centralizado:** Consolidar faturamento acumulado, ticket médio (Valor Unitário) e volume de vendas em um único ambiente.
* **Análise Geográfica e de Desempenho Regional:** Identificar gargalos e estados líderes em receita para otimização logística.
* **Visão de Portfólio (Curva ABC):** Avaliar quais categorias e produtos (ex: Eletrônicos, Hardware) sustentam a margem operacional.
* **Análise Temporal:** Acompanhar a sazonalidade e a tendência de quedas ou picos nas vendas (Janeiro a Julho).

---

## 🎨 Design Estratégico & Identidade Visual

O design deste dashboard afasta-se dos relatórios corporativos tradicionais e monótonos, adotando uma abordagem moderna baseada em **Dark Mode (Tema Escuro)** com pontos de atenção de alta performance:

* **Fundo Escuro Premium (`#1E1E24` / Black Sólido):** Reduz a fadiga visual do usuário em longos períodos de análise e faz com que os elementos de dados saltem aos olhos imediatamente.
* **Contraste Neon (Verde Limão e Azul Vibrante):** O uso de verde neon indica de forma cirúrgica os botões de navegação ativos ("Faturamento por Cidade" ou "Faturamento por Categoria"), orientando o fluxo de leitura do usuário. O azul foi estrategicamente aplicado para representar as barras e linhas de dados, mantendo a sobriedade sem perder o apelo analítico.
* **Arquitetura de Informação Limpa:** Ausência de linhas de grade desnecessárias e uso de bordas arredondadas e sutis nos cartões, criando uma interface fluida que lembra softwares modernos de SaaS.

---

## 🖥️ Estrutura das Telas & Visões Analíticas

O relatório possui um **menu lateral dinâmico** que permite alternar a perspectiva do negócio com apenas um clique.

### 1. Visão de Faturamento por Cidade (Visão Macro-Geográfica)

Nesta primeira tela, o foco está na distribuição regional e saúde financeira imediata de Fevereiro.

* **Tabela Matriz de Cidades vs. Categorias:** Apresenta de forma transparente o cruzamento de dados de faturamento. Notamos instantaneamente que grandes capitais como **Rio de Janeiro** (R$ 2.88M), **Curitiba** (R$ 2.85M) e **Salvador** (R$ 2.60M) lideram a geração de receita do período, enquanto São Paulo apresenta uma oportunidade de expansão (R$ 1.28M).
* **Cartões de KPIs Principais:** Destacam os números consolidados de forma imponente na parte superior direita (Quantidade: 580, Faturamento: R$ 16.292.639, Valor Unitário Médio: R$ 28.090,76).
* **Gráfico de Linha de Faturamento por Estado:** Exibe visualmente o declínio do faturamento ordenado do maior estado para o menor (RJ a SP).
* **Gráfico de Pizza (Normal vs. Rápida):** Traz uma métrica operacional crítica onde vemos que 59,74% das entregas/processos operam sob a classificação "Rápida".
* **Ranking de Produtos:** Um gráfico de barras horizontais elenca os campeões de venda, liderados pelo *Laptop Gamer* e *Teclado Mecânico*.

---

### 2. Visão de Faturamento por Categoria (Visão de Portfólio)

Ao acionar o segundo botão do menu lateral, o dashboard reorganiza-se completamente para detalhar a performance do catálogo de produtos.

* **Análise Hierárquica de Categorias (Drill-down):** Abre o detalhamento do faturamento por item, evidenciando o peso de **Acessórios** (R$ 37.59M) e **Eletrônicos** (R$ 49.97M) na composição do faturamento total acumulado de R$ 121.88M.
* **Visão Temporal Consolidada (Gráfico de Barras + Linha):** Exibe a evolução histórica de Janeiro a Julho. Essa estrutura permite diagnosticar um pico em Janeiro (R$ 20.41M), uma estabilização entre Fevereiro e Maio na casa dos R$ 17M-19M, e um sinal de alerta para Julho, que apresenta uma queda acentuada de receita (R$ 12.49M) e volume (396 unidades), demandando ação imediata da equipe de vendas.
* **Gráfico de Rosca Central:** Divide a participação interna de produtos específicos (como *Laptop Gamer*, *Placa de Vídeo* e *Teclado Mecânico*), facilitando a identificação do mix de produtos ideal.

---

## 🛠️ Tecnologias e Técnicas Aplicadas

* **Modelagem de Dados:** Relacionamentos do tipo Star Schema para otimização de performance das medidas.
* **DAX Avançado:** Criação de métricas de faturamento acumulado, médias móveis e tratamento de contextos de filtro.
* **UI/UX para BI:** Design de botões nativos para navegação entre telas, seleção de meses via segmentadores superiores e formatação condicional sutil.

---

## 💡 Principais Insights de Negócio Gerados

1.  **Sinal de Alerta no Fechamento (Julho):** Há uma tendência clara de desaceleração das vendas a partir de Maio, culminando no pior resultado em Julho. Recomenda-se uma campanha promocional para queima de estoque de Hardware e Acessórios.
2.  **Concentração de Receita:** As categorias de Eletrônicos e Acessórios somam juntas a vasta maioria do faturamento da empresa. O foco de marketing deve continuar blindando esses segmentos.
3.  **Anomalia de São Paulo:** Sendo o maior mercado consumidor do país, apresentar o menor faturamento entre as capitais analisadas na visão de fevereiro indica a necessidade urgente de uma revisão da estratégia de vendas local ou ajuste na distribuição de produtos.

---
Documentação desenvolvida para portfólio técnico no GitHub. 🚀
