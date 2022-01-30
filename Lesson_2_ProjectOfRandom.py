from random import *

def is_valid(start, end, n):
    if  n.isdigit() and start <= int(n) <= end:
        return True
    else:
        return False

def game(x):
    
    flag = False
    
    print("Добро пожаловать в числовую угадайку! Введите число")
    cnt = 0
    while flag == False:
        n = input()
        if is_valid(start, end, n):
            while flag == False:
                n = int(n)
                if n < x:
                    print("Ваше число меньше загаданного, попробуйте еще разок")
                    cnt += 1
                    break
                elif n > x:
                    print("Ваше число больше загаданного, попробуйте еще разок")
                    cnt += 1
                    break
                else:
                    print("Вы угадали, поздравляем! Кол-во попыток: ", cnt)
                    flag = True
                    
                    break
            
        else:
            print("А может быть все-таки введем целое число от 1 до 100?")
            continue

ask = ''
while True:
    print("Сыграем в угадайку? д - да, н - нет!")
    ask = input()
    if ask == 'д':
        start, end = 1, 100
        x = randint(start, end)
        game(x)
    elif ask == 'н':
        print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
        break
    else:
        print("Некорректные данные\n")
