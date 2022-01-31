import random
word_list = ['красный', 'треугольник', 'апельсин', 'медведь', 'грейпфрут', 'ниндзя', 'коктель', 'вертушка',
             'гиббон', 'артель', 'силикон', 'штанга', 'шифер', 'принадлежность', 'параболоид', 'длиномер',
             'контроллер']
error_words = ['Не то печатаешь, давай заново',
               'Что печатаешь, двоечник! Заново',
               'Ошибка. Пробуй заново',
               'Кто тебя учил текст набирать? Удаляю и снова печатай',
               'Неверный текст, снова давай',
               'Галиматья, опять давай',
               'Чушь! Нет таких букв в алфавите. Снова давай']
guessed_list = ['Ты уже писал такое. Напряги извилины',
                'Тебе надо на свежий воздух. То же самое пишешь',
                'Было уже. Попробуй еще',
                'Опять! было уже',
                'Что заладил одно и то же. Давай думай еще',
                'Нет. Было уже. Еще варианты']
win_words = ['Выиграл! Красава! ', 'Угадал, Дай пять! Хотя нет, можешь нажать пять раз [Enter]',
             'Ты разгадал! Всеми правдами и неправдами ты сделал это']
guess_words = ['Есть такая буква', 'Угадал букву']
not_guess_words = ['Нет такого слова', 'Вот и не угадал', 'Не угадал', 'Не то слово',
                   'Хватит себя мучать. Угадывай буквы', 'Нет. Не выдумаывай']
not_guess_letter = ['Нет такой буквы', 'Вот и не угадал', 'Не угадал', 'Не та буква',
                    'Подумай еще и начни с другой буквы', 'Нет. Не выдумаывай']
loser_words = ['Ты loser!', 'Ха! Не угадал. Ты проиграл', 'Ты не смог угадать', 'Game over']


def get_word(text_list):
    word = random.choice(text_list)
    return word.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                Повесили чувака
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                Осталась 1 попытка
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                Осталось 2 попытки
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                Осталось 3 попытки
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                Осталось 4 попытки
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                Осталось 5 попыток
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                Осталось 6 попыток
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = ['*' for _ in range(len(word))]  # список, содержащий символы _ на каждую букву задуманного слова
    guessed = False                                   # сигнальная метка
    guessed_letters = []                              # список уже названных букв
    guessed_words = []                                # список уже названных слов
    tries = 6                                         # количество попыток
    print('Давайте играть в угадайку')
    print(display_hangman(tries))
    print(f'Слово из {len(word)} букв ', *word_completion, sep='')
    while not guessed:
        word_input = input('Введите букву или слово ').upper()
        if not word_input.isalpha():
            print(get_word(error_words))
            continue
        if word_input in guessed_letters or word_input in guessed_words:
            print(get_word(guessed_list))
            continue
        if len(word_input) > 1:
            if word_input == word:
                print(get_word(win_words))
                break
            else:
                guessed_words.append(word_input)
                tries -= 1
                print(get_word(not_guess_words))
                print(display_hangman(tries))
                print(f'Слово из {len(word)} букв ', *word_completion, sep='')
        if len(word_input) == 1:
            guessed_letters.append(word_input)
            if word_input in word:
                guessed = True
                for i in range(len(word)):
                    if word[i] == word_input:
                        word_completion[i] = word_input
                    if not word_completion[i].isalpha():
                        guessed = False
                if guessed:
                    print(f'Да! Слово из {len(word)} букв это', *word_completion, sep='')
                    print(get_word(win_words))
                else:
                    print(get_word(guess_words))
                    print(display_hangman(tries))
                    print(f'Слово из {len(word)} букв ', *word_completion, sep='')
            else:
                tries -= 1
                print(get_word(not_guess_letter))
                print(display_hangman(tries))
                print(f'Слово из {len(word)} букв ', *word_completion, sep='')
        if tries == 0:
            print(get_word(loser_words))
            break


play(get_word(word_list))
