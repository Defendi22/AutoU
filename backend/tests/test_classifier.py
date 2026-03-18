import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_classify_produtivo():
    mock_result = {
        "categoria": "Produtivo",
        "confianca": 95,
        "motivo": "Solicitação de suporte técnico",
        "resposta_sugerida": "Prezado, iremos analisar sua solicitação."
    }
    with patch("main.classify_email", return_value=mock_result):
        response = client.post(
            "/classify",
            data={"email_text": "Preciso de suporte técnico urgente."}
        )
    assert response.status_code == 200
    assert response.json()["categoria"] == "Produtivo"
    assert response.json()["confianca"] == 95

def test_classify_improdutivo():
    mock_result = {
        "categoria": "Improdutivo",
        "confianca": 90,
        "motivo": "Mensagem de felicitação",
        "resposta_sugerida": "Obrigado pela mensagem!"
    }
    with patch("main.classify_email", return_value=mock_result):
        response = client.post(
            "/classify",
            data={"email_text": "Feliz Natal a todos!"}
        )
    assert response.status_code == 200
    assert response.json()["categoria"] == "Improdutivo"

def test_classify_sem_conteudo():
    response = client.post("/classify", data={})
    assert response.status_code == 400

def test_classify_texto_vazio():
    response = client.post("/classify", data={"email_text": "   "})
    assert response.status_code == 400