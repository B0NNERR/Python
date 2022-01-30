from random import *

x = randint(1, 100)

n = int(input())

if n > x:
    print("Слишком много, попробуйте еще раз")
elif n == x:
    print("Вы угадали, поздравляем!")
else:
    print("Слишком мало, попробуйте еще раз")

print(f"n = {n}, x = {x}")
