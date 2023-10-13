from coordinates import get_coordinates
from api_service import get_weather
from translate import  Translator

async def translate_to_russian(text):
    translator = Translator(from_lang='en', to_lang='ru')
    translation = translator.translate(text)
    return translation


async def weather() -> str:
    """Returns a message about the temperature and weather description"""
    wthr = await get_weather(await get_coordinates())
    return f'{await translate_to_russian(wthr.location)}, {await translate_to_russian(wthr.description)}\n' \
           f'Температура {int(wthr.temperature)}°C, ощущается как {int(wthr.temperature_feeling)}°C'


async def wind() -> str:
    """Returns a message about wind direction and speed"""
    wthr = await get_weather(await get_coordinates())
    return f'{await translate_to_russian(wthr.wind_direction)} ветер {wthr.wind_speed} m/s'


async def sun_time() -> str:
    """Returns a message about the time of sunrise and sunset"""
    wthr = await get_weather(await get_coordinates())
    return f'Восход: {wthr.sunrise.strftime("%H:%M")}\n' \
           f'Закат: {wthr.sunset.strftime("%H:%M")}\n'