# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
import os
os.system('cls||clear')
a = int(input('Введите трехзначное число \nа= '))
if len(str(a)) == 3:
    result = 0
    while (a != 0) :
        result = result + a % 10
        a //= 10
    print ('Сумма чисел в составе числа a = ', result)
else :
    print ('Введено не корректное число!!')