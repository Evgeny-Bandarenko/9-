import random


# С клавиатуры вводится
# 7мизначное число.
# Если четных цифр в нем
# больше, чем нечетных, то
# найти сумму всех цифр.
# Если нечетных больше, чем
# четных, то найти
# произведение 1, 3 и 6 цифр

# n = int(input())
# numbers = [n // 1000000, (n // 100000) % 10, (n // 10000) % 10, (n // 1000) % 10, (n // 100) % 10, (n // 10) % 10,
#            n % 10]
# chet = 0
# nechet = 0
#
# for number in numbers:
#     if number % 2 == 0:
#         chet += 1
#     else:
#         nechet += 1
#
# if chet > nechet:
#     print(sum(numbers))
# else:
#     print(numbers[0] * numbers[2] * numbers[5])

# С клавиатуры вводится строка.
# Если количество согласных и
# гласных в ней одинаково, то
# выведите на экран все гласные
# буквы

# str = input("Ведите строку ").upper()
# gl = "A, E, I, O, U, Y"
# soglas = " B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, W, X, Z"
# g = 0
# sog = 0
# cons = 0
# v = []
# for i in str:
#     if i in gl:
#        g += 1
#     if i in str:
#        if i in soglas:
#         sog += 1
#         v.append(i)
# if g < sog or g > sog:
#     print("Не равное количество гласных и согласных")
# elif g == sog:
#     print(v)
#
    # for i in str:
    #     if i in gl:
    #         print(i, end=" ")

# С клавиатуры вводятся 2 числа
# a и b и генеруется 2 числа
# рандомно r1 и r2. Все числа от
# 1 до 20.
# Посчитать сколько раз a > r1
# and b > r2.
# Проверку выполнить 6 раз.
# В случае равенства
# (когда a, b больше 3 раза и r1,
# r2 больше 3 раза) вывести на
# печать рандомные числа,
# полученные в 4 итерации.


# iter = 1
# re = 0
# re1 = 0
# ir1 = 0
# ir2 = 0
# while iter <=6:
#     a = int(input())
#     b = int(input())
#     r1 = random.randint(1, 20)
#     r2 = random.randrange(1, 21)
#     if a > r1 and b > r2:
#         re += 1
#     elif a < r1 and b < r2:
#         re1 += 1
#     if iter == 4:
#         ir1 = r1
#         ir2 = r2
#     iter += 1
#
# if re == re1:
#     print(re, re1)
#     print(f"Рандомные числа полученые в 4 итерации:{ir1, ir2}")


# s = input("Введите строку:")
# vowels = set("1234567890")
# for letter in s:
#     if letter in vowels:
#
#         print(letter, end=" ")

# Вводится строка, содержащая буквы, цифры, пробелы и прочие символы.
# Посчитайте: - Сколько пар букв (стоятрядом) верхнего регистра
# - Сколько пар букв (стоятрядом) нижнего регистра
# - Сколько согласных букв
# - Сколько гласных букв
# - Сколько всего букв

# str = input("Ведите строку ")
# gl = "AaEeIiOoUuYy"
# soglas = " BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxZz"
# pair_down = 0
# pair_large = 0
# cons = 0
# cons_1 = 0
# cons_2 = 0
#
# for i in range(1, len(str)):
#     if str[i - 1].islower() and str[i].islower():
#        pair_down += 1
# print("Всего пар нижнего регистра",pair_down)
# for i in range(1, len(str)):
#     if str[i - 1].isupper() and str[i].isupper():
#         pair_large += 1
# print("Всего пар верхнего регистра",pair_large)
# for i in str:
#     if i.isalpha() and i in soglas:
#         cons += 1
# print("В строке согласных букв", cons)
# for i in str:
#     if i.isalpha() and i in gl:
#         cons_1 += 1
# print("В строке гласных букв", cons_1)
# for i in str:
#     if i.isalpha():
#         cons_2 += 1
# print("В строке букв", cons_2)


# text = input()
# vowels = "eyuoia"
# pair_up, pair_down, cons, vows = 0, 0, 0, 0
# for i in range(1, len(text)):
#     if text[i-1].islower() and text[i].islower():
#         pair_down += 1
#     elif text[i-1].isupper() and text[i].isupper():
#         pair_up += 1
#
# for i in text:
#     if i.isalpha() and i in vowels:
#         vows += 1
#     else:
#         cons += 1
# print(f'''Пар верхнего регистра: {pair_up}
# Пар нижнего регистра: {pair_down}
# гласных букв {vows}
# согласных букв {cons}
# всего букв {vows + cons}''')

# num = int(input("Какую цифру будем искать:"))
# how = int(input("Сколько раз будем искать:"))
# c = 0
# iter = 1
# while iter <= how:
#     r = random.randint(1, 21)
#     print(r)
#     while r != 0:
#         last = r % 10
#         if last == num:
#             c += 1
#         r = r // 10
#     iter += 1
# print(c)


# Вводится строка, содержащая буквы, цифры, пробелы и прочие символы.
# Посчитайте:
# - Сколько пар букв (стоят рядом) верхнего регистра
# - Сколько пар букв (стоят рядом) нижнего регистра
# - Сколько согласных букв
# - Сколько гласных букв
# - Сколько всего букв
# text = input()
# vowels = "eyuoia"
# pair_up, pair_down, cons, vows = 0, 0, 0, 0
# for i in range(1, len(text)):
#     if text[i-1].islower() and text[i].islower():
#         pair_down += 1
#     elif text[i-1].isupper() and text[i].isupper():
#         pair_up += 1
#
#     if text[i - 1].isalpha():
#         if text[i-1].lower() in vowels:
#             vows += 1
#         else:
#             cons += 1
# print(f'''Пар верхнего регистра: {pair_up}
# Пар нижнего регистра: {pair_down}
# гласных букв {vows}
# согласных букв {cons}
# всего букв {vows + cons}''')





