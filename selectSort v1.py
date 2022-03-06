from random import *

def selectionSort(mylist):
    for i in range(len(mylist)):
        for j in range(i, len(mylist)):
            if mylist[i] > mylist[j]:
                mylist[i], mylist[j] = mylist[j], mylist[i]
    return mylist


l = [randint(1, 100) for _ in range(20)] # список рандомных чисел

print("Исходный список:", *l)

l = selectionSort(l)
        
print("Отсортированный список:", *l)

