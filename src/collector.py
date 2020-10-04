class Collector:
	def __init__(self, signal):
		self.signal = signal
		self.message = None
		

	def collected(self):
		if self.signal == 7:
			self.message = self.method7()

		return self.message

	def method7(self):
		message = "Нашли какую то ошибку или недочёт?\nНапишите прямо тут детальное сообщение об ошибке с пометкой: *Ошибка*\nМы обязательно прочтём и исправим баг в ближайшее время\nСпасибо"
		
		return message
		

