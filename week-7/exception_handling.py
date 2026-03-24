""" try:
    mass = float(input('Enter mass: '))
    height = float(input('Enter your height: '))
    bmi = mass  / height * height
    print(f'Your bmi for the weight {mass} kg and height {height} meters is {bmi}.')
except TypeError:
    print('This is a type error')
except ZeroDivisionError:
    print(f'The give value for height is {height}. A zero division error, a number can not be divided by zero. Try again with non-zero value') """


try:
    mass = float(input('Enter mass: '))
    height = float(input('Enter your height: '))
    bmi = round(mass  / (height * height), 2)
    print(f'Your bmi for the weight {mass} kg and height {height} meters is {bmi}.')
except Exception as e:
    print(f'The give value for height is {height}. {e}. Try again!!')
# else:
#     print('This block will executed if there is no exception')

# finally:
#     print('I will be executed no matter what.')