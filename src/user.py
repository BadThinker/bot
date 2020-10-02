from src.api import vk
from src.consts import GROUP_ID

class User:
	def __init__(self, message, id):
		self.message = message				#Текущее сообщение
		self.id = id						#ID-пользователя
		self.inGroup = self.isMember()		#Состоит ли он в группе?
		self.university = None				#Университет пользователя
		self.institute = None				#Институт пользователя
		self.course = None					#Курс пользователя
		self.group = None					#Группа пользователя
		self.day = None						#Выбранный пользователем день

	#Проверяет является ли пользователь участником
	def isMember(self):
		if(vk.method('groups.isMember', {'group_id': GROUP_ID, 'user_id': self.id})):
			return True
		else:
			return False

	#Печатает инфу о пользователе
	def printed(self):
		print("ID: ", self.id)
		print("inGroup: ", self.inGroup)