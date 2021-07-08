# импортируется библиотека для рандомных чисел
import random

# создается лист с набором 30-ти рандомных чисел от -100 до 100
random_list = [random.randrange(-100,100) for i in range(30)]

# выводится список
print("\nRandom list of numbers from -100 to 100 is: ", random_list)

# поиск максимального элемента в созданном списке
max_element = max(random_list)

# определение индекса максимального элемента в списке
position = random_list.index(max_element)

# вывод индекса элемента (т.к. счёт начинается  с 0, то к переменной индекса добавляем 1, чтобы счёт был человеческим (начинался с 1))
print("\nA maximum number from the list is: ", max_element, "\nin position: ", position + 1)

# создаём пустой новый лист
new_list=[]

# обращаемся к элементам старого списка и говорим, если элемент является нечётным, то мы добавляем элемент этот в конец нового списка
for element in random_list:
    if (element % 2) == 1:
        new_list.append(element)
    
# если в список не заносится никакое число (длина не меняется), то выскакивает надпись, что нет никаких нечётных чисел
if len(new_list) == 0:
  print("\nthere isn't any of odd numbers")

# если длина меняется, то те находящиеся числа сортируются по убыванию и выводится новый список
else:
  new_list.sort(reverse=True)
  print("\nThe new list is: ", new_list)