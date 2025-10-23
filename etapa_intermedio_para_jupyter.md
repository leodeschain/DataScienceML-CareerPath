# Guia Intermediário: Corrigindo o Ambiente Jupyter no VS Code

Este guia documenta os passos para resolver problemas de ambiente (kernel) entre o Jupyter Notebook e o VS Code, especificamente para este projeto. O objetivo é forçar o VS Code a usar o ambiente virtual (`.venv`) correto, onde todas as nossas bibliotecas estão instaladas.

## O Problema

Ao tentar executar uma célula no Jupyter Notebook dentro do VS Code, você encontra o erro `ModuleNotFoundError`. Isso acontece porque o VS Code/Jupyter está usando um interpretador Python "global" do seu sistema, em vez do interpretador isolado do nosso projeto localizado na pasta `.venv`.

## Passo 1: Recriar o Ambiente Virtual (Instalação Limpa)

Para garantir que não há arquivos corrompidos, o melhor é começar com um ambiente limpo.

1.  **Feche o VS Code** para liberar quaisquer processos que possam estar usando a pasta do ambiente.
2.  **Abra o Explorador de Arquivos** do Windows.
3.  Navegue até a pasta raiz do projeto: `C:\projects\projetodev\datascienceml\data-ml-portfolio\`
4.  **Delete a pasta `.venv`** manualmente.
5.  **Abra um terminal**. Recomendo o **Git Bash**, pois ele executa scripts `.sh` nativamente no Windows.
6.  No terminal, navegue até a pasta do projeto: `cd C:/projects/projetodev/datascienceml/data-ml-portfolio/`
7.  Execute o script de configuração para recriar o ambiente e reinstalar as dependências:
    ```bash
    bash setup.sh
    ```

Ao final deste passo, você terá uma pasta `.venv` nova e funcional.

## Passo 2: Configurar o VS Code Permanentemente

Esta é a solução definitiva. Vamos criar um arquivo de configuração para que o VS Code **nunca mais** pergunte qual ambiente usar para este projeto.

1.  **Abra o VS Code** na pasta do projeto (`C:\projects\projetodev\datascienceml\data-ml-portfolio\`).
2.  Na raiz do projeto, crie uma nova pasta chamada `.vscode`.
3.  Dentro desta nova pasta `.vscode`, crie um arquivo chamado `settings.json`.
4.  Copie e cole o seguinte conteúdo nesse arquivo `settings.json`:

    ```json
    {
        "python.defaultInterpreterPath": "C:/projects/projetodev/datascienceml/data-ml-portfolio/.venv/Scripts/python.exe"
    }
    ```
    *(Nota: Usamos barras normais `/` no caminho dentro do JSON por compatibilidade).*

## Passo 3: Verificação Final

1.  **Reinicie o VS Code** uma última vez para garantir que ele carregue as novas configurações.
2.  Abra o notebook `20_ANALYTICS/notebooks/01_exploratory_analysis.ipynb`.
3.  Verifique o canto superior direito da tela do notebook. Ele deve mostrar automaticamente o nome do kernel apontando para o ambiente `.venv`.
4.  Execute a primeira célula de código (a de importação). Ela deve funcionar sem nenhum erro.

Com estes passos, o problema de ambiente estará resolvido de forma definitiva para este workspace.
