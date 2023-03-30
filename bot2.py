import logging
from aiogram import Bot, Dispatcher, executor, types
import aiogram.utils.markdown as fmt
from aiogram.dispatcher.filters import CommandHelp, CommandStart, Text
from config import BOT_TOKEN
bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

####
import datetime
import pytz

from aiogram.dispatcher import filters

# Задаем временные зоны
sar_tz = pytz.timezone('Europe/Saratov')
mad_tz = pytz.timezone('Europe/Madrid')
mos_tz = pytz.timezone('Europe/Moscow')
kiev_tz = pytz.timezone('Europe/Kiev')
# Получаем текущее время в каждой временной зоне
sar_time = datetime.datetime.now(sar_tz)
mad_time = datetime.datetime.now(mad_tz)
mos_time = datetime.datetime.now(mos_tz)
kiev_time = datetime.datetime.now(kiev_tz)
# Выводим время в каждой временной зоне
Madrid = "Текущее время в Мадриде:", mad_time.strftime("%H:%M:%S")
Moscow = "Текущее время в Москве:", mos_time.strftime("%H:%M:%S")
Kiev = "Текущее время в Киеве:", kiev_time.strftime("%H:%M:%S")
Saratov = "Текущее время в Саратове:", sar_time.strftime("%H:%M:%S")



###


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"privet,{message.from_user.full_name}")

@dp.message_handler(CommandHelp())
async def bot_start(message: types.Message):
    await message.answer(f"{message.from_user.full_name}, добрый вечер! Рад приветствовать тебя в нашей группе, чем могу помочь?")

@dp.message_handler(Text(startswith='Привет'))
async def bot_start(message: types.Message):
    await message.answer(f"И тебе не хворать, {message.from_user.full_name}")

@dp.message_handler(Text(equals='Время'))
async def bot_start(message: types.Message):
    await message.answer(f"{Madrid}\n{Moscow}\n{Kiev}\n{Saratov}")


# обработчик команды /Саша
@dp.message_handler(Text(equals='Фото Саши'))
async def send_photo(message: types.Message):
    # загружаем картинку из файла
    photo = types.InputFile('tg/sasha.jpg')

    # отправляем картинку
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption='Саша в рассвете сил')


# обработчик команды /Марина
@dp.message_handler(Text(equals='Фото Марины'))
async def send_photo(message: types.Message):
    # загружаем картинку из файла
    photo = types.InputFile('tg/Marina.jpg')

    # отправляем картинку
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption='Куплю немножко я картошки ВИАЙПИ')


# обработчик команды /Маша
@dp.message_handler(Text(equals='Фото Маши'))
async def send_photo(message: types.Message):
    # загружаем картинку из файла
    photo = types.InputFile('tg/Masha.jpg')

    # отправляем картинку
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption='МнямМняма')

# обработчик команды /Сережа
@dp.message_handler(Text(equals='Фото Сережи'))
async def send_photo(message: types.Message):
    # загружаем картинку из файла
    photo = types.InputFile('tg/brat.jpg')

    # отправляем картинку
    await bot.send_photo(chat_id=message.chat.id, photo=photo, caption='ЮнайтедСексиБойз')


###############################################


@dp.message_handler(hashtags=['eur', 'usd'])
async def hashtag_example(msg: types.Message):
    await msg.answer('Ееее, деньги 😎')



IMAGE_REGEXP = r'https://.+?\.(jpg|png|jpeg)'


@dp.message_handler(filters.Regexp(IMAGE_REGEXP))
async def regexp_example(msg: types.Message):
    await msg.answer('Похоже на картинку, не так ли?')

@dp.message_handler(commands='change_photo', is_chat_admin=True)
async def chat_admin_example(msg: types.Message):
    await msg.answer('Нет')


@dp.message_handler(content_types=[types.ContentType.ANIMATION])
async def echo_document(message: types.Message):
    await message.reply_animation(message.animation.file_id)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


