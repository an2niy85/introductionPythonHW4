# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого списка: '))
m = int(input('Введите количество элементов второго списка: '))
set1 = set()
set2 = set()

for i in range(n):
    num = int(input('Введите элемент первого списка: '))
    set1.add(num)

for i in range(n):
    num = int(input('Введите элемент воторого списка: '))
    set2.add(num)

common_element = set1.intersection(set2)
sorted_element = sorted(common_element)

print('Общие элементы: ')
for num in sorted_element:
    print(num)
