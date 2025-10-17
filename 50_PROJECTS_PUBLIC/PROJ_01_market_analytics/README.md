# Projeto 1: Análise de Market Basket

## Resumo Executivo

Este projeto analisa um dataset de transações de varejo para identificar associações de produtos frequentemente comprados juntos (market basket analysis). Usando o algoritmo Apriori, descobrimos regras de associação que podem ser usadas para otimizar o layout da loja, promoções e sistemas de recomendação. O resultado principal é um conjunto de regras acionáveis, como "quem compra pão também tende a comprar manteiga".

## Contexto

Entender o comportamento de compra do cliente é crucial para o varejo. A análise de cesta de compras ajuda a descobrir padrões de compra, permitindo que as empresas tomem decisões baseadas em dados para aumentar as vendas e a satisfação do cliente.

## Dados

*   **Origem:** Dataset sintético de transações de varejo. Para um exemplo real, você pode usar o [Online Retail Data Set](https://archive.ics.uci.edu/ml/datasets/Online+Retail) do UCI Machine Learning Repository.
*   **Licença:** O dataset de exemplo é de domínio público. Verifique a licença para datasets reais.
*   **Descrição:** O dataset contém transações, onde cada transação é uma lista de itens comprados.

## Metodologia

### Etapas de Pré-processamento

1.  Carregamento dos dados de transação.
2.  Transformação dos dados para o formato de lista de listas, onde cada lista interna representa uma transação.
3.  One-hot encoding das transações para criar uma matriz de itens por transação.

### Modelo/Algoritmo

Foi utilizado o algoritmo **Apriori** para extrair conjuntos de itens frequentes. A partir desses conjuntos, geramos regras de associação com métricas de **suporte, confiança e lift**.

*   **Suporte:** Frequência do conjunto de itens no dataset.
*   **Confiança:** Probabilidade de comprar o item Y, dado que o item X foi comprado.
*   **Lift:** Aumento na probabilidade de comprar Y, dado X. Um lift > 1 indica uma associação positiva.

### Resultados

| Regra | Suporte | Confiança | Lift |
| :--- | :--- | :--- | :--- |
| {Pão} -> {Manteiga} | 0.15 | 0.65 | 2.1 |
| {Leite} -> {Café} | 0.12 | 0.50 | 1.8 |

As regras com lift > 1.5 foram consideradas significativas.

## Como Reproduzir

1.  **Clone o repositório e instale as dependências:**
    ```bash
    git clone [URL_DO_REPOSITORIO]
    cd data-ml-portfolio
    ./setup.sh 
    ```
2.  **Execute o notebook:**
    ```bash
    jupyter notebook 50_PROJECTS_PUBLIC/PROJ_01_market_analytics/notebook.ipynb
    ```

## Deploy

A aplicação interativa para este projeto está disponível e pode ser executada localmente. Veja as instruções no link abaixo:

*   [Link para o Deploy](./deploy/README.md)
