from src.user import User

class Analysis:
	def __init__(self, User):
		self.text = User.message	#Получаем сообщение пользователя
	
	def analysed(self):
		print("Ага, я проанализировал этот текст: ", self.text)
