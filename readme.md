# 📧 Email Classifier AI

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions&logoColor=white)
![Render](https://img.shields.io/badge/Deploy-Render-46E3B7?style=for-the-badge&logo=render&logoColor=white)

**Aplicação web com IA para classificação automática de emails corporativos e geração de respostas inteligentes.**

[🚀 Acessar aplicação](https://autou-x0vv.onrender.com) · [📋 Ver testes](#-testes) · [🐳 Rodar com Docker](#-rodando-com-docker)

</div>

---

## 📌 Sobre o projeto

O **Email Classifier AI** automatiza a leitura e classificação de emails corporativos do setor financeiro, eliminando a necessidade de triagem manual. A aplicação analisa o conteúdo de cada email e:

- 🏷️ **Classifica** o email como **Produtivo** ou **Improdutivo**
- 💬 **Gera uma resposta automática** adequada ao contexto
- 📊 **Exibe um índice de confiança** da classificação
- 📁 **Suporta upload** de arquivos `.txt` e `.pdf`

---

## ✨ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| 📝 Entrada por texto | Cole o conteúdo do email diretamente no formulário |
| 📁 Upload de arquivo | Envie arquivos `.txt` ou `.pdf` para processamento |
| 🤖 Classificação com IA | Modelo LLaMA 3.3 70B via Groq API |
| 💬 Resposta automática | Sugestão de resposta gerada pela IA |
| 📊 Índice de confiança | Percentual de certeza da classificação |
| 📋 Copiar resposta | Botão para copiar a resposta sugerida |
| 🌙 Interface dark | Design moderno com tema escuro |

---

## 🗂️ Estrutura do projeto

```
email-classifier/
├── 📂 backend/
│   ├── main.py               # Servidor FastAPI e rotas da API
│   ├── classifier.py         # Integração com a IA (Groq API)
│   ├── utils.py              # Leitura de arquivos .txt e .pdf
│   └── tests/
│       ├── __init__.py
│       └── test_classifier.py  # Testes automatizados com pytest
│
├── 📂 frontend/
│   ├── index.html            # Interface web
│   └── style.css             # Estilização com tema escuro
│
├── 📂 .github/
│   └── workflows/
│       └── ci.yml            # Pipeline CI/CD com GitHub Actions
│
├── .env                      # Variáveis de ambiente (não versionado)
├── .gitignore
├── Dockerfile                # Configuração do container
├── docker-compose.yml        # Orquestração local
├── requirements.txt          # Dependências Python
└── README.md
```

---

## 🛠️ Tecnologias utilizadas

### Backend
- **Python 3.10** — linguagem principal
- **FastAPI** — framework web moderno e de alta performance
- **Uvicorn** — servidor ASGI
- **Groq API + LLaMA 3.3 70B** — modelo de linguagem para classificação e geração de respostas
- **PyPDF2** — extração de texto de arquivos PDF
- **python-dotenv** — gerenciamento de variáveis de ambiente

### Frontend
- **HTML5 + CSS3** — interface responsiva com tema escuro
- **JavaScript** — consumo da API e interatividade

### Infraestrutura
- **Docker + Docker Compose** — containerização da aplicação
- **GitHub Actions** — CI/CD automatizado
- **Render** — hospedagem na nuvem (free tier)

---

## 🚀 Como rodar localmente

### Pré-requisitos

- Python 3.10+
- Docker Desktop
- Git
- Chave de API do [Groq](https://console.groq.com)

### Configuração do ambiente

**1. Clone o repositório:**
```bash
git clone https://github.com/Defendi22/AutoU
cd email-classifier
```

**2. Crie o arquivo `.env` na raiz do projeto:**
```env
GROQ_API_KEY=sua_chave_aqui
```

---

### 🐳 Rodando com Docker

```bash
docker-compose up
```

Acesse: **http://localhost:8000**

---

### 🐍 Rodando sem Docker

**1. Crie e ative o ambiente virtual:**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

**2. Instale as dependências:**
```bash
pip install -r requirements.txt
```

**3. Inicie o servidor:**
```bash
cd backend
uvicorn main:app --reload
```

Acesse: **http://localhost:8000**

---

## 🧪 Testes

Os testes cobrem os principais cenários da API usando `pytest` com mocks para não depender da API externa.

```bash
cd backend
pytest tests/ -v
```

### Casos de teste

| Teste | Descrição |
|---|---|
| `test_health_check` | Verifica se o servidor está respondendo |
| `test_classify_produtivo` | Classifica corretamente email produtivo |
| `test_classify_improdutivo` | Classifica corretamente email improdutivo |
| `test_classify_sem_conteudo` | Retorna erro 400 sem conteúdo |
| `test_classify_texto_vazio` | Retorna erro 400 para texto vazio |

---

## 🔄 CI/CD Pipeline

A cada `git push` na branch `main`, o GitHub Actions executa automaticamente:

```
Push para main
     │
     ▼
┌─────────────┐
│  Roda testes │  ← pytest tests/ -v
└──────┬──────┘
       │ passou
       ▼
┌──────────────┐
│ Deploy Render │  ← trigger automático via webhook
└──────────────┘
```

---

## 🌐 API

### `GET /health`
Verifica se o servidor está online.

**Resposta:**
```json
{ "status": "ok" }
```

---

### `POST /classify`
Classifica o email e retorna a análise.

**Parâmetros (form-data):**
| Campo | Tipo | Descrição |
|---|---|---|
| `email_text` | string | Texto do email (opcional) |
| `file` | file | Arquivo `.txt` ou `.pdf` (opcional) |

**Resposta:**
```json
{
  "categoria": "Produtivo",
  "confianca": 90,
  "motivo": "Solicitação de suporte técnico",
  "resposta_sugerida": "Prezado, agradecemos seu contato..."
}
```

---

## 📂 Categorias de classificação

| Categoria | Descrição | Exemplos |
|---|---|---|
| ✅ **Produtivo** | Requer ação ou resposta | Suporte técnico, dúvidas, status de casos |
| ⏸️ **Improdutivo** | Não requer ação imediata | Felicitações, agradecimentos, mensagens sociais |

---

## 🔐 Variáveis de ambiente

| Variável | Descrição |
|---|---|
| `GROQ_API_KEY` | Chave de API do Groq (obrigatória) |

> ⚠️ Nunca versione o arquivo `.env`. Ele já está no `.gitignore`.

---

## 📄 Licença

Este projeto foi desenvolvido como desafio técnico. Espero que gostem 😀

---

<div align="center">
Desenvolvido por <strong>Fernando</strong>
</div>