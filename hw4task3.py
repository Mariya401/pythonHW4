"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""
# With SORT

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))


def my_func(a, b, c):
    lst = list()
    lst.append(a)
    lst.append(b)
    lst.append(c)
    lst.sort()
    return lst[1] + lst[2]


print(f'Cумма наибольших двух чисел: {my_func(num1, num2, num3)}')

# Without SORT

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))


def my_func(a, b, c):
    if a < b:
        return b + c
    elif b < a:
        return a + c
    else:
        return a + b


print(f'Cумма наибольших двух чисел: {my_func(num1, num2, num3)}')
