import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
Você é um assistente especializado em classificação de emails corporativos do setor financeiro.

Sua tarefa é analisar o conteúdo do email e retornar EXATAMENTE neste formato JSON:
{
  "categoria": "Produtivo" ou "Improdutivo",
  "confianca": número de 0 a 100,
  "motivo": "explicação curta do motivo da classificação",
  "resposta_sugerida": "resposta automática adequada para enviar ao remetente"
}

Definições:
- Produtivo: emails que requerem ação ou resposta (suporte técnico, dúvidas, status de casos, solicitações)
- Improdutivo: emails que não requerem ação imediata (felicitações, agradecimentos, mensagens sociais)

Retorne APENAS o JSON, sem texto adicional, sem markdown, sem explicações.
"""

def classify_email(email_text: str) -> dict:
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Email para classificar:\n{email_text}"}
        ],
        temperature=0.1
    )

    raw = response.choices[0].message.content.strip()

    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    result = json.loads(raw)
    return result