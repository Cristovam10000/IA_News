import os
import warnings
import asyncio
from datetime import date
from google import genai
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

warnings.filterwarnings("ignore")
API_IA = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=API_IA)

async def call_agent(agent, message_text: str) -> str:
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners   import Runner
    from google.genai         import types

    session_service = InMemorySessionService()
    await session_service.create_session(
        app_name=agent.name,
        user_id="user1",
        session_id="session1"
    )
    runner = Runner(agent=agent, app_name=agent.name, session_service=session_service)
    content = types.Content(role="user", parts=[types.Part(text=message_text)])
    resposta = ""
    async for event in runner.run_async(
        user_id="user1", session_id="session1", new_message=content
    ):
        if event.is_final_response():
            for p in event.content.parts:
                if p.text:
                    resposta += p.text + "\n"
    return resposta

# --- Agente 1: Buscador de Notícias Globais ---
def agente_buscador(topico, data_de_hoje):
    from google.adk.agents import Agent
    from google.adk.tools  import google_search

    agent = Agent(
        name="agente_buscador",
        model="gemini-2.0-flash",
        description="busca as últimas notícias globais",
        tools=[google_search],
        instruction=(
            "Você é um assistente de pesquisa global. Use google_search "
            "para coletar até 5 temas ou eventos internacionais mais comentados no último mês, "
            "considerando número de fontes e grau de repercussão."
        )
    )
    prompt = f"Tópico: {topico}\nData: {data_de_hoje}"
    return agent, prompt

# --- Agente 2: Planejador de Conteúdo ---
def agente_planejador(topico, temas):
    from google.adk.agents import Agent
    from google.adk.tools  import google_search

    agent = Agent(
        name="agente_planejador",
        model="gemini-2.0-flash",
        description="planeja o conteúdo jornalístico",
        tools=[google_search],
        instruction=(
            "Você é um planejador de redação jornalística. A partir dos temas coletados, "
            "use google_search para aprofundar dados e estruturar um plano de reportagem: "
            "liste pontos-chave de cada tema e selecione três mais impactantes."
        )
    )
    prompt = f"Tópico: {topico}\nTemas identificados:\n{temas}"
    return agent, prompt

# --- Agente 3: Redator do Jornal ---
def agente_redator(topico, plano):
    from google.adk.agents import Agent

    agent = Agent(
        name="agente_redator",
        model="gemini-2.0-flash",
        description="redige as matérias do jornal",
        instruction=(
            "Você é um redator de jornal profissional. Com base no plano, escreva três matérias completas "
            "em Markdown, cada uma com:"
                "\n# Título da Manchete\n"                "\n*título em itálico*\n"                "\nTexto corrido em parágrafos, sem rótulos como 'Subtítulo:' ou 'Texto:'.\n"                "Use '---' como separador entre as matérias."
        )
    )
    prompt = f"Tópico: {topico}\nPlano de Reportagem:\n{plano}"
    return agent, prompt

# --- Agente 4: Revisor de Qualidade ---
def agente_revisor(topico, rascunho):
    from google.adk.agents import Agent

    agent = Agent(
        name="agente_revisor",
        model="gemini-2.0-flash",
        description="revê clareza e formatação Markdown",
        instruction=(
            "Você é um editor meticuloso. Revise o rascunho em Markdown garantindo:"
               "\n- Títulos com '#' no início da linha"
                "\n- Subtítulos em itálico (envoltos em '*')"
                "\n- Separadores '---' entre matérias"
                "\n- Parágrafos limpos, sem rótulos extras."
                "\nSe necessário, ajuste para melhorar a leitura e a consistência."
        )
    )
    prompt = f"Tópico: {topico}\nRascunho:{rascunho}"
    return agent, prompt

# --- Função principal ---
async def gerar_jornal(topico:str) -> str:
    data_de_hoje = date.today().strftime("%d/%m/%Y")
    

    print("🚀 Iniciando o IA Jornal")
    print(f"Hoje em: {topico}\n")

    buscador, prompt1 = agente_buscador(topico, data_de_hoje)
    temas = await call_agent(buscador, prompt1)

    planejador, prompt2 = agente_planejador(topico, temas)
    plano = await call_agent(planejador, prompt2)

    redator, prompt3 = agente_redator(topico, plano)
    rascunho = await call_agent(redator, prompt3)

    revisor, prompt4 = agente_revisor(topico, rascunho)
    review = await call_agent(revisor, prompt4)

    return review


# ====== FastAPI App ======

app = FastAPI(title="IA Jornal API")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class journalResponse(BaseModel):
    markdown: str

@app.get("/jornal", response_model=journalResponse)
async def get_jornal(topic: str = "principais noticias do mundo"):
    try:
        content = await gerar_jornal(topic)
        return journalResponse(markdown=content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))