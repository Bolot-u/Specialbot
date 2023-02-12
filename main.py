from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging
import decouple
from decouple import config

TOKEN = config('TOKEN')
bot = Bot(TOKEN)
db = Dispatcher(bot=bot)

@db.message_handler(commands=['start','hello'])
async def start_handler(message: types.Message):
            await bot.send_message(message.from_user.id, f'hello {message.from_user.first_name}')
            await message.answer("it is an answer")
            await message.reply('it is a reply')
if __name__=='__main__':



    logging.basicConfig(level=logging.INFO)
    executor.start_polling(db, skip_updates=True)