from bot_object import bot
from database import User
from state_handler import get_state_and_process
from distance import get_closest_school


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='main_menu_state'
                        )
            user.save()
        else:
            user.update(state='main_menu_state')
        get_state_and_process(message, user, True)
    # except Exception as e:
    #     print(e)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # try:
        user = User.objects(user_id=message.from_user.id).first()
        if user is None:
            user = User(user_id=message.from_user.id,
                        username=message.from_user.username,
                        first_name=message.from_user.first_name,
                        last_name=message.from_user.last_name,
                        state='main_menu_state'
                        )
            user.save()
        get_state_and_process(message, user)
    # except Exception as e:
    #     print(e)


@bot.message_handler(content_types=['location'])
def handle_location(message):
    # try:
        schools = get_closest_school(message.location.latitude, message.location.longitude)
        if schools == []:
            bot.send_message(message.chat.id,
                             'Шкіл поблизу немає. Ви що, в лісі?')
        else:
            for school in schools:
                print(school)
                bot.send_location(message.chat.id,
                                  school['position']['lat'],
                                  school['position']['lon'])
                bot.send_message(message.chat.id,
                                 '{0}\nЗа адресою: {1}'.format(
                                     school['poi']['name'],
                                     school['address']['freeformAddress']
                                 ))
    # except Exception as e:
    #     print(e)


if __name__ == '__main__':
    bot.remove_webhook()
    bot.polling(none_stop=True)
