from random import *


def binary_search(mylist=[], n=None):
    low = 0
    high = len(mylist) - 1
    while low <= high:
        mid = int((low + high) / 2)
        num = mylist[mid]
        if num == n:
            return mid
        if num > n:
            high = mid - 1
        else:
            low = mid + 1
    return "Числа нет в уникальном списке нет"

l = list(set(randint(1, 100) for i in range(10))) # числа от 1 до 240000
n = randint(1, 100) #число которое нужно найти
l.sort()
print(f"Index элемента '{n}' списка {l}: {binary_search(l, n)}")
