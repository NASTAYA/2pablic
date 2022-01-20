# Напишите программу, которой на вход подается последовательность чисел через пробел,
# а также запрашивается у пользователя любое число.
# В качестве задания повышенного уровня сложности можете выполнить проверку соответствия
# указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
#   Преобразование введённой последовательности в список
#   Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
#   Устанавливается номер позиции элемента, который меньше введенного пользователем числа,
#    а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска,
#    который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.

import random

string = input('Введите произвольную последовательность разных целых чисел через пробел : ')
list_of_strings = string.split()  # список строковых представлений чисел
list_of_numbers = list(set((map(int, list_of_strings))))  # список уникальных чисел

nam = int(input('Ведите число в пределах последовательности не равное минимальному и максимальному: '))

while nam <= min(list_of_numbers) or nam >= max(list_of_numbers):
    if nam <= min(list_of_numbers):
        print('Веденное число не соответствует условию ввода данных, оно равно или менее минимального')
        nam = int(input('Ведите другое число в пределах последовательности не равное минимальному и максимальному: '))
    elif nam >= max(list_of_numbers):
        print('Веденное число не соответствует условию ввода данных, оно равно или более максимального')
        nam = int(input('Ведите другое число в пределах последовательности не равное минимальному и максимальному: '))


def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)


qsort_random(list_of_numbers, 0, len(list_of_numbers)-1)

element = nam
array = [i for i in list_of_numbers]


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] < element <= array[middle + 1]:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element <= array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


print(f'Последовательность уникальных чисел {list_of_numbers}')

print(f'Позиция элемента, который меньше числа {nam}, а '
      f'следующий за ним больше или равен  числу {nam} - '
      f'{binary_search(array, element, 0, len(list_of_numbers))}')








