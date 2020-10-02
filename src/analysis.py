from src.message import Message

class Analysis:
	def __init__(self, Message):
		self.text = Message.message
	
	def analysed(self):
		print("Ага, я проанализировал этот текст: ", self.text)
