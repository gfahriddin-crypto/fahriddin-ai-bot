import telebot
from openai import OpenAI
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = OpenAI(api_key=OPENAI_API_KEY)

SYSTEM_PROMPT = "Sen Fahriddinsan. Oddiy, samimiy, erkakcha gaplash."

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_text = message.text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_text}
        ]
    )

    answer = response.choices[0].message.content
    bot.reply_to(message, answer)

print("AI bot ishga tushdi...")
bot.infinity_polling()
