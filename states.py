from aiogram.dispatcher.filters.state import StatesGroup, State


class menus(StatesGroup):
	menu = State()
	acceptNewList = State()
	acceptCloseList = State()

class ListBuilding(StatesGroup):
	title = State()
	hours = State()
	cont = State()

class ChangeList(StatesGroup):
	choice = State()
	addTask_title = State()
	addTask_hours = State()
	delTask = State()

class jrLobby(StatesGroup):
	jrMenu = State()
	compMark = State()