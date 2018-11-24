from telebot import types
from languages import DICTIONARY


def get_main_menu_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton(text=DICTIONARY[language]['choose_school_button'], request_location=True))
    keyboard.add(DICTIONARY[language]['faq_button'])
    keyboard.add(DICTIONARY[language]['useful_info_button'])
    keyboard.add(DICTIONARY[language]['excursion_button'])
    return keyboard


def get_faq_mon_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['faq_mon_btn'])
    keyboard.add(DICTIONARY[language]['ask_mon_btn'])
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard


def get_excursion_button_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['excursion_1_1'])
    keyboard.add(DICTIONARY[language]['excursion_1_2'])
    keyboard.add(DICTIONARY[language]['excursion_1_3'])
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard
