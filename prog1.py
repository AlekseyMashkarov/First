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

    def variant():
        variant = input('Введите номер пункта меню: ')
        return variant

    variant = variant()

    return variant

print('Здравствуйте! Я - финансовый помощник.')
print('***|||***|||***')
print('Показать вам, что я могу?')
print('')

variant = main_menu()

if variant == 0:
    print('До новых встреч!')
    sys.exit()
