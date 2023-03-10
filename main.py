import random
from words import *

def get_word():
    return random.choice(word_list)

def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',

                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    print(stages[tries])

guessed_words = []
def play(word):
    word_completion = ''
    guessed = False
    guessed_letters = []
    tried_letters = []
    tries = 6

    while word not in guessed_words:
        display_hangman(tries)

        if tries == 0:
            print('У вас скінчилися спроби. Загадане слово:', word.upper())
            break
        
        word_completion = ''
        for i in range(len(word)):
            if word[i] in guessed_letters:
                word_completion += word[i]
            else:
                word_completion += '_'
        print(word_completion.upper())

        if word_completion == word:
            guessed = True

        while guessed == False:
            c = input('Уведіть літеру: ')
            if c.isalpha() == False and c != "'":
                print('Неправильний ввід. Символ не є літерою. Спробуйте ще раз.')
                continue
            elif c in guessed_letters or c in tried_letters:
                print('Неправильний ввід. Такий символ вже був. Спробуйте ще раз.')
                continue
            elif c in guessed_words:
                print('Неправильний ввід. Це слово вже відгадано. Спробуйте ще раз.')
                continue
            break
        
        while guessed == False:
            if len(c) == 1:
                if c in word:
                    guessed_letters.append(c)
                    print('Ви вгадали літеру!')
                    break
                else:
                    tries -= 1
                    tried_letters.append(c)
                    print('Ви не вгадали! У вас залишилось', tries, 'спроб.')
                    break
            else:
                if c == word:
                    guessed = True
                else:
                    tries -= 1
                    print('Ви не вгадали! У вас залишилось', tries, 'спроб.')
                    break
        else:
            guessed_words.append(word)
            print('Вітаємо! Слово відгадано! Кількість відгаданих слів: ', len(guessed_words))
        
    if input('Чи хочете спробувати зіграти ще? (+ или -): ') == '+':
        play(get_word())

if __name__ == '__main__':
    print('Гра починається!')
    play(get_word())