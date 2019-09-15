#coding UTF-8

#Тренировочная программа-игра для отработки навыков написания кода Python

import random
import sys

print('Здравствуйте! Пожалуйста, отгадайте число, загаданное мной.')
print('')

def game_main():
    a = random.randint(1, 100)
    def int_check():
        x = int(input('Какое число я загадал? '))
        if x > a:
            print('Меньше!')
            int_check()
        elif x < a:
            print('Больше!')
            int_check()
        else:
            print('Угадали!!!')
            b = input('Сыграем ещё? Y/N ')
            if b == 'Y':
                game_main()
            else:
                sys.exit()
            game_main()
    int_check()

game_main()
