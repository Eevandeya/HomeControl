from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from states import menus, ListBuilding, ChangeList
from aiogram.types import ReplyKeyboardRemove
import system
import markups as mrkp

from states import jrLobby
from loader import dp, bot


@dp.message_handler(commands=['start'])
async def enter_menu(message: types.Message):
    await bot.send_message(message.chat.id, 'Выбирите действие', reply_markup=mrkp.jrmenu)
    await jrLobby.jrMenu.set()

@dp.message_handler(state=jrLobby.jrMenu)
async def mainMenu(message: types.Message, state: FSMContext):
    answer = message.text

    if answer == '🟩Завершить дело':
        with open('SessionValidity.txt','r') as SessionValidity:
            Validity = SessionValidity.read()
        if Validity == 'True':
            await message.answer('Введите номер дела, которое хотите завершить')
            await message.answer(system.rectifier(), reply_markup=mrkp.cancel)
            await jrLobby.compMark.set()
        elif Validity == 'False':
            await message.answer('Список дел уже закрыт!⛔', reply_markup=mrkp.jrmenu)
            await jrLobby.jrMenu.set()

    elif answer == '🟦Просмотреть список':
            await message.answer(system.rectifier(), reply_markup=mrkp.jrmenu)
            await jrLobby.jrMenu.set()

    elif answer == '-backdoor':
        await message.answer('BACKDOORED',reply_markup=ReplyKeyboardRemove())
        await state.finish()

@dp.message_handler(state=jrLobby.compMark)
async def compliteTask(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '❌Отмена':
        await message.answer('Отменено.', reply_markup=mrkp.jrmenu)
        await jrLobby.jrMenu.set()
    else:
        await message.answer(system.Task_done(answer), reply_markup=mrkp.jrmenu)
        await jrLobby.jrMenu.set()