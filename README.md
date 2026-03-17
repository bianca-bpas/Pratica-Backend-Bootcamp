A ideia a atividade de hoje, é desenvolver uma API simples.

Diferente das atividades anteriores, onde trabalhamos no repositório compartilhado do Bootcamp, agora você devera criar o seu próprio repositório. O objetivo é que você passe pela experiência de iniciar uma aplicação, criar suas rotas e versionar tudo em um repositório novo no seu GitHub.

**O Desafio:**
Você deve desenvolver uma API simples que realize as quatro operações básicas de um **CRUD** (Create, Read, Update, Delete) sobre um tema da sua escolha (ex: um gerenciador de tarefas, um catálogo de filmes, uma pokedex, um controle de estoque, etc.).

**Requisitos:**

- **Tecnologia Livre:** Você pode usar a linguagem e o framework que preferir (Node.js com Express ou NestJS, Python com FastAPI ou Flask, Java com Spring, etc.).
- **Armazenamento:** Não é necessário conectar a um banco de dados. Você pode salvar os dados em uma variável na memória (como um *Array* ou *Lista* no próprio código). Lembre-se que, ao reiniciar o servidor, os dados serão perdidos.
- **Arquitetura Livre:** Não cobraremos padrões de projeto complexos nesta etapa. O foco é fazer funcionar.
- **Mínimo de 4 Rotas:** Sua API deve obrigatoriamente ter rotas para:
    1. **Criar** um novo registro (`POST`).
    2. **Listar** os registros (`GET`).
    3. **Atualizar** um registro existente (`PUT` ou `PATCH`).
    4. **Deletar** um registro (`DELETE`).

---

**Testando e Enviando:**

1. Com o código pronto, abra o terminal, instale as dependências com o comando npm install (caso ainda não tenha feito) e inicie o projeto com npm run dev.
2. Teste suas rotas usando alguma ferramenta como “postman.
3. Com tudo funcionando, suba seu projeto para o repositório criado.
4. Envie o formulário da atividade com o link do seu repositório.