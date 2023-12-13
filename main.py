
# # Введите число, пока не введут 0. Найти произведение чисел, оканчивающихся на 4.
# mult = 1
# number = int(input("Введите число"))
# while number != 0:
#     if number % 10 == 4:
#         mult *= number
#     number = int(input("Введите число"))
# if mult == 1:
#     mult = 0
# print(mult)

# # Вводятся строки, пока не будет введена пустая строка. Если длина очередного введеного слова равна 5, то
# # нужно вывести сообщение "YES" и прекратить возможность ввода для пользователя, если таких слов нет, то
# # вывести 'NO' один раз в конце.

# flag = True
# while True:
#     some_str = input("Ведите слово: ")
# # if some_str == '':
# # break
#     if not some_str:
#         break
#     if len(some_str) == 5:
#         print('YES')
#         flag = False
#         break
# if flag:
#     print('NO')



# # 100 раз вывести слово hello в консоль

# i = 1
# while i <= 100:
#     print('Hello')
#     i += 1

# for _ in range(100): # 0, 1, 2, 3, 4, 5, 6, 7, 8...99
#     print('Hello')


# Вводится количество чисел, затем сами числа, если число = 10, вывести YES и закончить ввод,
# в конце вывести NO если никакое из чисел не было равно 10.
# n = int(input('Введите кол-во чисел: '))
# for _ in range(n):
#     number = int(input())
#     if number == 10:
#         print('YES')
#         break
# else:
#     print('NO')

# # Вводится количество чисел, затем сами числа. Найти сумму чисел, кратных 3
# n = int(input("Введите количество чисел: "))
# summa = 0
# for _ in range(n):
#     number = int(input("Введите число"))
#     if number % 3 ==0:
#         summa += number
# print(summa)

# Задача 1. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while

# n = int(input("Введите число: "))
# i = 1
# N = 1
# while i <= n:
#     N = i * N
#     i = i + 1
# print(N)


# Задача 2. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# a = int(input("Введите число > 1: "))
# fibsum = 0
# fib1 = 0
# fib2 = 1
# i = 2
# while fibsum < a:
#     fibsum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fibsum
#     i = i + 1

# if fibsum == a:
#     print(i)
# else:
#     print("-1")


# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил 
# купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз 
# потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# num = int(input("Введите колич арбузов: "))
# max = int(input("Введите вес арбуза: "))
# min = max
# for _ in range(num):
#     mas = int(input("Введите вес арбуза: "))
#     if mas > max:
#         max = mas
#     if mas <= min:
#         min = mas
# print(max)
# print(min)
    

# some_list = [1, 2, 3, 4, 5, 6]

# # Вывести все элементы списка в столбик
# for element in some_list:
#     print(element)

# # Сравнивать элементы списка
# count = 0
# for ind in range(1, len(some_list)):
#     if some_list[ind] > some_list[ind - 1]:
#         count += 1
# print(count)



# # Задача №17.
# # Дан список чисел. Определите, сколько в нем 
# # встречается различных чисел.
# # Input: [1, 1, 2, 0, -1, 3, 4, 4]
# # Output: 6

# n =int(input("Введите количество элементов: "))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input("Введите элемент: ")))
# print(some_list)

# new_list = []
# for elem in some_list:
#     if elem not in new_list:
#         new_list.append(elem)
# print(len(new_list))

# # # 19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю 
# # # последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.   
# n = int(input("Введите количество чисел в последовательности n: "))
# k = int(input("Введите число на котор нужно сдвинуть: "))

# some_list = []
# for _ in range(n):
#     some_list.append(int(input("Введите элемент: ")))
# print(some_list)

# x = some_list[:k]
# y = some_list[k:]
# z = y + x
# print(z)

# # 23. Дан массив, состоящий из целых чисел. Напишите программу,
# #  которая подсчитает количество элементов массива,
# #  больших предыдущего (элемента с предыдущим номером)

# n = int(input("Введите количество чисел в списке: "))
# some_list = []
# for _ in range(n):
#     some_list.append(int(input("Введите элемент: ")))
# print(some_list)
# count = 0
# for ind in range(1, len(some_list)):
#     if some_list[ind] > some_list[ind-1]:
#         count += 1
# print(count)


##1 Создайте список из 10 четных чисел и выведите его с помощью цикла for
# list1 = list(range(1,11))
# for numbers in list1:
#     print(numbers)

##2 Создайте список из 5 элементов. Сделайте срез от второго индекса до четвертого
# list2 = list(range(6))
# print(list2)
# print(list2[2:5])

#3 Создайте пустой список и добавьте в него 10 случайных чисел и выведите их. В данной задаче нужно использовать функцию randint.
# k = 5
# list3 = []

# for _ in range(k):
#     from random import randint
#     n = randint(1, 10) # Случайное число от 1 до 10
#     list3.append(n)
# print(list3)

# #4 Удалите все элементы из списка, созданного в задании 3

# for ind in range(len(list3)):
#     list3.pop()
    
# print(list3)

# # 5.Создайте список из введенной пользователем строки и удалите из него символы 'a', 'e', 'o'

# str = "пора есть"
# list_new = list(str)
# print(list_new)

# list_new.remove("а")
# list_new.remove("е")
# list_new.remove("о")
# print(list_new)

# import random
# some_set = set()
# for _ in range(10**3):
#     some_set.add(random.randint(1, 1000))
# some_list = list(some_set)
# print(99 in some_list)

# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко; D,
# G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
# А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка; Й, Ы – 4 очка; Ж, З, Х, Ц, Ч – 5 очков; Ш, Э, Ю – 8 очков; Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.
# *Пример:* ноутбук, ответ: 12

# scrabble_dict = {1: 'A, E, I, O, U, L, N, S, T, R', 2: 'D, G', 3: 'B, C, M, P', 4: 'F, H, V, W, Y'}
# some_str = input()
# summa = 0

# for letter in some_str:
#   for key in scrabble_dict:
#    if letter in scrabble_dict[key]:
#     summa += key
# print(summa)

# Второй способ (более оптимальный)
# scrabble_dict = {'A': 1, 'E': 1, 'I': 1}
# some_str = input()
# summa = 0

# for letter in some_str:
#   summa += scrabble_dict[letter]
# print(summa)


# 25. Напишите программу, которая принимает на вход строку,
# и выводит на экран кол-во повторений каждого из символов

# Ввод: как дела
"""k - 2
а - 2
д - 1
е - 1
л - 1
"""

# some_dict = {}
# word = input()
# for letter in word:
#   if letter not in some_dict:
#     some_dict[letter] = 1
#   else:
#     some_dict[letter] += 1
# print(some_dict)

# word = input()
# for letter in word:
#     print(f"{letter} - {word.count(letter)}")

# word = input()
# used = set()
# for letter in word:
#   if letter not in word:
#     print(f"{letter} - {word.count(letter)}")
#   used.add(letter)



# 1
# n = int(input("Введите число n: "))

# for elements in range(0, n+1):
#     print(elements)


# 2
# n = int(input("Введите число n: "))
# k = int(input("Введите число k: "))

# for elements in range(k, n+1):
#     print(elements)


# 3
# n = int(input("Введите число n: "))
# k = int(input("Введите число k: "))
# sum = 0
# for item in range(k, n+1):
#     sum += item
# print(sum)

# 4
# n = int(input("Введите число n: "))
# k = int(input("Введите число k: "))
# sum = 0
# for item in range(k, n+1):
#     if item%2 == 0:
#        sum += item
# print(sum)

#5
# Пользователь вводит число N. Найдите сумму чисел: 1 + 1.1 + 1.2 + 1.3 + ... + (1 + N / 10).

# n = int(input("Введите число n: "))
# sum = 1
# for i in range(1, n + 1):
#   sum += 1 + i/10
# print(sum)

# # print(sum(1 + i / 10 for i in range(1, int(input()) + 1)))

# n = input()
# print("Привет,", n)



# a = input()
# b = input()
# c = input()
# d = input()
# print(b,c,d,sep=a)

# a = int(input())
# b = int(input())
# c = int(input())
# print(a+b+c)

# a = int(input())
# V = a*a*a
# S = 6*a*a
# print("Объем = ", V)
# print("Площадь полной поверхности = ", S)

# a = int(input())
# b = int(input())
# f = 3*(a+b)**3 + 275*b**2 - 127*a - 41
# print(f)



# a = int(input())
# b = int(input())
# print(a, '+', b, '=', a+b)
# print(a, '-', b, '=', a-b)
# print(a, '*', b, '=', a*b)

# a1 = int(input())
# d = int(input())
# n = int(input())
# an = a1 + d * (n - 1)
# print(an)

# x = int(input())
# print(x, 2*x, 3*x, 4*x, 5*x, sep="---")

# a = 15 // (16 % 7)
# b = 34 % a * 5 - 29 % 5 * 2
# print(a + b)

# a = 82 // 3 ** 2 % 7
# print(2 % 7)

# b1 = int(input())
# q = int(input())
# n = int(input())
# bn = b1 * q**(n-1)
# print(bn)

# a = int(input())
# b = a//100
# print(b)

# n = int(input())
# k = int(input())
# a = k//n
# b = k%n
# print(a)
# print(b)

# n = int(input())
# n1 = n % 2
# n2 = n//2 + n1
# print(n2)

# n = int(input())
# n = n*(-1)
# n1 = n//4
# n1 = n1*(-1)
# print(n1)

# n = int(input())
# n1 = n //60
# n2= n%60
# print(n, 'мин', '-', 'это', n1, 'час', n2, 'мин')

# Задача 2. Напишите программу, в которой рассчитывается сумма цифр двузначного числа.
# n = int(input("Введите двухзначное число"))
# n1 = n%10
# n2 = n // 10
# print(n1+n2)

# Задача 3. Напишите программу, которая печатает число, образованное при перестановке цифр двузначного числа.
# n = int(input("Введите двухзначное число"))
# n1 = n%10
# n2 = n // 10
# num = n1*10 + n2
# print(num)

# Задача 4. Напишите программу, в которую вводится трёхзначное число и которая выводит на экран его цифры (через запятую).
# n = int(input("Введите трехзначное число"))
# n3 = n%10
# n2 = (n//10)%10
# n1 = n//100
# print(n1, n2, n3, sep=',')

# n = int(input())
# n3 = n%10
# n2 = (n//10)%10
# n1 = n//100
# print(n1,n2,n3, sep='')
# print(n1,n3,n2,sep='')
# print(n2,n1,n3,sep='')
# print(n2,n3,n1,sep='')
# print(n3,n1,n2,sep='')
# print(n3,n2,n1,sep='')


# n = int(input())
# n4 = n%10
# n3 = (n//10)%10
# n2 = (n//100)%10
# n1 = (n//1000)
# print("Цифра в позиции тысяч равна",n1)
# print("Цифра в позиции сотен равна",n2)
# print("Цифра в позиции десятков равна",n3)
# print("Цифра в позиции едениц равна",n4)

# a = 17 // (23 % 7)
# b = 34 % a * 5 - 29 % 4 * 3
# print(b)


# print("*****************")
# print("*","*",sep='               ')
# print("*","*",sep='               ')
# print("*****************")

# a=int(input())
# b=int(input())
# print("Квадрат суммы", a, 'и', b, 'равен',(a+b)**2)
# print("Сумма квадратов", a, 'и', b, 'равна', a**2+ b**2)

# a=int(input())
# b=int(input())
# c=int(input())
# d=int(input())
# print(a**b + c**d)

# n = input()
# n1 = n +n
# n2 = n+n+n
# print(int(n)+int(n1)+int(n2))

# answer = input('Какой язык программирования мы изучаем?')
# if answer == 'Python':
#     print('Верно! Мы ботаем Python =)')
#     print('Python - отличный язык!')

# Задача 3. Напишите программу, которая считывает три числа и подсчитывает количество чётных чисел.

# answer = int(input('Введите три числа'))
# count = 0
# num3 = answer % 10
# num2 = answer // 10 % 10
# num1 = answer// 100

# if num1 % 2 == 0:
#     count += 1
# if num2 % 2 == 0:
#     count += 1
# if num3 % 2 == 0:
#     count += 1
# print(count)

# pasw = input('Введите пароль')
# pasw2 = input('Повторите пароль')
# if pasw == pasw2:
#     print("Пароль принят")
# else:
#     print("Пароль не принят")

# num = int(input())
# if num % 2 == 0:
#     print("Четное")
# else:
#     print("Нечетное")

# Напишите программу, которая проверяет, что для заданного четырехзначного числа 
# выполняется следующее соотношение: сумма первой и последней цифр равна разности второй и третьей цифр.
# num = int(input())
# num4 = num % 10
# num3 = num // 10 % 10
# num2 = num // 100 % 10
# num1 = num // 1000
# if num1 + num4 == num2 - num3:
#     print("ДА")
# else:
#     print("НЕТ")

# Напишите программу, которая определяет, разрешен пользователю доступ к интернет-ресурсу или нет.
# Формат выходных данных
# Программа должна вывести текст «Доступ разрешен» если возраст не менее 18, и «Доступ запрещен» в противном случае.

# age = int(input())
# if age >= 18:
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# if num3-num2 == num2 - num1:
#     print('YES')
# else:
#     print("NO")

# num1 = int(input())
# num2 = int(input())
# if num1 < num2:
#     min = num1
# if num2 < num1:
#     min = num2
# print(min)

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# num4 = int(input())
# min = num1
# if num2 < min:
#     min = num2
# if num3 < min:
#     min = num3
# if num4 < min:
#     min = num4
# print(min)

# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится:

# до 13 включительно – детство;
# от 14 до 24 – молодость;
# от 25 до 59 – зрелость;
# от 60 – старость.

# age = int(input())
# if age <= 13:
#     print("детство")
# if  14 <= age <= 24: 
#     print("молодость")
# if 25 <= age <= 59:
#     print("зрелость")
# if age >= 60:
#     print("старость")   

# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
# sum = 0

# if num1 > 0:
#     sum += num1

# if num2 > 0:
#     sum += num2

# if num3 > 0:
#     sum += num3
# print(sum)

# # Задача 1. Напишите программу, которая определяет, является ли заданное натуральное число трёхзначным.
# num = int(input())
# if num // 100 > 0 and num // 100 < 10:
#     print("yes")
# else:
#     print("no")

# # Задача 2. Напишите программу, которая проверяет, что все три цифры натурального трёхзначного числа различны.
# num = int(input())
# num3 = num % 10
# num2 = num // 10 % 10
# num1 = num // 100
# print(num1,num2,num3)

# if num1 != num2 != num3:
#     print("различны")
# else:
#     print("есть одинаковые")

# Задача 3. Напишите программу, которая по координатам точки, не лежащей на осях координат, определяет номер координатной четверти, в которой она находится.
# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print("1")
# if x > 0 and y < 0:
#     print("4")
# if x < 0 and y < 0:
#     print("3")
# if x < 0 and y > 0:
#     print("2")

# x = int(input())
# if (x > -30 and x <= -2) or (x > 7 and x <= 25):
#     print("Принадлежит")
# else:
#     print("Не принадлежит")

# num = int(input())
# if num >= 1000 and num < 10000 and num % 7 == 0 or num % 17 == 0:
#     print("YES")
# else:
#     print('NO')

# num1 = int(input())
# if (num1 % 4 == 0 and num1 % 100 != 0) or num1 % 400 == 0:
#    print('YES')
# else:
#    print("NO")

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# if (-1 <= a-c <= 1) and (-1 <= b-d <= 1):
#     print('YES')
# else:
#     print("NO")

# Задача 1. Даны три целых числа. Определите, сколько среди них совпадающих. Программа должна вывести одно из чисел: 3 (если все совпадают),
#  2 (если два совпадает) или 0 (если все числа различны).

# Если Зум быстрее Флэша нужно вывести «NO», если Флэш быстрее Зума нужно вывести «YES», если их скорости равны нужно вывести "Don't know".

# n, k = int(input()), int(input())

# if n > k:
#     print("NO")
# elif k > n:
#     print("YES")
# else:
#     print("Don't know")

# a, b, c = int(input()), int(input()), int(input())
# if a==b and b==c:
#     print("Равносторонний")
# elif a==b or b==c or a==c:
#     print("Равнобедренный")
# else:
#     print("Разносторонний")

# a, b, c = int(input()), int(input()), int(input())
# if c > a > b:
#     print(a)
# elif a > b > c:
#     print(b)
# elif b > c > a:
#     print(c)
# elif c > b > a:
#     print(b)
# elif b > a > c:
#     print(a)
# elif a > c > b:
#     print(c)

# n = int(input())
# if n >= 64:
#     print("Полусредний вес")
# elif n >= 60:
#     print("Первый полусредний вес")
# else:
#     print("Легкий вес")

# if sim != "+" and sim != "-" and sim != "*" and sim != "/":
#     print("Неверная операция")

#  (+, -, *, /)
# a, b = int(input()), int(input())
# sim = input()
# if sim == "+":
#     print(a+b)
# elif sim == "-":
#     print(a-b)
# elif sim == "*":
#     print(a*b)
# elif sim == "/":
#    if b!=0:
#       print(a/b)
#    else:
#       print("На ноль делить нельзя!")
# else:
#     print("Неверная операция")  

# c1 = input()   
# c2 = input()
# if (c1 == "красный" and c2 == "синий") or (c1 == "синий" and c2 == "красный"):
#    print("фиолетовый")
# elif (c1 == "красный" and c2 == "желтый") or (c1 == "желтый" and c2 == "красный"):
#    print("оранжевый")
# elif (c1 == "синий" and c2 == "желтый") or (c1 == "желтый" and c2 == "синий"):
#    print("зеленый")
# elif c1 == "красный" and c2 == "красный":
#    print("красный")
# elif c1 == "синий" and c2 == "синий":
#    print("синий")
# elif c1 == "желтый" and c2 == "желтый":
#    print("желтый")
# else:
#    print("ошибка цвета")


# карман 0 зеленый;

# для карманов с 1 по 10 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;
# для карманов с 19 по 28 карманы с нечетным номером имеют красный цвет, карманы с четным номером – черный;

# для карманов с 11 по 18 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный;
# для карманов с 29 по 36 карманы с нечетным номером имеют черный цвет, карманы с четным номером – красный.

# Напишите программу, которая считывает номер кармана и показывает, является ли этот карман зеленым, красным или черным. 
# Программа должна вывести сообщение об ошибке, если пользователь вводит число, которое лежит вне диапазона от 0 до 36.
# num = int(input())
# if num > 36 or num < 0:
#    print("ошибка ввода")
# if num == 0:
#    print("зеленый")  
# elif 10 >= num >=1 or 28 >= num >= 19:
#    if num % 2 == 0:
#       print("черный")
#    else:
#       print("красный")
# elif 18 >= num >=11 or 36 >= num >= 29:
#    if num % 2 == 0:
#       print("красный")
#    else:
#       print("черный")

# p1, p2, p3, p4 = int(input()), int(input()), int(input()), int(input())
# if (p2 < p3 and p1 < p4) or (p3 < p1 and p4 < p1):
#     print("пустое множество")
# elif p3 == p2:
#         print(p2)
# elif p1 == p4:
#      print(p1)
# elif p2 > p3 and p2 < p4 and p1 < p3:
#     print(p3, p2)
# elif p2 > p3 and p2 > p4 and p1 < p3:
#      print(p3, p4)
# elif p1 > p3 and p2 < p4:
#      print(p1, p2)
# elif p1 > p3 and p2 == p4:
#      print(p1, p2)
# elif p1 < p3 and p2 == p4:
#      print(p3, p2)
# elif p1 > p3 and p4 < p2:
#      print(p1, p4)
# elif p1 == p3 and p4 > p2:
#      print(p1, p2)

# n = int(input())
# if n % 100 == 0:
#     print("YES")
# else:
#     print("NO")

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
# if ((x1 + y1) % 2 == 0 and (x2 + y2) % 2  == 0) or ((x1 + y1) % 2  == 1 and (x2 + y2) % 2  == 1):
#     print("YES")
# else:
#     print("NO")

# v = int(input())
# g = input()
# if 15 >= v >= 10 and g == "f":
#     print("YES")
# else:
#     print("NO")
# n = int(input())
# if n == 1:
#     print("I")
# elif n == 2:
#     print("II")
# elif n == 3:
#     print("III")
# elif n == 4:
#     print("IV")
# elif n == 5:
#     print("V")
# elif n == 6:
#     print("VI")
# elif n == 7:
#     print("VII")
# elif n == 8:
#     print("VII")
# elif n == 9:
#     print("IX")
# elif n == 10:
#     print("X")
# else:
#     print("ошибка")

# если число нечётное, то вывести «YES»;
# если число чётное в диапазоне от 2 до 5 (включительно), то вывести «NO»;
# если число чётное в диапазоне от 6 до 20 (включительно), то вывести «YES»;
# если число чётное и больше 20, то вывести «NO».
# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input()),
# if (x1 + x2) == (y1 + y2) or (x2 - x1)**2 == (y2 - y1)**2:
#     print("YES")
# else:
#     print("NO")


# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input()),
# if ((x1 - x2)**2 == 1 and  (y1 - y2)**2 == 4) or ((x1 - x2)**2 == 4 and  (y1 - y2)**2 == 1):
#     print("YES")
# else:
#     print("NO")

# x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input()),
# if x1 == x2 or y1 == y2:
#     print("YES")
# elif ((x1-x2)**2 > 1 or (y1-y2)**2 > 1) and ((x1 - x2)**2 != (y1 - y2)**2):
#     print("NO")
# else:
#     print("YES")

# x1, x2 = float(input()), float(input())
# print(1/2*x1*x2)

# S, V1, V2 = float(input()), float(input()), float(input())
# t = (S/(V1+V2))
# print(t)

# F = float(input())
# C = (5/9*(F - 32))
# print(C)

# num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
# print(num)

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print("Наименьшее число =", min(a,b,c,d,e))
# print("Наибольшее число =", max(a,b,c,d,e))

# a, b, c = int(input()), int(input()), int(input())
# maxim = a
# minim = a
# midem = a
# if b > a and b > c:
#      maxim = b
# elif c > a and c > b:
#      maxim = c
# if b < a and b < c:
#      minim = b
# elif c < a and c < b:
#      minim = c
# if b != maxim and b != minim:
#      midem = b
# elif c != maxim and c != minim:
#      midem = c
# print(maxim)
# print(midem)
# print(minim)

# a, b, c = int(input()), int(input()), int(input())
# print(max(a,b,c))
# print((a + b + c) - max(a,b,c) - min(a, b,c))
# print(min(a,b,c))

# num = int(input())
# a = num % 10
# b = (num %100)//10
# c = num // 100
# if max(a,b,c) - min(a,b,c) == (a + b + c) - max(a,b,c) - min(a, b,c):
#    print("Число интересное")
# else:
#    print("Число неинтересное")

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e)) 

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# print(abs(a - c) + abs(b - d))

# "Python is a great language!", said Fred. "I don't ever remember having this much fun before."
    
# print("\"Python is a great language!\", said Fred. \"I don't ever remember having this much fun before.\" ")

# name = input()
# surname = input()
# print("Hello", name, surname + "!", "You have just delved into Python")

# name = input()
# size = len(name)
# print(f"Футбольная команда {name} имеет длину {size} символов")

# name1 = input()
# name2 = input()
# name3 = input()
# if len(name1) > len(name2) and len(name1) > len(name3):
#     big = name1
# elif len(name2) > len(name1) and len(name2) > len(name3):
#     big = name2
# else:
#     big = name3
# if len(name1) < len(name2) and len(name1) < len(name3):
#     small = name1
# elif len(name2) < len(name1) and len(name1) < len(name3):
#     small = name2
# else:
#     small = name3
# print(small)
# print(big)

# name1 = input()
# name2 = input()
# name3 = input()
# first = min(len(name1), len(name2), len(name3))
# third = max(len(name1), len(name2), len(name3))
# second = (len(name1) + len(name2) + len(name3)) - (first + third)
# if second - first == third - second:
#     print("YES")
# else:
#     print("NO")

# s = input()
# if '@' in s and '.' in s:
#     print("YES")
# else:
#     print("NO")

# num1 = sqrt

# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())

# from math import *
# p = sqrt(pow((x1 - x2), 2) + pow((y1 - y2), 2))
# print(p)

# from math import *
# R = float(input())
# S = pi * pow(R, 2)
# C = 2 * pi * R
# print(S)
# print(C)

# from math import *
# a, b = float(input()), float(input())
# var1 = (a + b)/2
# var2 = sqrt(a * b)
# var3 = 2 * a * b / (a + b)
# var4 = sqrt((pow(a,2) + pow(b,2))/ 2)

# print(var1)
# print(var2)
# print(var3)
# print(var4)

# from math import *
# x = float(input())
# r = radians(x)
# trig = sin(r) + cos(r) + pow(tan(r), 2)
# print(trig)

# from math import *
# x = float(input())
# sum = ceil(x) + floor(x)
# print(sum)

# from math import *
# a, b, c = float(input()), float(input()), float(input())
# d = pow(b, 2) - 4 * a * c
# if d > 0:
#     x1 = (-b + sqrt(d)) / (2 * a)
#     x2 =  (-b - sqrt(d)) / (2 * a)
#     print(min(x1, x2))
#     print(max(x1, x2))
# elif d == 0:
#     x = -b / (2 * a)
#     print(x)

# elif d < 0:
#     print("Нет корней")

# from math import *
# n, a = int(input()), float(input())
# s = (n * (pow(a, 2))) / (4 * (tan(pi / n)))
# print(s)

# for i in range(5):
#     num = int(input())
#     print('Квадрат вашего числа равен:', num * num)
# print('Цикл завершен')

# for i in range(10):
#     print("Python is awesome!")

# sent = input()
# n = int(input())
# for i in range(n):
#     print(sent)

# for i in range(6):
#     print("AAA")
# for i in range(5):
#     print("BBBB")
# print("E")
# for i in range(9):
#     print("TTTTT")
# print("G")

# n = int(input())
# for _ in range(n):
#     print("*" * 19)

# n = int(input())
# for i in range(n+1):
#     print("Квадрат числа", i, "равен", pow(i, 2))

# n = int(input())
# for i in range(n):
#     print("*" * abs(i - n))

# a = int(input())
# b = int(input())
# c = int(input())

# for i in range(c):
#   print(i+1, (a * (b / 100 + 1)** i))

# a, b = int(input()), int(input())
# for a in range(b):
#     print(a+1)

# m, n = int(input()), int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# elif m > n:
#     for i in range(m, n-1, -1):
#         print(i)
# else:
#     print(m)


# m, n = int(input()), int(input())
# if m % 2 ==1:
#     for i in range(m, n-1, -2):
#         print(i)
# else:
#     for i in range(m-1, n-1, -2):
#         print(i)

# m, n = int(input()), int(input())
# for i in range(m, n+1):
#     if (i % 17 == 0) or (i % 10 == 9) or ((i % 3 == 0) and (i % 5 == 0)):
#         print(i)

# n = int(input())

# for i in range(1, 11):
#     print(f"{n} x {i} = {n*i}")

# Напишем программу, которая считывает 10 чисел и определяет сколько из них больше 10.
# count = 0
# for i in range(5,15):
#     if i > 10:
#         count = count + 1
# print(count)

# counter = 0
# for _ in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# Рассмотрим еще один пример: подсчитать количество чисел из диапазона 
# [
# 1
# ;
# 100
# ]
# [1;100], квадрат которых оканчивается на 4.

# count = 0
# for i in range(1,101):
#     if (pow(i,2) % 10 == 4):
#         count = count + 1
# print(count)

# counter = 0
# for i in range(1, 101):
#     if i**2 % 10 == 4:
#         counter = counter + 1
# print(counter)

# Напишем программу, которая считывает 10 чисел и определяет сумму тех из них, которые больше 10.

# sum = 0
# for _ in range(3):
#     num = int(input())
#     if num > 10:
#         sum = sum + num
# print(sum)

# Рассмотрим еще один пример: напишем программу, которая запрашивает 10 целых чисел и находит их среднее значение:
# med = 0
# n = 3
# for _ in range(n):
#     num = int(input())
#     med = num + med
# med = med/n
# print(med)

# maxim = 0
# for i in range(4):
#     num = int(input())
#     if num > maxim:
#         maxim = num
# print(maxim)

# total = 0
# for i in range(1, 6):
#     total += i
#     print(total, end='')

# count = 0
# a, b = int(input()), int(input())
# for i in range(a, b+1):
#     if ((pow(i, 3)) % 10 == 4) or ((pow(i, 3)) % 10 == 9):
#         count = count + 1
# print(count)

# sum = 0
# n = int(input())
# for i in range(n):
#     num = int(input())
#     sum += num
# print(sum)

# from math import *
# n = int(input())
# sum = 1
# for i in range(2, n+1):
#     sum = sum + 1/i
# ln = log(n)
# print(sum - ln)

# sum = 0
# n = int(input())
# for i in range(1, n+1):
#     if ((pow(i, 2)) % 10 == 2) or ((pow(i, 2)) % 10 == 5) or ((pow(i, 2)) % 10 == 8):
#         sum += i
# print(sum)

# n = int(input())
# fact = 1
# for i in range(1, n+1):
#     fact *= i
# pr
# fact = 1
# for i in range(10):
#     n = int(input())
#     if n != 0:
#         fact *= n
# print(fact)

# sum = 0
# n = int(input())
# for i in range(1, n+1):
#     if n % i == 0:
#         sum += i
# print(sum)

# total = 0
# n = int(input())
# for i in range(n):
#     if i % 2 == 0:
#         total += i + 1
#     else:
#         total -= i + 1
# print(total)

# max1 = 0
# max2 = 1
# n = int(input())
# for i in range(1, n+1):
#     num = int(input())
#     if num > max1:
#         max2 = max1
#         max1 = num
#     elif num > max2:
#         max2 = num
# print(max1)
# print(max2)

# n = int(input())
# x1 = 0
# x2 = 1

# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа равен:', num * num)
#     num = int(input())

# for i in range(0, 100, 3):
#     print(i)

# i = 0
# while i < 100:
#     print(i)
#     i += 3

# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)

# text = input()
# while text != "КОНЕЦ" and text != "конец":
#     print(text)
#     text = input()

# word = input()
# while word != "КОНЕЦ":
#     print(word)
#     word = input()

# i = 0
# text = input()

# while text != "стоп" and text != "хватит" and text != "достаточно":
#     i += 1
#     text = input()
# print(i)

# num = int(input())
# count = 0
# while num != 0:
#     while num >= 25:
#         num -= 25
#         count += 1
#     while num >= 10:
#         num -= 10
#         count += 1
#     while num >= 5:
#         num -= 5
#         count += 1
#     while num >= 1:
#         num -= 1
#         count += 1
# print(count)

# num = int(input())
# while num != 0:
#     num2 = num % 10
#     print(num2)
#     num = num // 10

# num = int(input())
# total = str()
# while num != 0:
#     num2 = num % 10
#     num3 = str(num2)
#     total += num3
#     num = num // 10

# print(total)

# num = int(input())
# largest = 0
# minim = num
# while num != 0:
#     num2 = num % 10
#     if num2 > largest:
#         largest = num2
#     if num2 < minim:
#         minim = num2
#     num = num // 10
# print("Максимальная цифра равна", largest)
# print("Минимальная цифра равна", minim)

# num = int(input())
# sum = 0
# count = 0
# fact = 1
# num3 = num
# while num != 0:
#     num1 = num % 10
#     sum += num1
#     count += 1
#     fact *= num1
#     last_dig = num
#     num = num // 10
    
# print(sum)
# print(count)
# print(fact)
# print(sum / count)

# num5 = num3 % 10
# while num3 != 0 and num3 >= 9:
#     num3 = num3 // 10
# print(num3+ num5)


# num = int(input())
# while num > 9:
#     num2 = num % 10
#     num = num // 10
# print(num2)

# num = int(input())
# flag = True
# while num > 9:
#     num2 = num % 10
#     num3 = (num % 100)//10
#     if num2 != num3:
#         flag = False 
#     num = num // 10
# if flag == True:
#     print("YES")
# else:
#     print("NO")

# n= int(input())
# n4 = n
# flag = False
# n3 = 0

# while n != 0:
#     n2 = n % 10
#     if n3 <= n2:
#         flag = True
#     else:
#         flag = False
#     n3 = n2
#     n = n // 10

# n4 = n4 /2

# if flag == True:
#     print('YES')
# else:
#     print('NO')

# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию
#     print(i)

# n = int(input())
# for i in range(2, 99999):
#     if n % i == 0:
#         break
# print(i)

# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)

# i = 1
# while i < 101:
#     if i % 7 == 0:
#         print(i)
#     i += 1

# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i)

# for i in range(100, 0, -1):
#     print(i)

# a = 1
# for i in range(1, 1001):
#     if i % 2 == 1:
#         a = a + 1
# print(a)

# sum = 0
# for i in range(1, 1001, 2):
#     sum += i
# print(sum)

# n = input()
# a = 0
# for i in range(n):
#     a = a * i
# print(a)

# На обработку поступает последовательность из 10 целых чисел. Нужно написать программу, 
# которая выводит на экран количество неотрицательных чисел последовательности и их произведение.
#  Если неотрицательных чисел нет, требуется вывести на экран «NO». Программист торопился и написал программу неправильно.

# mult = 1
# count = 0

# for i in range(3):
#     num = int(input())
#     if num >= 0:
#         mult *= num
#         count += 1
# if count > 0:
#     print(count)
#     print(mult)
# else:
#     print("NO")

# count = 0
# p = 1
# for i in range(10):
#     x = int(input())
#     if x >= 0:
#         p *= x
#         count += 1
# if count > 0:
#     print(count)
#     print(p)
# else:
#     print('NO')



# total = 0
# count = 0
# max = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         total += num
#         count += 1
#         if num < max:
#             max = num
# if count > 0:
#     print(max)
#     print(total)
     
# else:
#     print("NO")


# mx = 0
# s = 0
# count = 0
# for i in range(1, 4):
#     x = int(input())
#     if x < 0:
#         s += x
#         if x < mx:
#             mx = x
#         count += 1

# if count > 0:
#     print(s)
#     print(mx)
# else:
#     print("NO")

# n = int(input())
# count = 0
# max_digit = 0
# while n > 0:
#     digit = n % 10
#     if (digit % 3 == 0) or (digit == 0):
#         if digit > max_digit:
#             max_digit = digit
#         count += 1
#     n = n // 10
# if count == 0:
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# while n > 9:
#     n = n // 10
# print(n)

# n = int(input())
# product = 1
# while n > 0:
#     digit = n % 10
#     product = product * digit
#     n = n // 10
# print(product)

# n = int(input())
# for j in range(n):
#     for k in range(3):
#         print(n, end=' ')
#     print()

# total = 0
# for n in range(1, 12):
#     for k in range(1,12):
#         for m in range(1, 11):
#             if 28 * n + 30 * k + 31 * m == 365:
#                 print(n, k, m)
#                 total += 1


# for n in range(1, 11):
#     for k in range(1, 19):
#         for m in range(1, 101):
#             if 10 * n + 5 * k + 0.5 * m == 100:
#                 if n + k + m == 100:
#                     print(n, k, m)

# for a in range(1, 11):
#     for b in range(1, 11):
#         for c in range(1, 11):
#             for d in range(1, 11):
#                 for e in range(1, 151):
#                     if pow(a, 5) + pow(b, 5) + pow(c, 5) + pow(d, 5) == pow(e, 5):
#                         print(a, b, c, d, e)
#                     else:
#                         print("NO")

# for a in range(1, 151, 0.5):
#     for b in range(1, 151, 0.5):
#         for c in range(1, 151, 0.5):
#             for d in range(1, 151, 0.5):
#                 for e in range(1, 151, 0.5):
#                     if a**5 + b**5 + c**5 + d**5 == e**5:
#                         print(a, b, c, d, e)
           

# n = int(input())
# total = 1
# for i in range(1, n+ 1):
#     for j in range(1, i +1):
#         print(total, end='')
#         total += 1
#     print()



# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(i + 1, end=' ')
#         i  += 1
#     print()

# n = int(input())
# for i in range(n):
#     total = 1
#     for j in range(i + 1):
#         print(total, end=' ')
#         total += 1
#     for k in range(i):
#         print(total - 2, end=" ")
#         total -= 1
#     print()

# num = int(input())
# for i in range(1, num + 1):
#     for j in range(1, i + 1):    
#         print(j, end ='')
#     for k in range(i - 1, 0, -1):
#         print(k, end='')
#     print()

# n = int(input())
# for i in range(1, n + 1):
#     for j in range()

# a, b = int(input()), int(input())
# total = 0
# for i in range(a, b+1):
#     sum = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             sum += j
#             if sum >= total:
#                 largest = i
#                 total = sum              
# print(largest, total)

# n = int(input())

# while n > 9:
#     sum = 0
#     while n != 0:
#         num = n % 10
#         sum += num
#         n = n // 10
#     n = sum
# print(sum)


# n = int(input())
# fact = 1
# sum = 0
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         umnoj = i * j
#         fact *= umnoj
#     sum += fact
# print(sum)

# n = int(input())
# fact = 1
# sum = 1
# for i in range(1, n):
#     num = i + 1
#     fact *= num
#     sum += fact
# print(sum)

# from math import *

# n = int(input())
# sum = 0

# for i in range(1, n + 1):
#     num = factorial(i)
#     sum += num
# print(sum)

# a, b = int(input()), int(input())

# for i in range(a, b + 1):
#     flag = True
#     if i == 1:
#         flag = False
#     for j in range(2, i):
#         if i % j == 0:
#             flag = False
#             if i == j:
#                 flag = True
#     if flag == True:
#         print(i)


# n = int(input())
# s = 0
# while n != 0:
#     if (n % 10) % 2 == 0:
#         s += (n % 10)
#     n //= 10
# if s == 0:
#     print(0)
# else:
#     print(s)

# count = 0
# maximum = -10**12
# for i in range(1, 9):
#     num = int(input())
#     if num % 4 == 0:
#         count += 1
#         if num >= maximum:
#             maximum = num
# if count == 0:
#     print("NO")
# else:
#     print(count)
#     print(maximum)

# n = int(input())
# for i in range(1, n+1):
#     if i == 1 or i == n:
#         print(19 * "*")
#     else:
#         print("*", 15 * " ", "*")

# n = int(input())
# num = n

# while n > 999:
#     num = n % 10
#     n = n // 10

# if n > 99 and n < 1000:
#     print(n % 10)


# n = int(input())
# num = n
# last_dig = n % 10
# count = 0
# count1 = 0
# counnt_chetn = 0
# sum_b5 = 0
# proiz = 1
# sum_obsh = 0
# while n > 0:
#     num = n % 10
#     if num == 3:
#         count += 1
#     if num == last_dig:
#         count1 += 1
#     if num % 2 == 0:
#         counnt_chetn += 1
#     if num > 5:
#         sum_b5 += num
#     if num > 7:
#         proiz *= num
#     if num == 0 or num == 5:
#         sum_obsh += 1
    
#     n = n // 10

# print(count)
# print(count1)
# print(counnt_chetn)
# print(sum_b5)
# print(proiz)
# print(sum_obsh)

# n = 34
# for i in range(1, n):
#     for j in range(1, n):
#         for k in range(1, n):
#             for l in range(1, n):
#                 if i**3 + j**3 == k**3 + l**3:
#                     print(i**3 + j**3)

# s = input()
# for i in range(-len(s)-1, -1, -1):
#     print(s[i])

# s1, s2, s3 = input(), input(), input()
# print(s2[0] + s1[0] + s3[0])

# n = input()
# num = int(n)
# num1 = num
# sum = 0
# while num > 0:
#     num1 = num % 10
#     sum += num1
#     num //= 10
# print(sum)

# s = input()

# if '1' in s or '2' in s or '3' in s or '4' in s or '5' in s or '6' in s or '7' in s or '8' in s or '9' in s or '0' in s:
#     print("Цифра")
# else:
#     print("Цифр нет")

# s = input()
# count1 = 0
# count2 = 0
# for i in s:
#    if i == "*":
#       count1 += 1
#    if i == "+":
#       count2 += 1
# print(f"Символ + встречается {count2} раз")
# print(f"Символ * встречается {count1} раз")

# s = input()
# count = 0

# for i in range(0, len(s)-1):
#     if s[i] == s[i +1]:
#         count += 1
# print(count)

# s = input()
# glasn = "ауоыиэяюёе"
# glasn2 = "АУОЫИЭЯЮЁЕ"
# soglasn = "бвгджзйклмнпрстфхцчшщ"
# soglasn2 = "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ"
# count1 = 0
# count2 = 0
# for i in s:
#     if i in glasn or i in glasn2:
#         count1 += 1
#     if i in soglasn or i in soglasn2:
#         count2 += 1

# print(f"Количество гласных букв равно {count1}")
# print(f"Количество согласных букв равно {count2}")

# n = int(input())
# o = 1
# count = ""
# while n > 0:
#     o = int(o)
#     o = n % 2
#     n = n//2
#     o = str(o)
#     count += o

# for i in range(1, len(count)+1):
#     print(count[-i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# print(s[::7])


# s = input()

# if s[:len(s) + 1] == s[::-1]:
#     print("YES")
# else:
#     print("NO")

# s = input()
# print(s[1:(len(s)//2)])

# s = input()
# print(len(s))
# print(s * 3)
# print(s[0])
# print(s[:3])
# print(s[-3:])
# print(s[::-1])
# print(s[1:-1])

# третий символ этой строки;
# предпоследний символ этой строки;
# первые пять символов этой строки;
# всю строку, кроме последних двух символов;
# все символы с четными индексами;
# все символы с нечетными индексами;
# все символы в обратном порядке;
# все символы строки через один в обратном порядке, начиная с последнего.

# s = input()
# print(s[2])
# print(s[-2])
# print(s[:5])
# print(s[:-2])
# print(s[::2])
# print(s[1::2])
# print(s[::-1])
# print(s[::-2])

# s = input()
# if s == s.title():
#     print("YES")
# else: 
#     print("NO")


# s = input()
# print(s.swapcase())

# s = input()
# s = s.lower()
# if 'хорош' in s:
#   print("YES")
# else:
#   print("NO")

# s = input()
# count = 0
# n = "123456789"
# for i in s:
#   if (i not in n) and (i == i.lower()):
#     count += 1
# print(count)

# s = input()
# s = s.lower()
# a = s.count("а")
# g = s.count("г")
# c = s.count("ц")
# t = s.count("т")
# print("Аденин:", a)
# print("Гуанин:", g)
# print("Цитозин:", c)
# print("Тимин:", t)

# n = int(input())
# count = 0

# for i in range(n):
#   count1 = 0
#   s = input()
#   count1 = s.count("11")
#   if count1 >= 3:
#     count += 1
# print(count)

# s = input()
# count = 0
# n = "0123456789"
# for i in s:
#   if i in n:
#     count += 1
# print(count)

# s = input()
# maxim = 0
# largest = ""
# for i in s:
#   if s.count(i) >= maxim:
#     maxim = s.count(i)
#     largest = i
# print(largest)

# s = input()
# count = s.count("f")
# if count == 1:
#   print(s.find("f"))
# elif count > 1:
#   print(s.find("f"), s.rfind("f"))
# else:
#   print("NO")

# s = input()
# first = s.find("h")
# last = s.rfind('h')
# for i in range(len(s)):
#   if i >= first and i <= last:
#     new = s[i].replace(s[i], "")
# print(s)



# 888888888888888888
#   n = int(input())
# o = 1
# count = ""
# while n > 0:
#     o = int(o)
#     o = n % 2
#     n = n//2
#     o = str(o)
#     count += o

# for i in range(1, len(count)+1):
#     print(count[-i], end='')
# 88888888888888888888888888

# n = int(input())
# s = input()
# alf = 'abcdefghijklmnopqrstuvwxyz'

# for i in s:
#   num = alf.find(i)
#   num_new = num - n
#   if num_new < 0:
#     num_new = num_new + len(alf)
#   print((alf[num_new]), end='')

# На вход программе подается строка текста. Напишите программу, которая выводит индекс второго вхождения буквы «f». Если буква «f» встречается только один раз, выведите число 
# −  1, а если не встречается ни разу, выведите число − 2 

# s = input()
# count = 0
# for i in s:
#   ind = s.find("f")
#   if ind >= 0:
#     count += 1
#     if count == 1:
#       s = s.replace("f", ' ', 1)
#     if count == 2:
#       print(ind)
# if count == 1:
#   print(-1)
# elif count == 0:
#   print(-2)

# s = input()
# num1 = s.find('h')
# num2 = s.rfind('h')
# s2 = s[(num2 - 1):num1:-1]
# print(s.replace(s[(num1 + 1):num2], s2))

# n = int(input())
# numbers = list(range(n+1))
# for i in range(2, n+2):
#   numbers[i-1] == i
# print(numbers)
  
# n = int(input())
# numbers = list(range(1, n+1))
# print(numbers)

# n = int(input())
# alf = 'abcdefghijklmnopqrstuvwxyz'
# spisok = list()
# for i in range(n):
#   spisok = spisok + list(alf[i])
# print(spisok)

# alfa = []
# for i in range(26):
#   alfa.append(chr(ord('a') + i) * (i+1))
# print(alfa)



# numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]
# print(len(numbers))
# print(numbers[-1])
# print(numbers[::-1])
# if 5 in numbers or 17 in numbers:
#   print("YES")
# else:
#   print("NO")
# print(numbers[1:-1])
# # print(numbers[1:(len(numbers)-1)])

# n = int(input())
# list = []
# for i in range(n):
#   s = input()
#   list.append(s)
# print(list)

# n = int(input())
# list = []
# for i in range(n):
#   k = int(input())
#   list.append(k**3)
# print(list)

# n = int(input())
# list = []
# for i in range(1, n + 1):
#   if n % i == 0:
#     list.append(i)
# print(list)

# n = int(input())
# list = []
# list1 = []
# for i in range(n):
#   k = int(input())
#   list.append(k)
# for i in range(1, len(list)):
#   list1.append((list[i] + list[i - 1]))
# print(list1)

# n = int(input())
# list =[]
# for i in range(n):
#     k = int(input())
#     list.append(k)
# del list[1::2]

# print(list)

# n = int(input())
# list = []
# for i in range(n):
#   s = input()
#   list.append(s)

# k = int(input())
# k = k -1
# for i in range(n):
#   s1 = list[i]
#   if len(s1) <= k:
#     continue
#   s1 = s1[k]
#   print(s1, end='')

# n = int(input())
# list = []
# for i in range(n):
#   s = input()
#   list.extend(s)
# print(list)

# n = int(input())
# list = []
# for i in range(n):
#   x = int(input())
#   list.append(x)
# print(*list, sep='\n')
# print()
# for i in list:
#   f = i**2 + 2*i + 1
#   print(f)

# n = int(input())
# list = []
# for i in range(n):
#   x = int(input())
#   list.append(x)
# maxim = max(list)
# minim = min(list)

# del list[list.index(maxim)]

# print(*list, sep='\n')

# n = int(input())
# list = []
# for i in range(n):
#   x = input()
#   list.append(x)

# list2 = []

# for i in range(len(list)):
#   if list[i] not in list2:
#     list2.append(list[i])

# n = int(input())
# list = []
# list2 = []
# for i in range(n):
#   x = input()
#   list.append(x)

# z = input()
# for i in list:
#   if z.casefold() in i.casefold():
#     list2.append(i)
# print(*list2, sep='\n')

# n = int(input())
# list = []
# for i in range(n):
#   x = input()
#   list.append(x)
# k = int(input())
# list2 = []
# for i in range(k):
#   z = input()
#   list2.append(z)

# for sens in list:
#   count = 0
#   for search in list2:
#     if search.lower() in sens.lower():
#       count += 1
#       if count >= k:
#         print(sens)

# n = int(input())
# list = []
# for i in range(n):
#   x = int(input())
#   list.append(x)
# for neg in list:
#   if neg < 0:
#     print(neg)
# for zero in list:
#   if zero == 0:
#     print(zero)
# for posit in list:
#   if posit > 0:
#     print(posit)

# s = input()
# s1 = ''
# for i in s:
#   if i != i.lower():
#     s1 += i
# s1 = list(s1)
# print('.'.join(s1) + '.')

# s = input().split(".")
# count = 0
# for i in s:
#   i = int(i)
#   if i <= 255:
#     count += 1
# if count == 4:
#   print('ДА')
# else:
#   print("НЕТ")


# s = input()
# simv = input()
# list = []
# for i in range(len(s)):
#   list.append(s[i])
# print(simv.join(list))

# s = input().split()
# count = 0
# for i in range(len(s)):
#   for k in range(i+1,len(s)):
#     if s[i] == s[k]:
#       count += 1
# print(count)
    

# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()

# numbers = [8, 9, 10, 11]
# numbers.insert(1, 17)
# numbers.remove(9)
# numbers.append(4)
# numbers.append(5)
# numbers.append(6)
# del numbers[0]
# numbers = numbers*2
# numbers.insert(3, 25)
# print(numbers)

# s = input().split()

# for i in range(len(s)):
#   s[i] = int(s[i])
# maxim = max(s)
# minim = min(s)
# pos_maxim = s.index(maxim)
# pos_minim = s.index(minim)
# s[pos_maxim] = minim
# s[pos_minim] = maxim
# print(*s)

# s = input()
# s = s.lower()
# s = s.split()
# cnt = s.count('the') + s.count('an') + s.count('a')

# print("Общее количество артиклей:", cnt)
# s = input()
# num = int(s[1:])
# for i in range(num):
#   str = input()
#   if "#" in str:
#     index = str.find("#")
#     print(str[:index].rstrip())
#   else:
#     print(str)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords =[i[1:] for i in keywords]
               
# print(new_keywords)

# keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'try', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'while', 'yield']

# new_keywords = [i for i in keywords if len(i) >= 5]

# print(new_keywords)

# palindromes = []

# for i in range(100, 1000):
#   i = str(i)
#   for j in range(len(i)//2):
#     if i[j] == i[len(i) - 1 - j]:
#       palindromes.append(i)
# for k in range(len(palindromes)):
#   palindromes[k] = int(palindromes[k])

# palindromes = [i for i in range(100, 1000) for j in range(len(str(i))//2) if str(i)[j] == str(i)[len(str(i)) - 1 - j] ]
      

# print(palindromes)

# [print(i) for i in input().split()]

# s = input()
# dig = "1234567890"
# for i in s:
#   if i in dig:
#     print(i, end='')



# [print(i, end='') for i in input() if i in '1234567890']

# [print(int(i)**2, end=" ") for i in input().split() if int(i) % 2 == 0 and (int(i) ** 2) % 10 != 4]

# a = [17, 24, 91, 96, 67, -27, 79, -71, -71, 58, 48, 88, 88, -16, -78, 96, -76, 56, 92, 1, 32, -17, 36, 88, -61, -97, -37, -84, 50, 47, 94, -6, 52, -76, 93, 14, -32, 98, -65, -16, -9, -68, -20, -40, -71, 93, -91, 44, 25, 79, 97, 0, -94, 7, -47, -96, -55, -58, -78, -78, -79, 75, 44, -56, -41, 38, 16, 70, 17, -17, -24, -83, -74, -73, 11, -26, 63, -75, -19, -13, -51, -74, 21, -8, 21, -68, -66, -84, -95, 78, 69, -29, 39, 38, -55, 7, -11, -26, -62, -84]

# n = len(a)

# for i in range(n - 1):
#     flag = False
#     for j in range(n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#             flag = True
#     if flag == False:
#         break

# print(a)

# a = [78, -32, 5, 39, 58, -5, -63, 57, 72, 9, 53, -1, 63, -97, -21, -94, -47, 57, -8, 60, -23, -72, -22, -79, 90, 96, -41, -71, -48, 84, 89, -96, 41, -16, 94, -60, -64, -39, 60, -14, -62, -19, -3, 32, 98, 14, 43, 3, -56, 71, -71, -67, 80, 27, 92, 92, -64, 0, -77, 2, -26, 41, 3, -31, 48, 39, 20, -30, 35, 32, -58, 2, 63, 64, 66, 62, 82, -62, 9, -52, 35, -61, 87, 78, 93, -42, 87, -72, -10, -36, 61, -16, 59, 59, 22, -24, -67, 76, -94, 59]

# n = len(a)

# for i in range(n-1):
#   for j in range(n-i-1):
#     ind = a.index(max(a[0: n-i]))
#     maxim = a[ind]
#     a[ind] = a[n-i-1]
#     a[n-i-1] = maxim
    
# # реализация алгоритма сортировки выбором

# print(a)

# n = int(input())
# numbers = list(range(2, n+1, 2))
# print(numbers)

# L = input().split()
# M = input().split()
# N = []
# for i in range(len(L)):
#   N.append(int(L[i]) + int(M[i]))
# print(*N)

# s = input().split()
# sum = 0

# for i in range(len(s)):
#   sum += int(s[i]) 

# print(f"{'+'.join(s)}={sum}") 

# s = input().split('-')
# numbers = '0123456789'
# flag = False

# for i in s:
#  if i.isdigit():
#   flag = True
#  else:
#   flag = False
#   break


# if flag == True:
#   if len(s) == 4:
#    if len(s[0]) == 1 and len(s[1])== 3 and len(s[2])== 3 and len(s[3])== 4 and s[0] == '7':
#     flag = True
#    else:
#      flag = False

#   if len(s) == 3:
#    if len(s[0]) == 3 and len(s[1])== 3 and len(s[2])== 4:
#     flag = True
#    else:
#     flag = False
    
# if len(s) < 3:
#  flag = False
      
# if flag == True:
#   print("YES")
# else:
#   print("NO")

# flag = False
# numbers = '0123456789'
# for i in s:
#   for j in range(len(i)):
#     if i[j] in numbers:
#       flag = True
# if flag == True:
#   print("YES")
# else:
#   print("NO")


# s = input().split()
# l = 0
# for i in s:
#   if len(i) > l:
#     l = len(i)
# print(l)

# s = input().split()

# new = [i[0] for i in s]

# list = [i[1:] for i in s]

# last = [list[i] + new[i] + "ки" for i in range(len(list))]

# print(*last)

# # объявление функции

# def draw_triangle(fill, base):
#     for i in range(1, base + 1):
#         if i <= base // 2:
#             print(i * fill)
#         elif i > base// 2:
#             print((base - i + 1) * fill)
#         else:
#             print((base // 2 + 1) * fill)
# # считываем данные
# fill = input()
# base = int(input())

# вызываем функцию
# draw_triangle(fill, base)

# # объявление функции
# def print_fio(name, surname, patronymic):
#     print(surname[0].upper() + name[0].upper() + patronymic[0].upper())

# # считываем данные
# name, surname, patronymic = input(), input(), input()

# # вызываем функцию
# print_fio(name, surname, patronymic)


# def convert_to_celsius(temp):
#     result = (5 / 9) * (temp - 32)
#     return result

# from unittest import result


# def sum_digits(n):
#   result = 0
#   while n > 0:
#     result += n % 10
#     n //= 10
#   return result



# print(sum_digits(int(input())))

# def compute_average(numbers):
#   everage = 0
#   everage = sum(int(numbers))/len(numbers)
#   return(everage)

# print(compute_average(12345))

# # объявление функции
# def convert_to_miles(km):
#     mil = km * 0.6214
#     return mil

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(convert_to_miles(num))

# # объявление функции
# def get_days(month):
#     if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#         return 31
#     elif  month == 4 or month == 6 or month == 9 or month == 11:
#         return 30
#     else:
#         return 28

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))

# def get_factors(num):
#   new = []
#   for i in range(1, num + 1):
#    if num % i == 0:
#      new.append(i)
#   return(new) 

# n = int(input())
# print(get_factors(n))

# # объявление функции
# def get_factors(num):
#   new = []
#   for i in range(1, num + 1):
#    if num % i == 0:
#      new.append(i)
#   return(len(new))

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_factors(n))

# def find_all(target, symbol):
#   list = []
#   for i in range(0, len(target)):
#     if target[i] == symbol:
#       list.append(i)
#   return(list)

# s = input()
# char = input()

# print(find_all(s, char))

# # объявление функции
# def merge(list1, list2):
#   final_list = list1 + list2
#   final_list.sort()
#   return(final_list)

# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))

# def quick_merge(spisok1, spisok2):
#   final = []
#   p1 = 0
#   p2 = 0

#   while p1 < len(spisok1) and p2 < len(spisok2):
#     if spisok1[p1] < spisok2[p2]:
#       final.append(spisok1[p1])
#       p1 += 1
#     else:
#       final.append(spisok2[p2])
#       p2 += 1
  

#   if p1 < len(spisok1):
#     final += spisok1[p1:]
#   else:
#     final += spisok2[p2:]
#   return(final)

# n = int(input())
# result = []
# for i in range(0, n):
#   list = [int(c) for c in input().split()]
#   result = quick_merge(list, result)

# print(*result)

# объявление функции
# def is_valid_triangle(side1, side2, side3):
#   if side1 < side2 + side3 and side2 < side1 + side3 and side3 < side2 + side1:
#     return True
#   else:
#     return False
    

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))

# def is_prime(num):
#   flag = True
#   for i in range(2, num):
#     if num % i == 0:
#       flag = False
#       break
        
#   if num == 1:
#     flag = False
#   elif num == 2:
#     flag = True
#   return flag 


# def get_next_prime(n):

#   for i in range(n+1, n*3):
#     if is_prime(i) == True:
#       return i
      

# # считываем данные
# new = int(input())

# # вызываем функцию
# print(get_next_prime(new))



# def is_password_good(s):
#   alf_up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#   alf_low = "abcdefghijklmnopqrstuvwxyz"
#   num = '0123456789'
#   count1 = 0
#   count2 = 0
#   count3 = 0

#   for i in s:
#     if i in alf_up:
#       count1 += 1
#     elif i in alf_low:
#      count2 += 1
#     elif i in num:
#       count3 += 1

#   if count1 == 0 or count2 == 0 or count3 == 0 or len(s) < 8:
#     return False
#   else:
#     return True

# str = input()
# print(is_password_good(str))

# def is_password_good(s):
#   count1 = 0
#   for i in s:
#     if i.isdigit():
#       count1 += 1
#   return count1
#     # elif i in alf_low:
#     #  count2 += 1
#     # elif i in num:
#     #   count3 += 1

# str = input()

# print(is_password_good(str))

# # объявление функции
# def is_one_away(word1, word2):
#   count = 0
#   flag = False 
#   if len(word1) != len(word2):
#     flag = False
#   else:
#     for i in range(len(word1)):
#       if word1[i] != word2[i]:
#         count += 1
#   if count == 1:
#     flag = True
  
#   return flag
# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))


# def is_palindrome(text):
  
#   text = text.lower()
#   list = []
#   for i in range(len(text)):
#     if text[i].isalpha():
#       list.append(text[i])

#   flag = False
#   for i in range(0, (len(list) // 2) + 1):
#     if list[i] == list[len(list) - 1 - i]:
#       flag = True
#     else:
#       flag = False
#       break

#   return flag

# stroka = input()
# print(is_palindrome(stroka))


# def is_palindrome(text):
  
#   text = text.lower()
#   list = [text[i] for i in range(len(text)) if text[i].isalpha()]
   
#   flag = False
#   for i in range(0, (len(list) // 2) + 1):
#     if list[i] == list[len(list) - 1 - i]:
#       flag = True
#     else:
#       flag = False
#       break

#   return flag

# stroka = input()
# print(is_palindrome(stroka))

# def is_prime(num):
#   flag = True
#   for i in range(2, num):
#     if num % i == 0:
#       flag = False
#       break
        
#   if num == 1:
#     flag = False
#   elif num == 2:
#     flag = True
#   return flag 

# def is_palindrome(digit):
  
#   for i in range(0, (len(digit) // 2) + 1):
#     if digit[i] == digit[len(digit) - 1 - i]:
#       flag = True
#     else:
#       flag = False
#       break

#   return flag

# def is_chetnoe(num):
#   if num % 2 == 0:
#     return True

# def is_valid_password(password):
#   count = 0
#   password_list = password.split(":")
#   if is_palindrome(password_list[0]) == True:
#     count += 1
#   if is_prime(int(password_list[1])) == True:
#     count += 1
#   if is_chetnoe(int(password_list[2])) == True:
#     count += 1
#   if len(password_list) > 3:
#     return False

#   if count == 3:
#     return True
#   else:
#     return False

# psw = input()
# print(is_valid_password(psw))

# def is_correct_bracket(text):
#   flag = False
#   count = 0
#   open = "("
#   close = ")"
  
#   for i in text:
#     if i in open:
#      count += 1
#     elif i in close:
#       count -= 1
#     if count == - 1:
#       break
#   return count == 0

# s = input()   
# print(is_correct_bracket(s))

# def convert_to_python_case(text):
#   text_new = list(text)
#   list_new = []
#   for i in range(0, len(text_new)):
#     if i == 0:
#       list_new.append(text_new[i])
#     if i != 0:
#       if text_new[i].isupper():
#         list_new.append("_")
#         list_new.append(text_new[i])
#     if text_new[i].islower() or text_new[i].isdigit():
#       list_new.append(text_new[i])
#   return "".join(list_new).lower()

# s = input()
# print(convert_to_python_case(s))

# # объявление функции
# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x, y

# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)


# # объявление функции
# def draw_triangle():
#     for i in range(1, 9):
#         print((8-i) * " " + (i + i - 1) * "*")

# # основная программа
# draw_triangle()  # вызов функции

# # объявление функции
# def get_shipping_cost(quantity):
#     sum = 0
#     for i in range(1, quantity + 1):
#         if i == 1:
#             sum = 1000
#         else:
#             sum += 120
#     return sum

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_shipping_cost(n))

# from math import *

# def compute_binom(n, k):
#     b = (factorial(n)) // ((factorial(k)) * (factorial(n-k)))
#     return b

# # считываем данные
# n = int(input())
# k = int(input())

# # вызываем функцию
# print(compute_binom(n, k))




# # объявление функции
# def number_to_words(num):
#     list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
#     list_11 = ['одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать']
#     list_21 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']
#     if num < 11:    
#         return list_1[num-1]
#     elif num > 10 and num < 20:
#         return list_11[num-11]
#     elif num % 10 == 0:
#         return list_21[num // 10 - 2]
#     else:
#         last = num % 10 
#         first = num // 10
#         return list_21[first-2] + " " + list_1[last-1]

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_to_words(n))



# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
#     if language == "ru":
#         return lng_ru[number-1]
#     else:
#         return lng_en[number-1]

# # считываем данные
# lan = input()
# num = int(input())


# # вызываем функцию
# print(get_month(lan, num))



# # объявление функции
# def is_magic(date):
#     list = date.split(".")
#     return int(list[0]) * int(list[1]) == int(list[2]) % 100
    
# # считываем данные
# date = input()

# # вызываем функцию
# print(is_magic(date))


# # объявление функции
# def is_pangram(text):
#     text_new = text.upper()
#     text_final = set(text_new)
    
#     return len(text_final) == 27
    

# # считываем данные
# text = input()

# # вызываем функцию
# print(is_pangram(text))

# from random import *
# # Return random integer in range [a, b], including both end points.
# def randint(self, a, b):
#     return self.randrange(a, b + 1)
# list = []
# print(randint(' ', 0, 100))



# from random import *

# n = randint(1, 100)
# print("Угадайте число")
# m = 0

# while m != n:
#   m = int(input())
#   if m > n:
#     print("Слишком много, попробуйте еще раз")
#   elif m < n:
#     print("Слишком мало, попробуйте еще раз")
#   else:
#     print("Вы угадали, поздравляем!")


# from random import *
# n = int(input())
# x = randint(1, n)
# print(x)
# m = 0
# left = 1
# right = n
# count = 1
# while m != x:
#   print("Угадайте число")
#   m = (left + right)//2
#   print(m)
#   if m > x:
#     print("Слишком много, попробуйте еще раз")
#     right = m - 1

#   elif m < x:
#     print("Слишком мало, попробуйте еще раз")
#     left = m + 1
#   else:
#     print("Вы угадали, поздравляем!")
#   count += 1
# print("Количество попыток: ", count)


# from random import *
# n = int(input())
# x = randint(1, n)
# m = 0
# left = 1
# right = n
# count = 0
# while m != x:
#    m = (left + right)//2
 
#    if m > x:
   
#     right = m - 1

#    elif m < x:
    
#     left = m + 1
   
#    count += 1
# print(count)

# from math import *
# n = int(input())
# count = log2(n)

# print(ceil(count))



# from random import *
# x = randint(1, 100)
# print(x)

# def is_valid(n):
#   if n.isdigit() and 1 <= int(n) <= 100:
#     return True
#   else:
#     return False

# while True:
#   print("Введите число от 1 до 100")
#   num = input()
#   number = is_valid(num)
#   if number == False:
#     print("А может быть все-таки введем целое число от 1 до 100?")
#     continue
#   else:
#     num = int(num)
    
#   if num < x:
#     print('Ваше число меньше загаданного, попробуйте еще разок')
#     continue
#   elif num > x:
#     print('Ваше число больше загаданного, попробуйте еще разок')
#     continue
#   else:
#     print('Вы угадали, поздравляем!')
#     break

# from math import *

# a = int(input())
# b = int(input())
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(sqrt(a ** 10 + b ** 10))

# a = float(input())
# b = float(input())
# IMT = a / (b * b) 
# if 18.5 <= IMT <= 25:
#   print("Оптимальная масса")
# elif IMT < 18.5:
#   print('Недостаточная масса')
# else:
#   print("Избыточная масса")

# s = input()
# n = len(s)
# x = int(0.60 * n)
# y = int(((0.60 * n) % 10)*100)
# print(x, y)



# Вариант 1 - max and min
# list_of_ratings = [2, 2, 4, 3, 2, 3, 3, 5, 5, 5, 5, 5]
# max_number = max(list_of_ratings)
# min_number = min(list_of_ratings)
# print(f'Минимум - {min_number}, Максимум - {max_number}')

# for i in range(len(list_of_ratings)):
# if list_of_ratings[i] == min_number:
# list_of_ratings[i] = max_number

# print(list_of_ratings)

# def posled(n):
#   if n == 0:
#     return " "
#   k = int(input())

#   return posled(n-1) + f' {k}'

# print(posled(4))

# def arrange(a, b):
#   if a == b:
#     return f"{a}"
#   if a < b:
#     return f'{a}, {arrange((a + 1), b)}'
#   if a > b:
#     return f'{a}, {arrange((a - 1), b)}'

# print(arrange(10, 5))



# def fib_2(n):
#   if n <= 1:
#     return n
#   return fib_2(n - 1) + fib_2(n - 2)

# print(fib_2(18))

# def fact(n):
#   if n == 1:
#     return 1
#   return n * fact(n-1)

# print(fact(5))


# def f(a, b):
#   if b == 0:
#     return 1
#   return f(a, b - 1) * a

# print(f(3, 5))

# def sum(a, b):
#     if b == 0:
#         return a
#     elif a == 0:
#         return b
#     else:
#         return sum(a + 1, b - 1)
    
# print(sum(2,2))

# list = [1, 2, 3, 2, 2, 2, 3]
# count = 0
# for i in range(0, len(list)):
#   for j in range(i, len(list)-1):
#     if list[i] == list[j+1]:
#       count += 1

# print(count)

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(i)

# a1 = 2
# d = 3
# n = 4

# an = a1 + (n-1) * d

# for i in range(1, n + 1):
#   elem = a1 + (i-1) * d
#   print(elem)

# spisok = [1, 2, 3, 4, 5, 8, 15, 23, 38]

# list = [(i, i ** 2) for i in spisok if i % 2 == 0]

# print(list)

# data = '15 156 96 3 5 8 52 5'


# data = list(map(lambda x: int(x), data))

# n = int(input())
# perv = 0
# vtor = 0
# tret = 0
# chetv = 0

# for i in range(n):
#   x, y = int(input()), int(input())
#   if x > 0 and y > 0:
#     perv += 1
#   elif x > 0 and y < 0:
#     chetv += 1
#   elif x < 0 and y < 0:
#     tret += 1
#   elif x < 0 and y > 0:
#     tret += 1
# print(f' Первая четверть: {perv}')
# print(f' Вторая четверть: {vtor}')
# print(f' Третья четверть: {tret}')
# print(f' Четвертая четверть: {chetv}')
  

# s = input()
# list = s.split()
# count = 0
# for i in range(1, len(list)):
#   if int(list[i]) > int(list[i - 1]):
#     count += 1
# print(count)    


# s = input()
# list = s.split()

# for i in range(1, len(list), 2):
#   n = list[i]
#   list[i] = list[i - 1]
#   list[i-1] = n
  
# print(*list)   

# s = input()
# list = s.split()
# list_new = []
# for i in range(0, len(list)):
#   list_new.append(list[-1 + i])
  
# print(*list_new)   


# s = input()
# list = s.split()
# list_new = set(list)
  
# print(len(list_new))  


# n = int(input())
# flag = False
# list = []

# for _ in range(n):
#   n1 = int(input())
#   list.append(n1)

# n2 = int(input())

# for i in range(0, len(list)):
#   for j in range(0, len(list)):
#     if i != j and list[i] * list[j] == n2:
#       flag = True
#       break
  
# if flag == True:
#   print("ДА")
# else:
#   print("НЕТ")


# def print_operation_table(operation, num_rows, num_columns):
#   if num_rows < 2:
#     return print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    

#   for i in range(1, num_rows + 1):
#     for j in range(1, num_columns + 1
#                    ):
#       print(operation(j, i), end=" ")
#     print()
  
# print_operation_table(lambda x, y: x + y, 4, 4)


# def print_operation_table(operation, num_rows, num_columns):
#     a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
#     for i in a:
#         print(*[x for x in i])

# print_operation_table(lambda x, y: x - y, 5, 5)

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     result = []
#     if num_rows < 2 or num_columns < 2:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         print(' '.join([str(i) for i in range(1, num_columns + 1)]))
#         for i in range(2, num_rows + 1):
#             result.append(i)
#             for j in range(2, num_columns + 1):
#                 if j != num_columns:
#                     result.append(f'{operation(i, j)} ')
#                 else:
#                     result.append(operation(i, j))
#             result.append('\n')
#         print(''.join([str(i) for i in result[:len(result) - 1]]))
# print_operation_table(lambda x, y: x * y, 3, 3)

# stroka = 'пара-ра-рам'
# alf = "уеыаоэяиюё"
# list = stroka.split()

# ritm = []
# for i in list:
#   count = 0
#   for j in i:
#     if j in alf:
#       count += 1
#   ritm.append(count)
# print(ritm)
# for e in range(0, len(ritm)-1):
#   flag = False
#   if ritm[e] == ritm[e+1]:
#     flag = True
#   else:
#     break
# if len(list) <= 1:
#   print("Количество фраз должно быть больше одной!")
# elif flag == True:
#   print("Парам пам-пам")  
# else:
#   print("Пам парам")


# def filt(st, sr):

#   if st == "камень" and sr == "ножницы":
#     return(st)
#   elif st == "ножницы" and sr == "камень":
#     return(sr)
#   elif st == "ножницы" and sr == "бумага":
#     return(st) 
#   elif st == "бумага" and sr == "ножницы":
#     return(sr)
#   elif st == "бумага" and sr == "камень":
#     return(st) 
#   elif st == "камень" and sr == "бумага":
#     return(sr) 
  
# Тимур = input()
# Руслан = input()
# print(filt(Тимур, Руслан))

# st = input()
# sr = input()

# if st == "камень" and sr == "ножницы":
#   print("Тимур")
# elif st == "ножницы" and sr == "камень":
#   print("Руслан")
# elif st == "ножницы" and sr == "бумага":
#   print("Тимур") 
# elif st == "бумага" and sr == "ножницы":
#   print("Руслан")
# elif st == "бумага" and sr == "камень":
#   print("Тимур") 
# elif st == "камень" and sr == "бумага":
#   print("Руслан")
# else:
#   print("ничья")








