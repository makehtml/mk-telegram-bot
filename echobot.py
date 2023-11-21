import asyncio
import logging
import os
import tracemalloc

from dotenv import load_dotenv
from telethon import Button, TelegramClient, events, utils

load_dotenv()

API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_ID = BOT_TOKEN.split(":")[0]

ADMIN = "makehtml"

tracemalloc.start()
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.WARNING)
logger = logging.getLogger(__name__)

bot = TelegramClient(BOT_ID, API_ID, API_HASH)

first_line_buttons = [
    Button.text("🗺 Просто кнопка", single_use=False),
    Button.text("✅ Информация", single_use=False),
]

@bot.on(events.NewMessage(pattern="/start"))
async def start_handler(event: events.NewMessage.Event):
    markup = event.client.build_reply_markup(
        [
            first_line_buttons,
            [Button.text("⚠️ Включить тестирование", single_use=True)],
        ],
    )

    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    await event.respond(f"Привет, {name}!\nЭто бот для Мастер-Класса. Можешь нажать /info что бы посмотреть информацию.")
    await event.respond("Включаем и показываем кнопки...", link_preview=False, buttons=markup)

@bot.on(events.NewMessage(pattern=r"бот (\w+)"))
async def answer(event: events.NewMessage.Event):
    if "время" in event.pattern_match.search(".*время.*"):
        print("Показываю время")

@bot.on(events.NewMessage(pattern="/info"))
@bot.on(events.NewMessage(pattern="(?i).*Информация"))
async def info_handler(event: events.NewMessage.Event):
    await bot.send_message(
        event.chat_id, "Смотрим информацию...",
    )
    sender = await event.get_sender()
    name = utils.get_display_name(sender)
    await bot.send_message(
        event.chat_id,
        f"Регистрация\nID: {sender.id}\nusername: {sender.username}\nname: {name}\nphone: {sender.phone}",
    )
    await send_to_admin(f"Регистрация\nID: {sender.id}\nusername: {sender.username}\nname: {name}\nphone: {sender.phone}")

@bot.on(events.NewMessage(pattern="(?i).*Отключить тестирование"))
async def handle_disable_testing_command(event):
    markup = event.client.build_reply_markup(
        [
            first_line_buttons,
            [Button.text("⚠️ Включить тестирование", single_use=True)],
        ],
    )

    await event.respond("Тестирование отключено", buttons=markup)

@bot.on(events.NewMessage(pattern="(?i).*Включить тестирование"))
async def handle_testing_command(event):
    markup = event.client.build_reply_markup(
        [
            first_line_buttons,
            [
                Button.request_location("📍 Отправить локацию", single_use=True),
                Button.request_phone("📞 Отправить номер телефона", single_use=True),
            ], [
                Button.text("✨ Мои бронирования", single_use=True),
                Button.text("⚠️ Отключить тестирование", single_use=True),
            ],
        ],
    )
    await event.respond("Тестирование включено", buttons=markup)

async def send_to_admin(txt):
    txt = f"[admin] {txt}"
    await bot.send_message(ADMIN, txt)

async def main():
    await bot.start(bot_token=BOT_TOKEN)
    await send_to_admin("Запуск бота")
    await bot.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
