import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.types.web_app_info import WebAppInfo
import base64
from io import BytesIO
from PIL import Image
import os

API_TOKEN = '5159271198:AAE3uUnrDpNFyTIovPUTSTt8Jxtl6JE2kE0'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['id'])
async def send_welcome(message: types.Message):
    await message.reply(message.from_user.id)

# Обработка команды /start
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    website_button = InlineKeyboardButton("Посетить сайт",
                                          web_app=WebAppInfo(url="https://xaryki.github.io/Third_face_bot/"))
    markup = InlineKeyboardMarkup().add(website_button)
    # Отправляем информацию о новом годе с кнопкой
    await message.reply("🎉 Добро пожаловать в Новогодний бот! 🎊\n"
                        "Получи информацию о Новом Годе и выбери стильную шапку для браузера. "
                        "Нажми на кнопку ниже, чтобы посетить наш сайт и добавить праздничное настроение к своему онлайн-опыту. 🎅🎄\n"
                        "#НовыйГод #Бот", reply_markup=markup, parse_mode='Markdown', disable_web_page_preview=True)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    print(message.text)
    try:
        if message.web_app_data:
            data = message.web_app_data.data
            image_data = base64.b64decode(data.split(',')[1])
            image = Image.open(BytesIO(image_data))
            image_byte_array = BytesIO()
            image.save(image_byte_array, format='PNG')
            image_byte_array.seek(0)
            await bot.send_photo(message.chat.id, photo=image_byte_array, caption="Вот ваше фото:")
    except Exception as e:
        logging.error(f"Произошла ошибка: {e}")


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)