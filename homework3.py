# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
'''
import random                                           # импортирруем метод
list1 = []                                              # создаем пустой список
a = 0                                                   # задаем переменную для счета
for i in range(0,10):                                   # задаем цикл для заполнения списка
    list1.append(random.randint(0, 10))                 # добавляем в список рандомные числа от 0 до 10
print(list1)                                            # для удобства печатаем список

for i in range(0,10,2):                                 # задаем цикл для подсчета нечетных позиций от 0 до 10 с шагом 2
    a = a + list1[i]                                    # делаем подсчет
print ("Сумма нечетных элементов списка - ",a)          # печатаем на экран
'''

# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
'''
import random                                           # импортирруем метод
list1 = []                                              # создаем пустой список
list2 = []                                              # зоздаем второй пустой список для запуска подсчетов в цикле 2
for i in range(0,10):                                   # задаем цикл для заполнения списка
    list1.append(random.randint(1, 10))                 # добавляем в список рандомные числа от 1 до 10 !!! от единицы чтобы не вызодила ошибка произведения на 0
print(list1)                                            # для удобства печатаем список

for i in range(0,int(len(list1)/2)) :                   # задаем новый цикл 2 !!! пришлось преобразовать результат len(list1)/2 в INT без этого никак
    if i==0:                                            # если i = 0 то это особое условие и прописываем ручками следующую строку
        list2.append(list1[0]*list1[-1])                # а именно первое слагаемое  list от 0 второе от минус 1
    else:                                               # иначе
        list2.append(list1[-i-1]*list1[i])              # делаем подсчет в первом множителе от i отнимаем 1 для приведения к правильной симметрии  так как в нашем случае значения начинаются с 0
print (list2)                                           # печатаем на экран

'''

# Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
import random                                           # импортирруем метод
list1 = []                                              # создаем пустой список
list2 = []                                              # зоздаем второй пустой список для запуска подсчетов в цикле 2

for i in range(0,10):                                   # задаем цикл для заполнения списка
    list1.append(round(random.random()*10,2))           # добавляем в список рандомные числа с округлением 2 знака после запятой
print("Сгенерированный список -",list1)                                            # для удобства печатаем список

for i in range(0,10):                                   # задаем второй цикл для вычисления дробных частей
    list2.append(round(list1[i]%1,2))                   # создаем второй список с остатками дробных частей с округлением до 2го знака
print("Отбросили целую часть - ",list2)                 # выводим результат
max_n = max(list2)                                      # можно было отсортировать пузырьком но лень
min_n = min(list2)                                      # лень пузырить и не хочется писать большой код  долго комментить)
rezult = max_n - min_n                                  # вычисление разницы

print("Разница между мак и мин элементом дробной части равна ",rezult)  # печать результата 









# Задача 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное. Нельзя использовать готовые функции.