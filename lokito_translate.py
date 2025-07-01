
import openai
import json

with open('agent_config.json') as f:
    config = json.load(f)

openai.api_key = config["openai_api_key"]

idiomas = {
    "pt": "Português",
    "en": "Inglês",
    "es": "Espanhol",
    "fr": "Francês",
    "de": "Alemão"
}

def traduzir(texto):
    for cod, idioma in idiomas.items():
        prompt = f"Traduza este texto para {idioma} e mantenha o impacto viral:\n{texto}"
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": config["system_prompt"]},
                {"role": "user", "content": prompt}
            ]
        )
        traducao = resposta.choices[0].message["content"]
        print(f"[{idioma}] {traducao}\n")

if __name__ == "__main__":
    exemplo = "Esse site será derrubado. Somente quem clicar agora terá acesso ao chip secreto."
    traduzir(exemplo)
