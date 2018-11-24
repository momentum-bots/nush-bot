from bot_object import bot
from languages import DICTIONARY
from keyboards import *
from time import sleep



def choose_status_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['nush_is_msg'])
        sleep(0.5)
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['choose_status_button'],
                         reply_markup=get_choose_status_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['is_parents_button']:
            return True, 'parents_state'
        elif message.text == DICTIONARY['ua']['is_teachers_button']:
            return True, 'teachers_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


'''
PARENTS
'''
def parents_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['is_children_msg'],
                         reply_markup=get_parents_choose_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['is_children_button']:
            return True, 'parents_state'
        elif message.text == DICTIONARY['ua']['no_children_button']:
            return True, 'teachers_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


'''
TEACHERS
'''
def teachers_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['useful_docs_msg'],
                         parse_mode="HTML",
                         reply_markup=get_teachers_choose_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['pilot_schools_button']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['pilot_nush_msg'],
                             parse_mode="HTML",
                             reply_markup=get_teachers_choose_keyboard('ua'))
            sleep(0.5)
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['materials_for pilots_msg'],
                             parse_mode="HTML",
                             reply_markup=get_teachers_choose_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['trade_experiences_button']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['trade_experience_fb_group_msg'],
                             parse_mode="HTML",
                             reply_markup=get_teachers_choose_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['upgrade_qualification_button']:
            return True, 'upgrade_qualification_state'
        elif message.text == DICTIONARY['ua']['better_with_facebook_button']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['better_with_facebook_fb_group_msg'],
                             parse_mode="HTML",
                             reply_markup=get_teachers_choose_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['mon_button']:
            return True, 'mon_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def upgrade_qualification_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['upgrade_qualification_msg'],
                         reply_markup=get_upgrade_qualification_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['lectures_button']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['lectures_msg'],
                             parse_mode="HTML",
                             reply_markup=get_upgrade_qualification_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['online_courses_button']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['online_courses_msg'],
                             parse_mode="HTML",
                             reply_markup=get_upgrade_qualification_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['back_button']:
            return True, 'teachers_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def mon_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['mon_msg'],
                             reply_markup=get_mon_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['ask_mon_question_btn']:
            return True, 'ask_mon_question_state'
        elif message.text == DICTIONARY['ua']['faq_mon_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['faq_mon_msg'],
                             parse_mode="HTML",
                             reply_markup=get_mon_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['rating_mon_question_btn']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['rating_mon_question_msg'],
                             reply_markup=get_mon_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['back_button']:
                return True, 'teachers_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def ask_mon_question_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['ask_mon_question_msg'],
                         parse_mode="HTML",
                         reply_markup=get_ask_mon_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['back_button']:
            return True, 'mon_state'
    return False, ''



def excursion_state(message, user, is_entry=False):
    if is_entry:
        bot.send_photo(message.chat.id,
                       photo='https://telegram.org/img/t_logo.png',
                       reply_markup=get_excursion_button_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['back_button']:
            return True, 'choose_status_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''
