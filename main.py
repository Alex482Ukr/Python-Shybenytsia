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
            print('?? ?????? ???????????????????? ????????????. ???????????????? ??????????:', word.upper())
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
            c = input('?????????????? ????????????: ')
            if c.isalpha() == False and c != "'":
                print('???????????????????????? ????????. ???????????? ???? ?? ??????????????. ?????????????????? ???? ??????.')
                continue
            elif c in guessed_letters or c in tried_letters:
                print('???????????????????????? ????????. ?????????? ???????????? ?????? ??????. ?????????????????? ???? ??????.')
                continue
            elif c in guessed_words:
                print('???????????????????????? ????????. ???? ?????????? ?????? ??????????????????. ?????????????????? ???? ??????.')
                continue
            break
        
        while guessed == False:
            if len(c) == 1:
                if c in word:
                    guessed_letters.append(c)
                    print('???? ?????????????? ????????????!')
                    break
                else:
                    tries -= 1
                    tried_letters.append(c)
                    print('???? ???? ??????????????! ?? ?????? ????????????????????', tries, '??????????.')
                    break
            else:
                if c == word:
                    guessed = True
                else:
                    tries -= 1
                    print('???? ???? ??????????????! ?? ?????? ????????????????????', tries, '??????????.')
                    break
        else:
            guessed_words.append(word)
            print('??????????????! ?????????? ??????????????????! ?????????????????? ???????????????????? ????????: ', len(guessed_words))
        
    if input('???? ???????????? ???????????????????? ?????????????? ????? (+ ?????? -): ') == '+':
        play(get_word())

if __name__ == '__main__':
    print('?????? ??????????????????????!')
    play(get_word())