from telebot import TeleBot
import random

words = []
lifes = 8
with open(r'/Users/bot1nok/PycharmProjects/Telegram-bot/words', encoding='utf-8') as file:
    for line in file:
        words.append(line.rstrip())
random_word = random.choice(words)
word = {}
for i in random_word:
    word[i] = False
link = open(r'api.txt')
bot = TeleBot(link.readline())


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, 'Добро пожаловать в игру <Виселица>, чтобы начать играть начните вводить буквы (не повторяйтесь)')


@bot.message_handler(content_types=['text'])
def receive_message(msg):
    if msg != 'start':
        global word, lifes
        flag = True
        for letter, isopen in word.items():
            if msg.text == letter and isopen == False:
                flag = False
                word[letter] = True
                bot.send_message(msg.chat.id, f'Поздравляю вы угадали букву {msg.text}')
        end = True
        if flag:
            lifes -= 1
            if lifes == 0:
                end = False
                bot.send_message(msg.chat.id, 'Вы проиграли!')
                bot.send_message(msg.chat.id, f'Правильное слово было {random_word}')
            else:
                bot.send_message(msg.chat.id, 'Такой буквы в слове нету')
                if lifes == 1:
                    bot.send_message(msg.chat.id, f'У вас осталось {lifes} жизнь')
                elif lifes >= 2 and lifes <= 4:
                    bot.send_message(msg.chat.id, f'У вас осталось {lifes} жизни')
                else:
                    bot.send_message(msg.chat.id, f'У вас осталось {lifes} жизней')
        if end:
            ans_string = ''
            for i in random_word:
                if word[i] == True:
                    ans_string += i
                else:
                    ans_string += '_'
            bot.send_message(msg.chat.id, ans_string)


if __name__ == '__main__':
    bot.polling(none_stop=True)
