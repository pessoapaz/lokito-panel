
from flask import Flask, request, render_template
import openai
import json

app = Flask(__name__)

# Inicializa estado da missão
estado_missao = {
    "produto": "",
    "publico": "",
    "link": "",
    "modo": "",
    "ativo": False
}

# Carrega API da OpenAI
with open('agent_config.json', 'r') as f:
    config = json.load(f)

openai.api_key = config["openai_api_key"]

def gerar_resposta(prompt):
    resposta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": config["system_prompt"]},
            {"role": "user", "content": prompt}
        ]
    )
    return resposta.choices[0].message["content"]

@app.route("/", methods=["GET", "POST"])
def index():
    resposta = ""
    if request.method == "POST":
        comando = request.form["comando"]
        resposta = interpretar_comando(comando)
    return render_template("index.html", resposta=resposta, estado=estado_missao)

def interpretar_comando(txt):
    if txt.startswith("/divulgar"):
        estado_missao["ativo"] = True
        return "✅ Campanha iniciada. Use /produto, /publico, /link e /modo para definir os detalhes."

    elif txt.startswith("/pausar"):
        estado_missao["ativo"] = False
        return "⏸️ Campanha pausada."

    elif txt.startswith("/produto"):
        estado_missao["produto"] = txt.replace("/produto", "").strip()
        return f"📦 Produto definido: {estado_missao['produto']}"

    elif txt.startswith("/publico"):
        estado_missao["publico"] = txt.replace("/publico", "").strip()
        return f"🎯 Público definido: {estado_missao['publico']}"

    elif txt.startswith("/link"):
        estado_missao["link"] = txt.replace("/link", "").strip()
        return f"🔗 Link definido: {estado_missao['link']}"

    elif txt.startswith("/modo"):
        estado_missao["modo"] = txt.replace("/modo", "").strip()
        return f"🧠 Modo ativado: {estado_missao['modo']}"

    elif txt.startswith("/status"):
        return f"📊 STATUS ATUAL:\nProduto: {estado_missao['produto']}\nPúblico: {estado_missao['publico']}\nLink: {estado_missao['link']}\nModo: {estado_missao['modo']}\nAtivo: {estado_missao['ativo']}"

    elif txt.startswith("/gerar"):
        prompt = f"Crie uma mensagem para divulgar '{estado_missao['produto']}' para o público '{estado_missao['publico']}' usando o estilo '{estado_missao['modo']}'. Link: {estado_missao['link']}"
        return gerar_resposta(prompt)

    else:
        return "❓ Comando não reconhecido. Use /divulgar, /produto, /publico, /link, /modo, /gerar ou /status."

if __name__ == "__main__":
    app.run(debug=True)
