import re							#Регулярные выражения
from src.consts import ALL_INSTITUTES
from src.consts import ALL_COURSES
from src.consts import ALL_DAYS
from src.consts import START_COMMANDS
from src.consts import ERROR_COMMAND
from src.consts import BACK_GROUPS_COMMMAD
from src.consts import BACK_INSTITUTES_COMMAND
from src.consts import THIS_WEEK_COMMAND
from src.consts import NEXT_WEEK_COMMAND

#Это университет? (пока что не нужная функция, т.к. университет только один - ВлГУ)
def isUniversity(text, all_universitys):
	pass

#Это институт?
def isInstitute(text):
	for institute in ALL_INSTITUTES:
		if institute == text:	return True

	return False

#Это курс какого то университета?
def isCourse(text):
	if text.find("КУРС") != -1:
		text = text.replace("КУРС", "").strip().split(" ")
		if isInstitute(text[0]):
			text[1] = text[1].replace("М", "")
			if text[1].isdigit():	return True

	return False

#Это группа?
def isGroup(text):
	result = re.search(r"\w{1,3}[- ]\d\d\d.{0,1}|\w{1,3}\d\d\d.{0,1}", text)
	if result != None and result.group(0) == text: return True
	return False

#Это расписание на какой то день?
def isDay(text):
	result1 = re.search(r'(ПОНЕДЕЛЬНИК|ВТОРНИК|СРЕДА|ЧЕТВЕРГ|ПЯТНИЦА)( {0,1}\w{1,3}[- ]\d\d\d.{0,1}| {0,1}\w{1,3}\d\d\d.{0,1})', text)
	result2 = re.search(r'([А-Я]{1,3}[- ]\d\d\d\*{0,1}\ {0,1}|[А-Я]{1,3}\d\d\d\*{0,1}\ {0,1})(ПОНЕДЕЛЬНИК|ВТОРНИК|СРЕДА|ЧЕТВЕРГ|ПЯТНИЦА)', text)
	if result1 != None and result1.group(0) == text:	return True
	if result2 != None and result2.group(0) == text:	return True
	
	return False

#Это стартовая команда?
def isStart(text):
	for command in START_COMMANDS:
		if text == command:
			return True
	return False

#Это отчёт об ошибке?
def isError(text):
	if text == ERROR_COMMAND:	return True
	return False

#Это команда "Назад к группам"?
def isBackToGroups(text):
	if text == BACK_GROUPS_COMMMAD:	return True
	return False

#Это команда "Назад к институтам"?
def isBackToInstitutes(text):
	if text == BACK_INSTITUTES_COMMAND:	return True
	return False

#Это команда "Текущая неделя"?
def isThisWeek(text):
	if text == THIS_WEEK_COMMAND: 	return True
	return False

#Это команда "Следующая неделя"?
def isNextWeek(text):
	if text == NEXT_WEEK_COMMAND: 	return True
	return False
