# 40_DEPLOYMENT

## Objetivo

Este módulo contém tudo o que é necessário para fazer o deploy dos modelos de Machine Learning, seja como uma API ou como uma aplicação web interativa.

## Estrutura

*   **/api:** Código para a API (FastAPI) que serve o modelo.
    *   **/fastapi_app:** A aplicação FastAPI, pronta para ser dockerizada.
*   **/apps:** Aplicações web para demonstrar o modelo.
    *   **/streamlit_dashboard:** Um dashboard interativo com Streamlit.
*   **/infra:** Código de infraestrutura como código (ex: Terraform).
