'''
Builtin function are functions that exists by default
print() Done
len() Done
str() DONE
type() DONE
int() DONE
float() Done
input() DONE
round() DONE
abs() DONE
min() DONE
max() Done
sum() Done
list()
range()

'''
# print() - display the provided input
print('Hello', 'World', 2026, 'Learning Python', [1, 2, 3, 4], True)

# len(): It returns the length of the input
print(len('cat'))
print(len('Finland'))
print(len('cat dog'))
print(len([1, 2, 3]))
print(len({1, 2, 3}))
print(len({1, 2, 2, 3, 3}))
print(len({'name':'Asab', 'age':250,'is_married':True}))

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
country = 'Finland'

full_name = first_name + ' ' +  last_name
print(full_name)
print('My name is '+ full_name + '. ' + 'I live in '+ country +' and I am ' + str(age)  + ' years old.')

print(f'My name is {full_name}. I live in {country} and I am {age} years old.')

print('My name is {0}. I live in {1} and I am {2} years old. {1} is beautiful.'.format(full_name, country, age))

'''
My name is Asabeneh Yetayeh. I live in Finland and I am 250 years old.

'''

print(10, '10')
print(type(10), type('10'), int('10'), type(int('10')))

print(str(10) + '10')
print(10 + int('10'))

print('9.81', type('9.81'))
print(float('9.81'), type(float('9.81')))
print(float('9.81') * 100, int(float('9.81') * 100))

""" current_year = 2026
name = input('Enter your name: ')
birth_year = int(input('Enter your birth year: '))
print(name, current_year, birth_year, type(birth_year))
age = current_year - birth_year

print(f'You are {name}. You were born in {birth_year}. Now, you are {age} years old.') """

mass = 75.5
gravity = 9.81 
weight = mass * gravity 

print(weight, round(weight), round(weight, 2))
print(abs(-10))
print(min(10, 20, -10, 0, 30, 21))
print(max(10, 20, -10, 0, 30, 21))
print(sum([10, 20, -10, 0, 30, 21]))

print(list())
print(list('cat'))
print(list({1, 2, 3, 4, 5}))

print()

even_numbers = list(range(0, 101, 2))
print(even_numbers)

odd_numbers = list(range(1, 101, 2))
print(odd_numbers)
