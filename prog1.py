# coding UTF-8

# Программа - финансовый помощник, универсальное консольное приложение для различных финансовых расчётов.

import sys
import random
import math

def main_menu():
    print('Выберите один из вариантов: ')
    print('***|||***|||***')
    print('1) Рассчитать процент от суммы')
    print('2) Рассчитать ежемесячный доход от годового процента')
    print('2) Рассчитать ежедневный доход от годового процента')
    print('')
    print('0) Выход из приложения')
    print('')
    print('***|||***|||***')

    def variant():
        variant = input('Введите номер пункта меню: ')
        return variant

    variant = variant()

    return variant

def procent():
    summa = input('Введите сумму: ')
    proc = input('Введите процент: ')
    result = int(summa) / 100 * int(proc)
    print('Процент от суммы равен ', result)
    print('')

print('Здравствуйте! Я - финансовый помощник.')
print('***|||***|||***')
print('Показать вам, что я могу?')
print('')

def vibor():
    variant = main_menu()
    if variant == '0':
        print('До новых встреч!')
        sys.exit()
    elif variant == '1':
        print('Рассчитаем процент от суммы.')
        procent()
        vibor()
    else:
        print('')
        print('******************')
        print('Неправильный ввод!')
        print('******************')
        print('')
        vibor()

vibor()
