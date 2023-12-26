from googletrans import Translator
from aiogram import executor, types, Bot, Dispatcher
import logging
from loader import dp

logging.basicConfig(level=logging.INFO)

translator = Translator()

@dp.message_handler()
async def get_data(message: types.Message):
    translation = translator.translate(message.text, dest='en')
    translated_text = translation.text
    await message.reply(translated_text)
