import json
import pickle

def salvar_dados_json(dados, caminho="data/pedidos.json"):
    """Salva os dados em um arquivo JSON."""
    try:
        with open(caminho, "w") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)
        print("Dados salvos em JSON com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar dados em JSON: {e}")

def carregar_dados_json(caminho="data/pedidos.json"):
    """Carrega os dados de um arquivo JSON."""
    try:
        with open(caminho, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Arquivo JSON não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao carregar dados de JSON: {e}")
        return []

def salvar_dados_binario(dados, caminho="data/pedidos.pkl"):
    """Salva os dados em um arquivo binário (pickle)."""
    try:
        with open(caminho, "wb") as f:
            pickle.dump(dados, f)
        print("Dados salvos em binário com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar dados em binário: {e}")

def carregar_dados_binario(caminho="data/pedidos.pkl"):
    """Carrega os dados de um arquivo binário (pickle)."""
    try:
        with open(caminho, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        print("Arquivo binário não encontrado.")
        return []
    except Exception as e:
        print(f"Erro ao carregar dados de binário: {e}")
        return []



