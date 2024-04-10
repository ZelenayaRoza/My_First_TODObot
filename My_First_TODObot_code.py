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
