from src.user import User

class Analysis:
	def __init__(self, message):
		self.text = message			#Сообщение отправленное пользователя
	
	def analysed(self):
		print("Ага, я проанализировал этот текст: ", self.text)
