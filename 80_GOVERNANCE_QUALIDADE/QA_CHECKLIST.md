# QA Checklist - Critérios de Qualidade

Antes de um projeto ser movido para a pasta `50_PROJECTS_PUBLIC` e ser considerado "pronto", ele deve atender aos seguintes critérios:

## Documentação
- [ ] **README.md completo:** O README do projeto está preenchido, seguindo o `template_readme.md`?
- [ ] **Instruções claras:** As instruções de como reproduzir o projeto são claras e funcionais?
- [ ] **Comentários no código:** O código complexo está comentado (o "porquê", não o "o quê")?

## Dados
- [ ] **Dados públicos ou anonimizados:** O projeto utiliza apenas dados públicos ou devidamente anonimizados?
- [ ] **Licença de dados verificada:** A licença do dataset foi verificada e permite o uso no projeto?
- [ ] **Fonte dos dados citada:** A origem dos dados está claramente citada no README?

## Código e Ambiente
- [ ] **`requirements.txt` atualizado:** Todas as dependências estão listadas?
- [ ] **`setup.sh` funcional:** O script de setup executa sem erros?
- [ ] **Runtime razoável:** O notebook ou script principal executa em menos de 5 minutos em uma máquina padrão?
- [ ] **Testes implementados:** Existem testes unitários ou de integração para as partes críticas do código?
- [ ] **Testes passando:** Todos os testes (`pytest`) passam com sucesso?
- [ ] **Linting:** O código passa no linter (`flake8`) sem erros críticos?

## Deploy
- [ ] **Link de deploy funcional:** Se houver um deploy (Streamlit, FastAPI), o link está no README e funcionando?
- [ ] **Dockerfile (se aplicável):** O Dockerfile está otimizado e construindo a imagem corretamente?

## Versionamento
- [ ] **Branch de feature:** O desenvolvimento foi feito em uma branch separada e não diretamente na `main`?
- [ ] **Commits semânticos:** As mensagens de commit são claras e descritivas?
