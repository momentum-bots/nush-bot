from bot_object import bot
from database import User
from state_handler import get_state_and_process, get_state_and_process_callback_query
from distance import get_closest_school
from languages import DICTIONARY


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(reply):
    try:
        user = User.objects(user_id=reply.from_user.id).first()
        if user is None:
            user = User(user_id=reply.from_user.id,
                        username=reply.from_user.username,
                        first_name=reply.from_user.first_name,
                        last_name=reply.from_user.last_name,
                        state='choose_status_state'
                        )
            user.save()
        get_state_and_process_callback_query(reply, user)
    except Exception as e:
            print(e)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='choose_status_state'
                        )
            user.save()
        else:
            user.state = 'choose_status_state'
            user.save()
            # user.update(state='choose_status_state')
        get_state_and_process(message, user, True)
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='choose_status_state'
                        )
            user.save()
        get_state_and_process(message, user)
    except Exception as e:
        print(e)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    try:
        schools = get_closest_school(message.location.latitude, message.location.longitude)
        if not schools:
            bot.send_message(message.chat.id,
                             DICTIONARY['ua']['no_schools_nearby_msg'])
        else:
            for school in schools:
                bot.send_location(message.chat.id,
                                  school['position']['lat'],
                                  school['position']['lon'])
                bot.send_message(message.chat.id,
                                 DICTIONARY['ua']['school_nearby_msg'].format(
                                     school['poi']['name'],
                                     school['address']['freeformAddress']
                                 ))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)
