from random import randint

def rectifier():
	with open('TaskList.txt', 'r', encoding = 'utf-8') as TaskList:	
		punishment = 0
		task_counter = 0
		number = 1
		lines = TaskList.readlines()

		for key, line in enumerate(lines):
			lines[key] = lines[key][:-1]

		NiceList = 'Список дел:\n'

		for i in range(0,len(lines)-1,+3):
			if lines[i+1] == '0':
				NiceList = NiceList + str(number) + '. ' + '❌' + lines[i] + ' - ' + lines[i+2] + ' ч.' + '\n'
				punishment += int(lines[i+2])
				task_counter += 1
				number += 1

			elif lines[i+1] == '1':
				NiceList = NiceList + str(number) + '. ' + '✅' + lines[i] + ' - ' + lines[i+2] + ' ч.' + '\n'
				number += 1

		with open('SessionValidity.txt','r') as SessionValidity:
			Validity = SessionValidity.read()
			if Validity == 'True':
				NiceList = review(NiceList,task_counter,punishment)
			elif Validity == 'False':
				NiceList = conclusion(NiceList,task_counter,punishment)
	return NiceList

def conclusion(NiceList,task_counter,punishment):
	if task_counter > 0:
		NiceList = NiceList + '❌' + 'Не завершено' + '❌' + '\n' + 'Дел не сделано: ' + str(task_counter) + '; ' + 'Итоговое наказание: ' + str(punishment) + ' ч.'
	elif task_counter == 0:
		NiceList = NiceList + '✅' + 'Завершено' + '✅'
	return NiceList

def review(NiceList,task_counter,punishment):
	NiceList = NiceList + 'Дел осталось: ' + str(task_counter) + '; Наказание: ' + str(punishment) + ' ч.'
	return NiceList

def Task_reg(name,hours):
	with open('TaskList.txt','a',encoding = 'utf-8') as TaskList:
		TaskList.write(name + '\n')
		TaskList.write('0\n')
		TaskList.write(str(hours) + '\n')


def new_TaskList():
	with open('TaskList.txt','w+',encoding = 'utf-8') as TaskList:
		TaskList.seek(0)
		TaskList.close()
	with open('SessionValidity.txt','w') as SessionValidity:
		SessionValidity.write('True')

def CloseList():
	with open('SessionValidity.txt','w') as SessionValidity:
		SessionValidity.write('False')

def del_Task(suspect):
	suspect = int(suspect)
	with open('TaskList.txt', 'r', encoding = 'utf-8') as TaskList:
		lines = TaskList.readlines()
	if suspect == 1:
		for i in range(3):
			del lines[0]
	for i in range(3):
		del lines[suspect*3-3]
	with open('TaskList.txt', 'w', encoding = 'utf-8') as TaskList:
		TaskList.writelines(line for line in lines)

def genPassword():
	with open('password.txt', 'w', encoding = 'utf-8') as password:
		pas = 'P' + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) 
		password.write(pas)

def Task_done(suspect):
	suspect = int(suspect)
	output = ""

	with open('TaskList.txt', 'r', encoding = 'utf-8') as TaskList:
		lines = TaskList.readlines()

	if lines[suspect*3-2] == '0\n':
		del lines[suspect*3-2]
		lines.insert(suspect*3-2,'1\n')

		with open('TaskList.txt', 'w', encoding = 'utf-8') as TaskList:
			TaskList.writelines(line for line in lines)
		output = 'Задание успешно выполнено!'

	elif lines[suspect*3-2] == '1\n':
		output = 'Задание уже было выполнено!'

	return output