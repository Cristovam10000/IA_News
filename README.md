# IA Jornal API

Uma API em **FastAPI** que utiliza agentes do Google GenAI (Gemini) para gerar automaticamente um "jornal" com as principais notícias do mundo em formato Markdown. O conteúdo é orquestrado por quatro agentes:

1. **Buscador**: coleta temas e eventos internacionais relevantes.
2. **Planejador**: aprofunda dados e estrutura um plano de reportagem.
3. **Redator**: redige três matérias completas em Markdown.
4. **Revisor**: garante formatação e clareza no resultado final.

O endpoint `/jornal` retorna um JSON com o Markdown pronto, que pode ser renderizado em qualquer front-end (por exemplo, React).

---

## Funcionalidades

* Busca e seleção dos temas mais comentados no último mês.
* Produção de matérias estruturadas em Markdown, com títulos, subtítulos em itálico e separadores `---`.
* Pipeline assíncrono de agentes Gemini (gemini-2.0-flash).
* Endpoint RESTful com validação e documentação automática (Swagger UI).
* CORS configurado para permitir conexões de front-ends.

---

## Pré-requisitos

* Python 3.9 ou superior
* Node.js (v16+) e npm/yarn (opcional, para front-end React)
* Conta e API key do Google GenAI (configurada na variável `GOOGLE_API_KEY`)

---

## Instalação e Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/SEU_USUARIO/ia-jornal-api.git
   cd ia-jornal-api
   ```

2. Crie um ambiente virtual e ative-o:

   * **Linux/macOS**:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   * **Windows**:

     ```powershell
     python -m venv venv
     venv\Scripts\activate
     ```

3. Instale as dependências:

   ```bash
   pip install fastapi uvicorn google-genai
   ```

4. Defina sua chave de API do Google GenAI:

   * **Linux/macOS**:

     ```bash
     export GOOGLE_API_KEY="SUA_CHAVE_AQUI"
     ```
   * **Windows (PowerShell)**:

     ```powershell
     $Env:GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
     ```

---

## Executando a API

Inicie o servidor de desenvolvimento com recarga automática:

```bash
uvicorn app:app --reload
```

* A API ficará disponível em: `http://127.0.0.1:8000`
* Endpoint principal: `GET /jornal`
* Documentação interativa: `http://127.0.0.1:8000/docs`

---


