import random as r



digits = '0123456789'

lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

punctuation = '!#$%&*+-=?@^_'

chars_except = '1234567'



chars_list = []

count_pass = int(input('Количество паролей для генерации: '))

len_pass = int(input('Длина одного пароля: '))



# формируем массив, из которого будет генерировать пароли

if bool(int(input('Включать цифры {}? 1 Да, 0 - Нет '.format(digits)))): 

    chars_list.append(tuple(digits))

if bool(int(input('Включать прописные буквы {}? 1 Да, 0 - Нет '.format(uppercase_letters)))):

    chars_list.append(tuple(uppercase_letters))

if bool(int(input('Включать строчные буквы {}? 1 Да, 0 - Нет '.format(lowercase_letters)))): 

    chars_list.append(tuple(lowercase_letters))

if bool(int(input('Включать символы {}? 1 Да, 0 - Нет '.format(punctuation)))): 

    chars_list.append(tuple(punctuation))



chars_except_enable = bool(int(input('Исключать неоднозначные символы {}? 1 Да, 0 - Нет '.format(chars_except))))




for i in range(1, count_pass + 1):

    chars = ''

    for _ in range(len_pass):

        ch = r.choice(r.choice(chars_list))

        if chars_except_enable:

            while ch in chars_except:

                ch = r.choice(r.choice(chars_list))

        chars += ch        

    print('\n', i, 'пароль:  ', chars)
