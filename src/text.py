import re							#Регулярные выражения
from src.consts import ALL_DAYS

#Это университет? (пока что не нужная функция, т.к. университет только один - ВлГУ)
def isUniversity(text, all_universitys):
	pass

#Это институт?
def isInstitute(text, all_institutes):
	text = text.upper()
	for institute in all_institutes:
		if institute == text:	return True

	return False

#Это курс какого то университета?
def isCourse(text, all_courses):
	text = text.upper().split(" ")
	if(len(text) == 2):
		#******FIX IT*******(Сделать проверку на институт)
		if text[0].find("КУРС") != -1 or text[1].find("КУРС") != -1:		return True
	return False

#Это группа?
def isGroup(text):
	result = re.search(r"\w{1,3}[- ]\d\d\d.{0,1}|\w{1,3}\d\d\d.{0,1}", text)
	if result != None and result.group(0) == text: return True
	return False

#Это расписание на какой то день?
def isDay(text):
	text = text.upper().split(" ")
	if(len(text) > 1):
		for word in text:
			for day in ALL_DAYS:
				if word == day:
					for word2 in text:
						if isGroup(word2):	return True 
	
	return False
