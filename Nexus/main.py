
"""
NEXUS AI
Plataforma modular de Inteligência Artificial
Primeira versão: 0.1.0
"""

# Identidade do projeto
NOME = "NEXUS AI"
VERSAO = "0.1.0"


def apresentar():
    """Apresenta nossa inteligência artificial."""
    print(f"{NOME} - Versão {VERSAO}")
    print("Sistema inicializado com sucesso!")


def carregar_modelo(modelo_id="distilgpt2"):
    """
    Carrega um modelo de linguagem pré-treinado.
    A biblioteca Transformers será necessária.
    """
    try:
        from transformers import pipeline

        modelo = pipeline(
            "text-generation",
            model=modelo_id
        )

        return modelo

    except ImportError:
        print("Biblioteca Transformers não instalada.")
        return None

    except Exception as erro:
        print(f"Erro ao carregar modelo: {erro}")
        return None


def gerar_resposta(modelo, pergunta):
    """Gera uma resposta utilizando o modelo de linguagem."""

    if modelo is None:
        return "O modelo ainda não foi carregado."

    resultado = modelo(
        pergunta,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )

    return resultado[0]["generated_text"]


# Inicialização do sistema
if __name__ == "__main__":
    apresentar()