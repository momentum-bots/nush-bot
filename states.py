from bot_object import bot
from languages import DICTIONARY
from keyboards import *
from database import Question, ROLES
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
            user.role = ROLES[0]
            user.save()
            return True, 'parents_state'
        elif message.text == DICTIONARY['ua']['is_teachers_button']:
            user.role = ROLES[1]
            user.save()
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
            user.with_child_in_school = True
            user.save()
            return True, 'parents_with_children_state'
        elif message.text == DICTIONARY['ua']['no_children_button']:
            user.with_child_in_school = False
            user.save()
            return True, 'parents_without_children_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def parents_with_children_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['parents_with_children_msg'],
                         reply_markup=get_parents_with_children_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['olympiads_button']:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['olympiads_msg'],
                             parse_mode="HTML",
                             reply_markup=get_parents_with_children_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['ask_mon_question_btn']:
            return True, 'ask_mon_question_state'
        elif message.text == DICTIONARY['ua']['rating_mon_question_btn']:
            return True, 'rating_mon_question_state'
        elif message.text == DICTIONARY['ua']['back_button']:
            return True, 'parents_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def rating_mon_question_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         "Список питань до МОН:",
                         reply_markup=get_back_button_keyboard('ua'))
        for _question in Question.objects().order_by('rating'):
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['rated_questions_msg'].format(_question.text, _question.rating),
                             parse_mode="Markdown",
                             reply_markup=get_rating_mon_question_keyboard(_question.text ,'ua'))
    else:
        if message.text == DICTIONARY['ua']['back_button']:
            return return_to_your_state(user)
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def parents_without_children_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['parents_without_children_msg'],
                         reply_markup=get_parents_without_children_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['all_about_nush_btn']:
            return True, 'all_about_nush_state'
        elif message.text == DICTIONARY['ua']['excursion_button']:
            bot.send_photo(message.chat.id,
                           photo=open('img/excursion.png', 'rb'),
                           caption=DICTIONARY['ua']['excursion_msg'],
                           reply_markup=get_excursion_button_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['ask_mon_question_btn']:
            return True, 'ask_mon_question_state'
        elif message.text == DICTIONARY['ua']['rating_mon_question_btn']:
            return True, 'rating_mon_question_state'
        elif message.text == DICTIONARY['ua']['back_button']:
            return True, 'parents_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def universal_callback_query_handler(reply, user):
    if reply.data == DICTIONARY['ua']['excursion_1_button']:
        bot.send_photo(reply.from_user.id,
                       photo=open('img/lego.jpg', 'rb'),
                       caption=DICTIONARY['ua']['excursion_1_msg'],
                       reply_markup=get_inline_back_keyboard('ua'))
    elif reply.data == DICTIONARY['ua']['excursion_2_button']:
        bot.send_photo(reply.from_user.id,
                       photo=open('img/party.jpg', 'rb'),
                       caption=DICTIONARY['ua']['excursion_2_msg'],
                       reply_markup=get_inline_back_keyboard('ua'))
    elif reply.data == DICTIONARY['ua']['excursion_3_button']:
        bot.send_photo(reply.from_user.id,
                       photo=open('img/vidpochynok.jpg', 'rb'),
                       caption=DICTIONARY['ua']['excursion_3_msg'],
                       reply_markup=get_inline_back_keyboard('ua'))
    elif reply.data == DICTIONARY['ua']['excursion_4_button']:
        bot.send_photo(reply.from_user.id,
                       photo=open('img/stendy.jpeg', 'rb'),
                       caption=DICTIONARY['ua']['excursion_4_msg'],
                       reply_markup=get_inline_back_keyboard('ua'))
    elif reply.data == DICTIONARY['ua']['excursion_5_button']:
        bot.send_photo(reply.from_user.id,
                       photo=open('img/drawing.jpg', 'rb'),
                       caption=DICTIONARY['ua']['excursion_5_msg'],
                       reply_markup=get_inline_back_keyboard('ua'))
    # button for questions' rating
    elif reply.data == DICTIONARY['ua']['back_button']:
        bot.send_photo(reply.from_user.id,
                       photo=open('img/excursion.png', 'rb'),
                       caption=DICTIONARY['ua']['excursion_msg'],
                       reply_markup=get_excursion_button_keyboard('ua'))
    else:
        question = Question.objects(text=reply.data).first()
        print(question)
        if question is None:
            pass
        else:
            if user.user_id not in question.subscribed_users:
                question.subscribed_users.append(user.user_id)
                question.rating += 1
                question.save()
            else:
                bot.send_message(reply.from_user.id, "Ви вже підтримали це питання.")
    bot.answer_callback_query(reply.id)


def all_about_nush_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['all_about_nush_msg'],
                         reply_markup=get_all_about_nush_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['concept_nush_btn']:
            bot.send_message(message.chat.id,
                           "https://www.youtube.com/watch?v=uWPdRjpQMmo",
                           reply_markup=get_all_about_nush_keyboard('ua'))
            sleep(0.5)
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['norma_docs_msg'],
                             parse_mode="HTML",
                             reply_markup=get_all_about_nush_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['thematic_sections_button']:
            return True, 'thematic_sections_state'
        elif message.text == DICTIONARY['ua']['back_button']:
            return True, 'parents_without_children_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


def thematic_sections_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['thematic_sections_msg'],
                         reply_markup=get_thematic_sections_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['theme_first_btn']:
            bot.send_message(message.chat.id,
                             "В розробці :)",
                             reply_markup=get_thematic_sections_keyboard('ua'))
        if message.text == DICTIONARY['ua']['theme_second_btn']:
            bot.send_message(message.chat.id,
                             "В розробці :)",
                             reply_markup=get_thematic_sections_keyboard('ua'))
        elif message.text == DICTIONARY['ua']['back_button']:
            return True, 'all_about_nush_state'
        else:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_button'])
    return False, ''


"""
TEACHERS
"""


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
            return True, 'rating_mon_question_state'
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
            return return_to_your_state(user)
        else:
            user.current_question = message.text
            user.save()
            return True, 'question_confirmation_state'
    return False, ''


def question_confirmation_state(message, user, is_entry=False):
    if is_entry:
        bot.send_message(message.chat.id,
                         DICTIONARY['ua']['question_confirmation_msg'] % user.current_question,
                         parse_mode="Markdown",
                         reply_markup=get_question_confirmation_keyboard('ua'))
    else:
        if message.text == DICTIONARY['ua']['question_confirmation_btn']:
            question = Question(text=user.current_question,
                                subscribed_users=[])
            question.save()
            bot.send_message(message.chat.id, "Дякуємо Вам за питання!")
            return return_to_your_state(user)
        elif message.text == DICTIONARY['ua']['question_decline_btn']:
            return True, 'ask_mon_question_state'
    return False, ''


def return_to_your_state(user):
    if user.role == ROLES[0]:
        if user.with_child_in_school:
            return True, 'parents_with_children_state'
        elif user.with_child_in_school is False:
            return True, 'parents_without_children_state'
    elif user.role == ROLES[1]:
        return True, 'mon_state'