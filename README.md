# IA Jornal

Projeto full-stack que integra **FastAPI + Google GenAI** no back-end e **React + Vite** no front-end para gerar, via pipeline de agentes, um jornal em **Markdown** contendo as principais notícias globais (ou de um tópico escolhido pelo usuário).

---

## 📋 Sumário

- [Sobre](#sobre)  
- [Funcionalidades](#funcionalidades)  
- [Tecnologias](#tecnologias)  
- [Pré-requisitos](#pré-requisitos)  
- [Instalação](#instalação)  
  - [Backend](#backend)  
  - [Frontend](#frontend)  
- [Como executar](#como-executar)  
- [Estrutura de Pastas](#estrutura-de-pastas)  
- [Uso](#uso)  
- [Agradecimentos](#agradecimentos)  
- [Licença](#licença)

---

## Sobre

### Backend 🔧  
- **FastAPI** serve a rota `GET /jornal?topic=<tópico>`  
- Pipeline de **4 agentes** Gemini (`google-genai`):  
  1. ***Buscador* —** coleta temas recentes via Google Search  
  2. ***Planejador* —** define pontos-chave  
  3. ***Redator* —** escreve matérias em Markdown  
  4. ***Revisor* —** garante clareza e formatação  
- Responde com JSON `{ "markdown": "…" }`.

### Frontend 🎨  
- **React + Vite**  
- Campo para escolher tópico (padrão: “principais notícias do mundo”).  
- Faz *fetch* na rota `/jornal`, recebe Markdown e converte em HTML com **react-markdown**.  
- Componentes separados em `Button`, `TopicSelector`, `News`.

---

## Funcionalidades

- Busca de notícias por tópico em tempo real  
- Geração automática de conteúdo jornalístico (IA)  
- Markdown convertido em HTML responsivo  
- CORS habilitado → integração front/back sem dor de cabeça  

---

## Tecnologias

| Camada  | Techs |
|---------|-------|
| **Back**| Python 3.10+, FastAPI, Uvicorn, google-genai (Gemini API), Pydantic |
| **Front**| Node.js, Vite, React, react-markdown |

---

## Pré-requisitos

- **Git**  
- **Python 3.10+**  
- **Node.js** 16+ e **npm**  
- Chave da **Google GenAI** → variável `GOOGLE_API_KEY`

---

## Instalação

### Backend

```bash
# 1 · Clone o repo
git clone https://github.com/SEU_USUARIO/IA-Jornal.git
cd IA-Jornal

# 2 · Crie & ative venv
python -m venv venv
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3 · Instale dependências
pip install fastapi uvicorn google-genai pydantic

# 4 · Defina a API key
# macOS / Linux
export GOOGLE_API_KEY="SUA_CHAVE_AQUI"
# Windows CMD
set GOOGLE_API_KEY="SUA_CHAVE_AQUI"
# A partir da raiz 
cd meu-app
# 1. Instale as dependências
npm install
# 2.raiz do projeto
uvicorn app:app --reload
# 3. na pasta do frontend
npm run dev
````
### A gradecimentos
Obrigado à Alura pela Imersão IA 3ª Edição, que me deu toda a base necessária para a construção deste backend!
