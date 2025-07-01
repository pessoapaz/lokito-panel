
import telebot
import openai
import json

with open('agent_config.json') as f:
    config = json.load(f)

bot = telebot.TeleBot("INSIRA_SEU_TOKEN_AQUI")
openai.api_key = config["openai_api_key"]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🔓 LokitoBot ativo. Envie uma missão no formato:\n/divulgar [produto] para [público]")

@bot.message_handler(func=lambda msg: True)
def responder(msg):
    texto = msg.text
    if texto.startswith("/divulgar"):
        prompt = texto.replace("/divulgar", "").strip()
        prompt_full = f"Crie uma mensagem viral no estilo hacker/psicológico para: {prompt}"
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": config["system_prompt"]},
                {"role": "user", "content": prompt_full}
            ]
        )
        reply = resposta.choices[0].message["content"]
        bot.reply_to(msg, f"💬 Mensagem gerada:\n{reply}")
    else:
        bot.reply_to(msg, "Use o comando /divulgar seguido da missão.")

bot.polling()
