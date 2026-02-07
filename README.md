# Inje-o-de-depend-ncias
Atividade avaliativa do professor Anthony
# FastAPI – Exemplo de Dependências

Este repositório demonstra, de forma simples, como utilizar **dependências no FastAPI**

🔹 O que é uma dependência no FastAPI?

Uma **dependência** é uma função que o FastAPI executa **antes** de chamar uma rota.
Ela é usada para:

- Autenticação e autorização
- Validação de dados
- Reuso de lógica comum
- Controle de acesso a rotas

Dependências podem:
- Retornar valores para a rota
- Lançar exceções (ex: HTTP 401)
- Ser usadas diretamente na assinatura da rota ou no decorator

---

## ▶️ Como rodar o projeto

1. Instale as dependências:

```bash
pip install fastapi uvicorn
