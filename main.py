from vk_api.longpoll import VkLongPoll, VkEventType         #Для работы с сообщениями

from src.user import User			#Модуль с описанием пользователя
from src.api import vk				#Авторизованный объект 'vk' для работы с VK-API
from src.analysis import Analysis	#Объект анализирующий сообщение пользователя
from src.collector import Collector	#Сборщик, собирающий итоговое сообщение для пользователя 
from src.writer import write		#Функция отправки сообщения пользователю

while(True):
	longpoll = VkLongPoll(vk)		#Работа с сообщениями
	for event in longpoll.listen():
		# Если пришло новое сообщение и оно предназначалось боту
		if event.type == VkEventType.MESSAGE_NEW and event.to_me == True:
				message = event.message.upper()				#Сообщение в верхнем регистре
				id = event.user_id							#ID-пользователя
				user = User(message, id)					#Создали пользователя
				analysis = Analysis(message)				#Анализатор сообщения
				collector = Collector(analysis.analysed())	#Анализируем сообщение и отправляем сборщику
				write(collector.collected(), user, None)	#Отправляем собранное сообщение