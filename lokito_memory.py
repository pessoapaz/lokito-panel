
import json
from datetime import datetime

MEM_FILE = "lokito_memoria.json"

def salvar_campanha(produto, publico, link, modo, mensagem):
    try:
        with open(MEM_FILE, "r") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []

    campanha = {
        "data": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "produto": produto,
        "publico": publico,
        "link": link,
        "modo": modo,
        "mensagem": mensagem
    }

    dados.append(campanha)

    with open(MEM_FILE, "w") as f:
        json.dump(dados, f, indent=4)

def listar_campanhas():
    try:
        with open(MEM_FILE, "r") as f:
            dados = json.load(f)
            for c in dados:
                print(f"[{c['data']}] {c['produto']} para {c['publico']} – {c['modo']}")
                print(f"Mensagem: {c['mensagem']}")
                print("-" * 40)
    except FileNotFoundError:
        print("Nenhuma campanha salva ainda.")

if __name__ == "__main__":
    listar_campanhas()
