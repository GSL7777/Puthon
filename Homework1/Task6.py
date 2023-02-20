# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
#  *Пример:*
# 385916 -> yes
# 123456 -> no

# print('Введите число:')
# n = (input())
# m = int(n)
# if  len(n) % 2 != 0 or m < 0:
#     print('Введено не правильное значение. Введите другое число.')
# else:
#     i = 0
#     FirstSum = 0
#     SecondSum = 0
#     while i < int(len(n)/2):
#         x = m % 10
#         FirstSum = FirstSum + x
#         m = m // 10
#         i = i + 1
#     while m > 0:
#         x = m % 10
#         SecondSum = SecondSum + x
#         m = m // 10
#     if FirstSum == SecondSum:
#        print('Ура, вы выиграли!!!')
#     else:
#         print('К сожалению вам не повезло')




print('Введите шестизначное число:')
n = (input())
m = int(n)
if  len(n) != 6 or m < 0:
    print('Введено не правильное значение. Введите другое число.')
else:
    i = 0
    FirstSum = 0
    SecondSum = 0
    while i < 3:
        x = m % 10
        FirstSum = FirstSum + x
        m = m // 10
        i = i + 1
    while m > 0:
        x = m % 10
        SecondSum = SecondSum + x
        m = m // 10
    if FirstSum == SecondSum:
       print('Ура, вы выиграли!!!')
    else:
        print('К сожалению вам не повезло')