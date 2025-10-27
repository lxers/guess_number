from random import randint

def guess():
    num_rand = randint(1, 100)
    while True:
        num = int(input('Введите число: '))

        if num_rand > num: 
            print('Выше')
        elif num_rand < num: 
            print('Ниже')
        else:
            print('ВЫ УГАДАЛИ!')
            break

def empty(): # Тут я добавил пустую функцию потому что в функции guess() у меня уже стоял elif. 
    pass 

guess()