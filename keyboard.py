from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton)

main_kb = [[KeyboardButton(text='Погода ⛅️')],
           [KeyboardButton(text='Новости')],
           [KeyboardButton(text='Заметки')],
           [KeyboardButton(text='Политех')]]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт ниже')

tpu_kb = [[InlineKeyboardButton(text='Личный кабинет', url='https://portal.tpu.ru/desktop/student/')],
          [InlineKeyboardButton(text='Расписание', url='https://rasp.tpu.ru/site/department.html?id=7950&cource=3')]]

tpu = InlineKeyboardMarkup(inline_keyboard=tpu_kb)
