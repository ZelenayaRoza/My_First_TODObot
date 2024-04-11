import telebot

token = "7189418573:AAGgh2uU2GwmEDCGagK_reLsDcTBqRhOGXc"

bot = telebot.TeleBot(token)

import random

RANDOM_TASKS = ['Покормить котиков', 'Написать письмо', 'Сделать чай']

HELP = """
/help - напечатать справку по программе.
/add дата задачи текст задачи - добавить задачу в список
/show дата задачи - напечатать все добавленные задачи
/random - добавить случайную задачу на дату сегодня
"""

tasks = {}

def add_todo(date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = []
      tasks[date].append(task)

@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands = ["help"])
def help(message):
    bot.send_message(message.chat.id, HELP)

@bot.message_handler(commands = ["add", "todo"])
def add(message):
    command = message.text.split()
    if len(command) < 3:
        text = "Вы не ввели дату задачи"
        bot.send_message(message.chat.id, text)
        return
    else:
        command = message.text.split(maxsplit = 2)
        date = command[1].lower()
        task = command[2]
        add_todo(date, task)
        text = f'Задача   "{task}"   добавлена на дату   {date}'
        bot.send_message(message.chat.id, text)



@bot.message_handler(commands = ["random"])
def random_add(message):
    date = "сегодня"
    task = random.choice(RANDOM_TASKS)
    add_todo(date, task)
    text = f'Задача   "{task}"   добавлена на дату   {date}'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands = ["show", "print"])
def show(message):
    command = message.text.split()
    if len(command) < 2:
        text = "Вы не ввели дату задачи"
        bot.send_message(message.chat.id, text)
        return
    else:
        command = message.text.split(maxsplit = 1)
        date = command[1].lower()
        text = ""
    if date in tasks:
        text = date.upper() + "\n"
        for task in tasks[date]:
            text = text + "[] " + task + "\n"
    else:
        text = "Задач на эту дату нет"

    bot.send_message(message.chat.id, text)

# try:
#     bot.send_message(message.chat.id, )
# except:

bot.polling(none_stop = True)



python
import telebot
from telebot import types

API_TOKEN = 'YOUR_API_TOKEN'
bot = telebot.TeleBot(API_TOKEN)

tasks = {}  # Словарь для хранения задач

@bot.message_handler(commands=['add'])
def add_task(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Введите дату задачи (например, 31.12.2022):")
    bot.register_next_step_handler(message, get_date)

def get_date(message):
    chat_id = message.chat.id
    date = message.text
    tasks[date] = ""
    bot.send_message(chat_id, "Введите текст задачи:")
    bot.register_next_step_handler(message, get_task)

def get_task(message):
    chat_id = message.chat.id
    task_text = message.text
    date = list(tasks.keys())[-1]  # Получаем последнюю введенную дату
    tasks[date] = task_text
    bot.send_message(chat_id, f"Задача {task_text} добавлена в список на {date}")

bot.polling()
