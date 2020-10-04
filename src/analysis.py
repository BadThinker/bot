from src.user import User
from src.base import Base
from src.consts import ALL_COURSES, ALL_DAYS
from src.text import isUniversity, isInstitute, isCourse, isGroup, isDay, isStart, isError
from src.text import isBackToGroups, isBackToInstitutes, isThisWeek, isNextWeek

class Analysis:
	def __init__(self, message):
		self.text = message			#Сообщение отправленное пользователя
	
	#Анализируем сообщение пользователя и возвращаем сигнал:
	def analysed(self):
		base = Base()				#Создали базу данных

		if(isUniversity(self.text, base.all_universitys)):	return "Вы ввели университет"
		if(isInstitute(self.text, base.all_institutes)):	return "Вы ввели название института"
		if(isCourse(self.text, ALL_COURSES)):				return "Вы ввели какой-то курс"
		if(isGroup(self.text)):								return "Вы ввели какую-то группу"
		if(isDay(self.text)):								return "Вы ввели расписание на какой то день"
		if(isStart(self.text)):								return "Вы ввели стартовую команду"
		if(isError(self.text)):								return "Вы ввели \"Сообщить об ошибке\""
		if(isBackToGroups(self.text)):						return "Вы ввели команду \"Назад к группам\""
		if(isBackToInstitutes(self.text)):					return "Вы ввели команду \"Назад к институтам\""
		if(isThisWeek(self.text)):							return "Вы ввели команду \"Текущая неделя\""
		if(isNextWeek(self.text)):							return "Вы ввели команду \"Следующая неделя\""
		#***FIX IT****(Спам обрабатывется пока что так)
		else: 												return "Непонятная команда.."					
