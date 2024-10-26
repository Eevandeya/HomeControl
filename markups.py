from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# === main === 
button_NewList = '🟩Новый список дел'
button_ListClose = '🟥Закрыть список'
button_EditList = '🟨Изменить список'
button_ViewList = '🟦Просмотреть список'
mainMenu = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	           KeyboardButton(text=button_NewList), KeyboardButton(text=button_ListClose)
	         ],
	         [
	           KeyboardButton(text=button_EditList), KeyboardButton(text=button_ViewList)
	         ]
	       ]
	    )


# === accept_1 ===
button_Yes = '✅Да'
button_Cancel = '❌Отмена'
acceptMenu = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	            KeyboardButton(text=button_Yes), KeyboardButton(text=button_Cancel)
	         ],	         
	       ]
        )

# === extension ===
button_Next = '🔁Да'
button_EndList = '⏹Закончить список'
extension = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	            KeyboardButton(text=button_Next), KeyboardButton(text=button_EndList)
	         ],	         
	       ]
        )

# === Change List ===
button_DelTask = '🗑Удалить задние'
button_AddTask = '📝Добавить задание'
# button_Cancel
choice_of_change = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	            KeyboardButton(text=button_AddTask), KeyboardButton(text=button_DelTask)
	         ],
	         [	         
	            KeyboardButton(text=button_Cancel)
	         ]

	       ]
        )

# === START ===
button_start = '/start'
start = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	            KeyboardButton(text=button_start)
	         ]
	       ]
        )

# === ADMIN START ===
with open('password.txt', 'r', encoding = 'utf-8') as password:
	pas = password.read() 
button_permit = '/' + pas
permit = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	            KeyboardButton(text=button_permit)
	         ]
	       ]
        )

# === jr menu ===
# button_ViewList
button_DoneTask = '🟩Завершить дело'
jrmenu = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	            KeyboardButton(text=button_DoneTask), KeyboardButton(text=button_ViewList)
	         ],	         
	       ]
        )

# === cancel ===
#button_Cancel
cancel = ReplyKeyboardMarkup(
	resize_keyboard=True,
	keyboard=[
	         [
	            KeyboardButton(text=button_Cancel)
	         ],	         
	       ]
        )