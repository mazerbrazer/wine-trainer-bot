import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()


menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📚 Изучение")],
        [KeyboardButton(text="📝 Тест")],
        [KeyboardButton(text="🎓 Экзамен")],
        [KeyboardButton(text="❌ Ошибки")],
        [KeyboardButton(text="📊 Статистика")]
    ],
    resize_keyboard=True
)


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "🍷 <b>Wine Trainer</b>\n\nДобро пожаловать!",
        reply_markup=menu
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())