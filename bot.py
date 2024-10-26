from loader import bot, storage
from users import admins, users
from markups import start, permit

from system import genPassword

async def on_shutdown(dp):
    await bot.close()
    await storage.close()

async def on_startup(users,admins):
    genPassword()
    for admin_id in admins:
        await bot.send_message(admin_id, '🔴Админ🔴\nБот запущен!\nНажмите на кнопку для старта!🚀', reply_markup=permit)
    for user_id in users:
        await bot.send_message(user_id, 'Бот запущен!\nНажмите на кнопку для старта!🚀', reply_markup=start)

if __name__ == '__main__':
    from aiogram import executor
    from С_handlers import dp
    from H_handlers import dp

    executor.start(dp, on_startup(users,admins))
    executor.start_polling(dp, on_shutdown=on_shutdown, skip_updates=True)