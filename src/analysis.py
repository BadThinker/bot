from src.user import User
from src.consts import ALL_COURSES, ALL_DAYS
from src.text import isUniversity, isInstitute, isCourse, isGroup, isDay, isStart, isError
from src.text import isBackToGroups, isBackToInstitutes, isThisWeek, isNextWeek

class Analysis:
	def __init__(self, message):
		self.text = message			#Сообщение отправленное пользователя
	
	#Анализируем сообщение пользователя и возвращаем сигнал:
	def analysed(self):

		#if(isUniversity(self.text, base.all_universitys)):	return 1
		if(isInstitute(self.text)):							return 2
		if(isCourse(self.text)):							return 3
		if(isGroup(self.text)):								return 4
		if(isDay(self.text)):								return 5
		if(isStart(self.text)):								return 6
		if(isError(self.text)):								return 7
		if(isBackToGroups(self.text)):						return 8
		if(isBackToInstitutes(self.text)):					return 9
		if(isThisWeek(self.text)):							return 10
		if(isNextWeek(self.text)):							return 11
		#***FIX IT****(Спам обрабатывется пока что так)
		else: 												return 0					
