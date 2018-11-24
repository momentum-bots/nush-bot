from bot_object import bot
from languages import DICTIONARY
from keyboards import *


def main_menu_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['main_menu_msg'],
                         reply_markup=get_main_menu_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['excursion_button']:
            return True, 'excursion_state'
        if message.text == DICTIONARY['ua']['faq_button']:
            return True, 'ask_question_mon_state'
    return False, ''


def ask_question_mon_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['ask_mon_question_msg'],
                         reply_markup=get_faq_mon_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['back_button']:
            return True, 'main_menu_state'
    return False, ''


def excursion_state(message, user, is_entry=False):
    if is_entry:
        bot.send_photo(message.chat.id,
                       photo='https://telegram.org/img/t_logo.png',
                       reply_markup=get_excursion_button_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['back_button']:
            return True, 'main_menu_state'
    return False, ''
                       # photo=open('Sova.jpg', 'rb'),
