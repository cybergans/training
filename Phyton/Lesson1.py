# 1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.
# a = 7
# b = 2
# print("Первая переменная a=", a, ",", "Вторая переменная b=", b)
# print("Операции с переменными:")
# print("a + b =", a + b)
# print("a - b =", a - b)
# print("a * b =", a * b)
# print("a / b =", a / b)
# print("a // b =", a // b)
# print("a % b =", a % b)
# print("a ** b =", a ** b)
#
# name1 = input("Введите ваше имя: ")
# name2 = input("Введите вашу фамилию: ")
# year_birth = int(input("Введите ваш год рождения: "))
# year = int(input("Какой сегодня год? "))
# age = year - year_birth
# print("Введеные значения - %5s %5s %5d %5d" % (name1, name2, year_birth, year))
# print(f"Здравствуйте, {name1} {name2}!")
# print(f"Сейчас Вам {age} лет")

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
# user_time = int(input("Введите время в секундах: "))
# hours = user_time // 3600
# minutes = (user_time % 3600) // 60
# seconds = user_time % 60
# print(f"Время в формате чч:мм:сс {hours} : {minutes} : {seconds}")

# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.
# n = input("Введите число: ")
# nn = int(n * 2)
# nnn = int(n * 3)
# n = int(n)
# #print(n, nn, nnn)
# print(n + nn + nnn)

# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и арифметические операции.

# number = abs(int(input("Введите целое положительное число: ")))  # исключаем отрицательные
# max_digit = number % 10  # предположение, что первая цифра (справа) максимальная
# while number > 0:  # условие, что оставшееся число больше 0
#     number = number // 10  # отбрасываем следующую цифру
#     if number % 10 > max_digit:  # проверка, что следующая цифра больше предыдущей
#         max_digit = number % 10   # если условие выполняется, меняем макс цифру
#     if number > 9:
#         continue
#     else:
#         print("Максимальное цифра в числе ", max_digit)
#         break

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

# proceeds = p = int(input('Введите значение выручки: '))  # выручка
# costs = c = int(input('Введите значение издержек: '))  # издержки
# fin_result = fr = p - c  # прибыль
# if fin_result > 0:
#     print('Фирма работает в прибыль')
#     profitability = r = (fr / p) * 100  # рентабельность
#     print(f'Рентабельность выручки составляет {r}')
#     staff = s = int(input('Укажите число сотрудников: '))  # число сотрудников
#     print(f'Прибыль на одного сотрудника составляет {fr / s}')
# else:
#     print('Фирма работает в убыток')

# 6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# a = int(input('Введите число а: '))
# b = int(input('Введите число b: '))
# if a <= 0 or b <= 0:
#     print('Введите положительные числа')
# else:
#     c = 1
#     while a < b:
#         c += 1
#         a = a + a * 0.1
#     print(f'На {c}-й день спортсмен достиг результата - пробежал не менее {b} км.')