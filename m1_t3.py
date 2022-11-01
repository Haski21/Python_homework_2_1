'''
Задача №1. Посчитать размер вклада на счете за несколько лет.

Вход:
размер начального вклада (от 100 до 1_000_000 рублей), (float)
годовой процент начисления(от 1 до 20) с ежегодной капитализацией, (float)
количество лет по вкладу(от 1 до 100) - целые значения

Выход: итоговая сумма на счету.
Добавить проверки. Можно использовать float.
Решить задачу с циклом и без цикла.
'''

invest = float(input('first invest:'))
persent = float(input('persent is:'))
years = int(input('How much years:'))

if 99 < invest < 1_000_001 and 0 < persent < 21 and 1 < years < 101:
    print('0 year:', invest)
    a = 1
    while years:
        invest += invest // persent
        print(a, 'year:', invest)
        a += 1
        years -= 1
else: print('not true value')

#не моу понять, почему не работает round
print(round(invest * (1 + persent / 100) ** years, 5))
