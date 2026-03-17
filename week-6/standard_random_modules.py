import random
from math import floor

print(dir(random))


def find_weeky_lucky_number(n = 7):
    numbers = []
    for i in range(n + 1):
        random_number = floor(random.random() * 11)
        numbers.append(random_number)
    return numbers

print(find_weeky_lucky_number(10))

def random_id_generator(n = 4):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    length = len(letters) # 62
    id = ''
    for i in range(n + 1):
        index = floor(random.random() * length) # 0 61
        value = letters[index]
        id = id + value
    return id

print(random_id_generator())
print(random_id_generator(24))

'''
Teach me something. Teach my step by step, one concept at a time and evalute my understanding before you move to the next concept with exercise and quiz.


'''


