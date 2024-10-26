from aiogram import types
from aiogram.dispatcher import FSMContext
import markups as mrkp
from aiogram.types import ReplyKeyboardRemove
import system

from loader import dp, bot
from states import menus, ListBuilding, ChangeList

with open('password.txt', 'r', encoding='utf-8') as password:
    pas = password.read()


@dp.message_handler(commands=[pas])
async def enter_menu(message: types.Message):
    await bot.send_message(message.chat.id, 'Выбирите действие', reply_markup=mrkp.mainMenu)
    await menus.menu.set()


@dp.message_handler(state=menus.menu)
async def mainMenu(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '🟩Новый список дел':
        await bot.send_message(message.chat.id, "Удалить прошлый список дел, создавая новый?",
            reply_markup=mrkp.acceptMenu)
        await menus.acceptNewList.set()

    elif answer == '🟦Просмотреть список':
        await message.answer(system.rectifier(), reply_markup=mrkp.mainMenu)
        await menus.menu.set()

    elif answer == '🟥Закрыть список':
        with open('SessionValidity.txt','r') as SessionValidity:
            Validity = SessionValidity.read()
        if Validity == 'True':
            await message.answer('Вы уверены что хотите закрыть список?',reply_markup=mrkp.acceptMenu)
            await menus.acceptCloseList.set()
        elif Validity == 'False':
            await message.answer('Список дел уже закрыт!⛔')
            await menus.menu.set()

    elif answer == '🟨Изменить список':
        with open('SessionValidity.txt','r') as SessionValidity:
            Validity = SessionValidity.read()
        if Validity == 'True':
            await message.answer('Выберите действие',reply_markup=mrkp.choice_of_change)
            await ChangeList.choice.set()
        elif Validity == 'False':
            await message.answer('Список дел уже закрыт!⛔')
            await menus.menu.set()

    elif answer == '-backdoor':
        await message.answer('BACKDOORED',reply_markup=ReplyKeyboardRemove())
        await state.finish()


# === NEW LIST ===
@dp.message_handler(state=menus.acceptNewList)
async def NewTask_acept(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '✅Да':
        await bot.send_message(message.from_user.id, 'Создаём новый список.\nВведите название первого задания',
            reply_markup=ReplyKeyboardRemove())
        system.new_TaskList()
        await ListBuilding.title.set()

    elif answer == '❌Отмена':
        await bot.send_message(message.from_user.id, 'Выбирите действие:',
            reply_markup=mrkp.mainMenu)
        await menus.menu.set()


@dp.message_handler(state=ListBuilding.title)
async def ListBuilding_name(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer('Введите количество часов без девайсов за его невыполнение')
    await ListBuilding.hours.set()


@dp.message_handler(state=ListBuilding.hours)
async def ListBuilding_hours(message: types.Message, state: FSMContext):
    data = await state.get_data()
    title = data.get("title")
    hours = message.text
    system.Task_reg(title,hours)
    await message.answer('Ещё задание?',reply_markup=mrkp.extension)
    await ListBuilding.cont.set()


@dp.message_handler(state=ListBuilding.cont)
async def ListBuilding_name(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '🔁Да':
        await message.answer('Новое дело.\nВведите его название',
            reply_markup=ReplyKeyboardRemove())
        await ListBuilding.title.set()
    elif answer == '⏹Закончить список':
        await message.answer('Список успешно создан!')
        await message.answer(system.rectifier(),reply_markup=mrkp.mainMenu)
        await menus.menu.set()



# === CLOSE LIST ===
@dp.message_handler(state=menus.acceptCloseList)
async def Close(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '✅Да':
        system.CloseList()
        await message.answer('Список успешно закрыт!')
        await message.answer(system.rectifier(),reply_markup=mrkp.mainMenu)
        await menus.menu.set()
    elif answer == '❌Отмена':
        await bot.send_message(message.from_user.id, 'Отменено.',
            reply_markup=mrkp.mainMenu)
        await menus.menu.set()


# === CHANGE LIST ===
@dp.message_handler(state=ChangeList.choice)
async def Choice(message: types.Message, state: FSMContext):
    answer = message.text
    if answer == '📝Добавить задание':
        await bot.send_message(message.from_user.id, 'Введите название задания',
            reply_markup=ReplyKeyboardRemove())
        await ChangeList.addTask_title.set()

    elif answer == '🗑Удалить задние':
        await message.answer(system.rectifier())
        await message.answer('Введите номер задания, которое хотите удалить',
            reply_markup=ReplyKeyboardRemove())
        await ChangeList.delTask.set()

    elif answer == '❌Отмена':
        await message.answer('Отменено.',reply_markup=mrkp.mainMenu)
        await menus.menu.set()


@dp.message_handler(state=ChangeList.addTask_title)
async def AddTask_name(message: types.Message, state: FSMContext):
    title = message.text
    await state.update_data(title=title)
    await message.answer('Введите количество часов без девайсов за его невыполнение')
    await ChangeList.addTask_hours.set()


@dp.message_handler(state=ChangeList.addTask_hours)
async def AddTask_hours(message: types.Message, state: FSMContext):
    data = await state.get_data()
    title = data.get("title")
    hours = message.text
    system.Task_reg(title,hours)
    await message.answer('Новое задание успешно добавлено!')
    await message.answer(system.rectifier(),reply_markup=mrkp.mainMenu)
    await menus.menu.set()


@dp.message_handler(state=ChangeList.delTask)
async def DelTask(message: types.Message, state: FSMContext):
    number = message.text
    system.del_Task(number)
    await message.answer('Задание успешно удалено!')
    await message.answer(system.rectifier(),reply_markup=mrkp.mainMenu)
    await menus.menu.set()

