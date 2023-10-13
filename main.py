import asyncio
from aiogram import Bot, Dispatcher, F, types as t

import messages
from config import bot_token
import keyboard as kb

bot = Bot(bot_token)
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: t.Message):
    await message.answer('Приветствую вас, создатель', reply_markup=kb.main)


@dp.message(F.text == 'Политех')
async def cmd_tpu(message: t.Message):
    await message.answer('Выберите что хотите сделать', reply_markup=kb.tpu)

@dp.message(F.text == 'Погода ⛅️')
async def cmd_weather(message: t.Message):
    wth = await messages.weather()
    wnd = await messages.wind()
    sun = await messages.sun_time()
    await message.answer(wth + '\n' + wnd + '\n' + sun, reply_markup=kb.main)

@dp.message(F.text == 'Новости')
async def cmd_tpu(message: t.Message):
    await message.answer('Раздел в разработке', reply_markup=kb.main)

@dp.message(F.text == 'Заметки')
async def cmd_tpu(message: t.Message):
    await message.answer('Раздел в разработке', reply_markup=kb.main)


@dp.message(F.text == '/my_id')
async def cmd_my_id(message: t.Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваше имя: {message.from_user.first_name}')
    await message.answer_photo(photo='https://img.gazeta.ru/files3/142/14995142/59c54411-4c87-40ab-9fd6-65ef1cea-pic_32ratio_1200x800-1200x800-33845.jpg', caption='Райан Гослинг')


@dp.message(F.document)
async def cmd_send_doc(message: t.Message):
    await bot.send_document(chat_id='480577366', document=message.document.file_id, caption='Был прислан документ')


# Ниже функции не писать!
@dp.message()
async def echo(message: t.Message):
    await message.answer("Боюсь, что я вас не понимаю")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
