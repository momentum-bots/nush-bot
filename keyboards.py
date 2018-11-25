from telebot import types
from languages import DICTIONARY


def get_choose_status_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['is_parents_button'])
    keyboard.add(DICTIONARY[language]['is_teachers_button'])
    return keyboard


def get_parents_choose_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['is_children_button'])
    keyboard.add(DICTIONARY[language]['no_children_button'])
    return keyboard


# def get_parents_with_children_keyboard(language='ua'):
#     keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     keyboard.add(DICTIONARY[language]['excursion_1_1'])
#     keyboard.add(DICTIONARY[language]['excursion_1_2'])
#     keyboard.add(DICTIONARY[language]['excursion_1_3'])
#     keyboard.add(DICTIONARY[language]['back_button'])
#     return keyboard


def get_parents_without_children_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['excursion_button'])
    keyboard.add(DICTIONARY[language]['all_about_nush_btn'])
    keyboard.add(types.KeyboardButton(text=DICTIONARY[language]['choose_school_button'], request_location=True))
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard


def get_all_about_nush_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['concept_nush_btn'])
    keyboard.add(DICTIONARY[language]['thematic_sections_button'])
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard


def get_excursion_button_keyboard(language='ua'):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=DICTIONARY[language]['excursion_1_button'],
                                            callback_data=DICTIONARY[language]['excursion_1_button']))
    keyboard.row(types.InlineKeyboardButton(text=DICTIONARY[language]['excursion_2_button'],
                                            callback_data=DICTIONARY[language]['excursion_2_button']),
                 types.InlineKeyboardButton(text=DICTIONARY[language]['excursion_3_button'],
                                            callback_data=DICTIONARY[language]['excursion_3_button']))
    keyboard.row(types.InlineKeyboardButton(text=DICTIONARY[language]['excursion_4_button'],
                                            callback_data=DICTIONARY[language]['excursion_4_button']),
                 types.InlineKeyboardButton(text=DICTIONARY[language]['excursion_5_button'],
                                            callback_data=DICTIONARY[language]['excursion_5_button']))
    return keyboard


def get_inline_back_keyboard(language='ua'):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text=DICTIONARY[language]['back_to_class_button'],
                                            callback_data=DICTIONARY[language]['back_to_class_button']))
    return keyboard

def get_teachers_choose_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['pilot_schools_button'])
    keyboard.add(DICTIONARY[language]['trade_experiences_button'])
    keyboard.add(DICTIONARY[language]['upgrade_qualification_button'])
    keyboard.add(DICTIONARY[language]['better_with_facebook_button'])
    keyboard.add(DICTIONARY[language]['mon_button'])
    return keyboard


def get_upgrade_qualification_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['lectures_button'])
    keyboard.add(DICTIONARY[language]['online_courses_button'])
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard


def get_mon_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['ask_mon_question_btn'])
    keyboard.add(DICTIONARY[language]['faq_mon_btn'])
    keyboard.add(DICTIONARY[language]['rating_mon_question_btn'])
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard


def get_ask_mon_keyboard(language='ua'):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(DICTIONARY[language]['back_button'])
    return keyboard
