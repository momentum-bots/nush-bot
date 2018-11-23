from telebot import types
from languages import DICTIONARY


def get_main_menu_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['choose_school_button'])
    keyboard.add(DICTIONARY[language]['faq_button'])
    keyboard.add(DICTIONARY[language]['useful_info_button'])
    keyboard.add(DICTIONARY[language]['excursion_button'])
    return keyboard
