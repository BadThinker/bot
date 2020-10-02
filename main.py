from vk_api.longpoll import VkLongPoll, VkEventType         #Для работы с сообщениями

from src.user import User			#Модуль с описанием пользователя
from src.api import vk				#Авторизованный объект 'vk' для работы с VK-API
from src.analysis import Analysis	#Объект анализирующий сообщение пользователя
from src.base import Base			#Объект с базой данных

while(True):
	longpoll = VkLongPoll(vk)		#Работа с сообщениями
	for event in longpoll.listen():
		# Если пришло новое сообщение и оно предназначалось боту
		if event.type == VkEventType.MESSAGE_NEW and event.to_me == True:
				user = User(event.message, event.user_id)	#Создали пользователя
				analysis = Analysis(event.message)			#Анализатор сообщения
				analysis.analysed()							#Проанализировали текст
				base = Base()								#Создали базу данных
				print(base.all_institutes)		
				print(base.all_groups)