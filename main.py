import asyncio
from aiogram import Bot, Dispatcher, F, types as t
from config import bot_token

bot = Bot(bot_token)
dp = Dispatcher()


@dp.message(F.text == '/start')
async def cmd_start(message: t.Message):
    await message.answer('Приветствую вас, создатель')


@dp.message(F.text == '/my_id')
async def cmd_my_id(message: t.Message):
    await message.answer(f'Ваш ID: {message.from_user.id}')
    await message.reply(f'Ваше имя: {message.from_user.first_name}')
    await message.answer_photo(photo='https://img.gazeta.ru/files3/142/14995142/59c54411-4c87-40ab-9fd6-65ef1cea-pic_32ratio_1200x800-1200x800-33845.jpg', caption='Райан Гослинг')


@dp.message()
async def echo(message: t.Message):
    await message.answer("Боюсь, что я вас не понимаю")


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
