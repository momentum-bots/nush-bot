from bot_object import bot
from languages import DICTIONARY
from keyboards import *


def main_menu_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['main_menu_msg'],
                         reply_markup=get_main_menu_keyboard('ua'))
    else:
        pass
    return False, ''
