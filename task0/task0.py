import random

random_list = [random.randrange(-100,100) for i in range(30)]

print("\nRandom list of numbers from -100 to 100 is: ", random_list)

max_element = max(random_list)

position = random_list.index(max_element)

print("\nA maximum number from the list is: ", max_element, "\nin position: ", position + 1)

new_list=[]

for element in random_list:
    if (element % 2) == 1:
        new_list.append(element)
    

if len(new_list) == 0:
  print("\nthere isn't any of odd numbers")

else:
  new_list.sort(reverse=True)
  print("\nThe new list is: ", new_list)