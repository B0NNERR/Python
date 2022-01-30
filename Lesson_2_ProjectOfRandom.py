from random import *

def is_valid(start, end, n):
    if  n.isdigit() and start <= int(n) <= end:
        return True
    else:
        return False


start, end = 1, 100
x = randint(start, end)
flag = False
print("Добро пожаловать в числовую угадайку")
flag = False
while flag == False:
    n = input()
    if is_valid(start, end, n):
        while True:
            n = int(n)
            if n < x:
                print("Ваше число меньше загаданного, попробуйте еще разок")
                break
            elif n > x:
                print("Ваше число больше загаданного, попробуйте еще разок")
                break
            else:
                print("Вы угадали, поздравляем!")
                print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
                flag == True
                break
        
    else:
        print("А может быть все-таки введем целое число от 1 до 100?")
        continue
    
    
