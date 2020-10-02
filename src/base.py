from src.consts import PATH_TO_INSTITUTES
import os

class Base:
	def __init__(self):
		self.all_universitys = None						#Все университеты
		self.all_institutes = self.getAllInstitutes()	#Все институты
		self.all_groups = self.getAllGroups()			#Все группы

	#Вовзращает все университеты из базы данных
	def getUniversitys(self):	
		#Пока что ненужная функция, т.к. университет только один - ВлГУ
		pass

	#Вовзращает все институты из базы данных
	def getAllInstitutes(self):
		path = os.getcwd() + PATH_TO_INSTITUTES
		return os.listdir(path)
		
	#Вовзращает все группы из базы данных
	def getAllGroups(self):
		groups = []
		#Проходимся по всем институтам
		for institute in self.all_institutes:
			path = os.getcwd() + PATH_TO_INSTITUTES + "/" + institute
			courses = os.listdir(path)
			#Проходимся по всем курсам
			for course in courses:
				path = os.getcwd() + PATH_TO_INSTITUTES + "/" + institute + "/" + course
				this_groups = os.listdir(path)
				for group in this_groups:
					groups.append(group)

		return groups 