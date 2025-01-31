
import telebot
from telebot.types import ReplyKeyboardMarkup
import django
import os
#
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()


bot = telebot.TeleBot("7563690937:AAEN-F9LkfTfFyd512gpgpJL055_5E5XEfA")
# keyboard = ReplyKeyboardMarkup(
#     resize_keyboard=True, one_time_keyboard=False)
# keyboard.add("Button1")

category = []


@bot.message_handler(commands=["menu"])
def start(message):

    from foodDelivery.models import Category
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True, one_time_keyboard=True)
    for i in Category.objects.all():
        keyboard.add(str(i))
    bot.send_message(
        message.chat.id, f"hello {message.from_user.first_name}", reply_markup=keyboard)


@bot.message_handler(func=lambda message: True)
def handelBtn(message):
    meals = []
    # print(message)
    from foodDelivery.models import Meal
    for i in Meal.objects.filter(category__name=message.text).values():

        meals.append(
            f"الاسم: {i.get('name')}\nالوصف: {i.get('description')}\nالسعر: {i.get('price')}ج.م\n")

    m = "\n".join((meals))
    print(m)
    try:
        if message.text == "وجبات":

            bot.send_message(message.chat.id, str(m))

        elif message.text == "فطائر":
            bot.send_message(message.chat.id, str(m))

    except:
        bot.send_message(chat_id=message.chat.id, text="لا يوجد اعد المحاولة")

        # @bot.message_handler(func=lambda message: True)
        # def meal():


bot.polling()
