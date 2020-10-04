from vk_api.utils import get_random_id
from src.api import vk
from src.user import User
 
#Отправить сообщение пользователю
def write(message, User, Keyboard):
	if(Keyboard == None):
		vk.method('messages.send', {'user_id'	: User.id, 
									'message'	: message, 
									'random_id'	: get_random_id()})
	else:
		vk.method('messages.send', {'user_id'	: User.id, 
									'message'	: message, 
									'random_id'	: get_random_id(),
									'keyboard'	: Keyboard})	