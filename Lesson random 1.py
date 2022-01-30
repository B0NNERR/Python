from random import *

x = randint(1, 100)




while True:
    n = int(input())
    if n > x:
        print("Слишком много, попробуйте еще раз")
        continue
    elif n == x:
        print("Вы угадали, поздравляем!")
        break
    else:
        print("Слишком мало, попробуйте еще раз")
        continue
    

print(f"\nСлучайное число = {x}"
      f"\nЧисло введеное пользователем = {n}")
