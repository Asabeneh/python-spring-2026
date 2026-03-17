'''

Functions - Builtin and custom functions
Modules


'''
from countries import countries

def make_square(n):
    return n ** 2 


def add_two_nums (a, b):
    return a  + b 


def sum_all_nums(*args):
    is_true = all(isinstance(item, int) for item in args)
    if is_true:
        return sum(args)
    else:
        return 'You have invalid input'
    

def find_countries_pattern (pattern):
    return [country for country in countries if pattern in country]



def number_guessing_game ():
    import random
    number = random.randint(0, 100) # 0 and 100
    attempts = 0

    while True:
        user_input = int(input('Enter number: '))
        
        # 1. Check for the win first (on any attempt 0-6)
        if number == user_input:
            attempts = attempts + 1 # Count the final successful attempt
            print(f'==== You got the number. CONGRATULATION! YOU WON, at {attempts} attempts!!!!! ====')
            break
        
        # 2. Check if this was the 7th failed attempt
        elif attempts == 6:
            attempts = attempts + 1
            print(f'==== YOU LOST, at {attempts} attempts. Try again!!!!! ====')
            break

        attempts = attempts + 1

        # 3. Give hints
        if user_input > number:
            print(f'{user_input} is much bigger than my number. Try again with a smaller number')
        else:
            print(f'{user_input} is much lower than my number. Try again with a bigger number')

# number_guessing_game()
  
def find_countries_with_two_words(lst):
    new_lst = []
    for country in lst:
        words = country.split()
        if len(words) > 1:
            new_lst.append(country)
    return new_lst