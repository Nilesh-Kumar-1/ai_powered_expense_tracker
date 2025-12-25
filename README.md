# ai_powered_expense_tracker
This repo will contain backend code for ai_powered_expense_tracker application. This project will be completed in phases as described below.

# Roadmap: Expense Tracker Backend (Azure‑Native)

**Phase 1 – Core Backend Foundation**

**Goal:** Build a production‑ready FastAPI backend with clean architecture.

- **Project Setup**
    - Create repo structure (`app/`, `routes/`, `models/`, `services/`, `utils/`).
    - Configure environment management with `.env` locally and **Azure App Configuration** in cloud.
- **Database**
    - Use **Azure Database for PostgreSQL Flexible Server**.
    - Define models: `User`, `BankAccount`, `Label`, `Expense`.
    - Apply migrations with Alembic.
- **Authentication**
    - Start with JWT (short expiry, refresh tokens).
    - Isolate auth logic so you can swap to **Entra ID** later.
- **Expense CRUD**
    - Endpoints: `POST /expenses`, `GET /expenses`, `PUT /expenses/{id}`, `DELETE /expenses/{id}`.
    - Filters: category, date range, bank account.
    - Pagination & sorting.
- **Best Practices**
    - Async everywhere (`async def`).
    - Dependency injection with `Depends`.
    - Logging middleware (structured JSON).
    - Unit + integration tests with `pytest`.
- **Deployment**
- Containerize with Docker.
- Deploy to **Azure App Service** or **Azure Container Apps**.
- Secrets in **Azure Key Vault**.
- CI/CD with GitHub Actions.

**Phase 2 – Document Intelligence Integration**

**Goal:** Automate ingestion of bank statements (PDF → structured expenses).

- **Storage**
    - Create Blob containers: `incoming-statements`, `processed-statements`.
- **Eventing**
    - Configure **Event Grid** to trigger processing when a PDF is uploaded.
- **Document Intelligence**
    - Provision **Azure Document Intelligence**.
    - Use prebuilt “Receipts/Invoices” model or train custom model for bank statements.
- **Pipeline**
    - Endpoint: `POST /statements/upload`.
    - Store PDF in Blob → trigger extraction job.
    - Normalize extracted fields (date, description, amount, balance).
    - Map transactions into `Expense` records.
- **Operations**
- Track extraction confidence scores.
- Deduplicate transactions.
- Update status (`Received → Processing → Completed`).

**Phase 3 – RAG Pipeline with Azure AI**

**Goal:** Enable natural language queries and insights over expenses.

- **Vectorization**
    - Use **Azure OpenAI embeddings API** to embed expense descriptions.
    - Store embeddings in **Azure Cognitive Search** (vector fields).
- **Index Design**
    - Fields: id, user_id, date, amount, description, labels, account.
- **Retrieval**
    - Hybrid search (keyword + vector).
    - Scope queries by user_id and filters (date, category).
- **Generation**
    - Use **Azure OpenAI GPT models** for summarization and Q&A.
    - Prompt includes retrieved expenses as context.
    - Example: “Summarize my food expenses this month.” → returns grounded answer with references.
- **Endpoints**
    - `POST /insights/query` → free‑form Q&A.
    - `POST /insights/summary` → structured summaries.
- **Governance**
- Always ground answers in retrieved data.
- Cache frequent queries.
- Monitor token usage and latency.

**Phase 4 – Enterprise Security (Future)**

**Goal:** Replace JWT with **Microsoft Entra ID**.

- Register app in Entra ID.
- Implement OAuth2/OpenID Connect flow.
- Validate tokens via JWKS.
- Map Entra roles/groups to app roles (Admin/User).

📅 Suggested Timeline

- **Weeks 1–2:** Core backend (Phase 1).
- **Weeks 3–4:** Document Intelligence integration (Phase 2).
- **Weeks 5–6:** RAG pipeline with Cognitive Search + OpenAI (Phase 3).
- **Week 7+:** Entra ID integration (Phase 4).
