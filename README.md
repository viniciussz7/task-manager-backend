# 📝 Task Manager API

API REST para gerenciamento de tarefas com autenticação JWT, desenvolvida em Python, **FastAPI**, **SQLAlchemy** e **SQLite3**.  

---

## 🚀 Descrição
Aplicação permite criar, ler, atualizar e deletar tarefas (CRUD) vinculadas a usuários autenticados. A API inclui:

- Cadastro e login de usuários  
- Autenticação JWT para rotas protegidas  
- CRUD completo de tarefas, vinculadas ao usuário  
- Filtragem básica por limite e offset (paginação simples)  
- Estrutura modular e clara para fácil manutenção  

💡 Este projeto foi desenvolvido com intuito de aprender/estudar FastAPI (criar uma **API REST básica e profissional**.)

---

## 🛠 Tecnologias
- **Python 3.12**  
- **FastAPI**  
- **SQLAlchemy**  
- **SQLite3**  
- **Pydantic**  
- **JWT (jose)**  

---

## ⚡ Instalação e execução
**1. Clone o repositório:**
```bash
git clone <URL_DO_REPOSITORIO>
cd task-manager
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv .venv
source .venv/bin/activate  # Linux / macOS
.venv\Scripts\activate     # Windows
```

**3. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**4. Configure variáveis de ambiente (.env):**
```bash
# ============================
# Application Configuration
# ============================
APP_NAME="Task Manager API"
APP_VERSION="0.1.0"
ENVIRONMENT="development"  # development | production

# ============================
# Security
# ============================
SECRET_KEY="change-me-in-production"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=60

# ============================
# Database
# ============================
# SQLite (default)
DATABASE_URL="sqlite:///./app.db"

# Postgres (exemplo)
# DATABASE_URL="postgresql://user:password@localhost:5432/mydb"
```

**5. Execute a aplicação:**
```bash
uvicorn app.main:app --reload
```

**6. Acesse a documentação interativa:**
```bash
http://127.0.0.1:8000/docs
```

---

## 🖥 Swagger UI

<p align="center">
  <img src="assets/swagger.png" alt="Swagger Docs" width="800"/>
</p>

---

## 🔑 Rotas principais

### 👤 Usuários

- ```POST /users/``` — Registrar usuário

- ```POST /users/login``` — Login e retorno do token

- ```GET /users/me``` — Retorna dados do usuário logado

## ✅ Tarefas

- ```POST /tasks/``` — Criar tarefa

- ```GET /tasks/``` — Listar tarefas (com limit e offset)

- ```GET /tasks/{task_id}``` — Buscar tarefa específica

- ```PUT /tasks/{task_id}``` — Atualizar tarefa

- ```DELETE /tasks/{task_id}``` — Deletar tarefa

Todas as rotas de tarefas exigem autenticação JWT. Use o botão Authorize no Swagger UI.

---

## 📌 Boas práticas implementadas

- Tokens JWT com expiração configurável

- Filtros e ordenação avançada de tarefas (por status, titulo ou data)
  
- Estrutura modular (```routes```, ```schemas```, ```services```, ```models```, ```core```)

- CORS configurado

- Dependências gerenciadas via FastAPI ```Depends```

- Suporte a variáveis de ambiente (.env + .env.example)
  
- Leitura de configurações via pydantic settings
---

## 🌟 Melhorias e próximos passos

Funcionalidades planejadas para evoluções futuras:


- Refresh tokens e expiração configurável para uso real

- Paginação avançada (page + per_page + total pages)

- Boas práticas adicionais para produção: rate limiting, logging, métricas

---

## 🤝 Contribuição

Pull requests são bem-vindos!
Abra issues para sugestões ou melhorias.