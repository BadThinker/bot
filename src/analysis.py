from src.user import User
from src.base import Base
from src.consts import ALL_COURSES, ALL_DAYS
from src.text import isUniversity, isInstitute, isCourse, isGroup, isDay

class Analysis:
	def __init__(self, message):
		self.text = message			#Сообщение отправленное пользователя
	
	#Анализируем сообщение пользователя и возвращаем сигнал:
	def analysed(self):
		base = Base()				#Создали базу данных

		if(isUniversity(self.text, base.all_universitys)):	return 1
		if(isInstitute(self.text, base.all_institutes)):	return 2
		if(isCourse(self.text, ALL_COURSES)):				return 3
		if(isGroup(self.text)):								return 4
		if(isDay(self.text)):								return 5
		#***FIX IT****(Спам обрабатывется пока что так)
		else: 												return 0					
