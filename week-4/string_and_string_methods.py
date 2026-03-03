# What is a string?
# A string could be a single character or a big page of text

letter = 'a' # one character string
word = 'love' # multiple characters
sentence = 'I love people'
next_week_lessons = """
String and String Methods: https://www.youtube.com/watch?v=m8otfcdOA3E
List and List methods: https://www.youtube.com/watch?v=5shjY9yN_J0
Loops: https://youtu.be/xSqvQKVj_2I?si=QJ8m6c8mEiC49dbr
"""

# String methods

print(sentence.upper())
print(sentence.lower())
print(sentence.title())
print(sentence.swapcase())

first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250 
country = 'Finland'
height = 1.72

# I am Asabeneh Yetayeh. I live in Finland and I am 250 years old, and 1.72 meter tall.

# full_name = first_name + ' ' +  last_name
full_name = f'{first_name} {last_name}'

print(full_name)
print(f'I am {full_name}. I live in {country} and I am {age} years old, and {height} meter tall.')

print('I love people.\nI love Python too.\nIf I do not love Python what else can I love.')
print('Here is my words:\n\t* I love people.\n\t* I love Python too.\n\t* If I do not love Python what else can I love.')

print('Days\tTopics\tExercises') # adding tab space or 4 spaces
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')

print('In the old Python it was impossible to print the symbol slash(\)')
print('In the old Python it was impossible to print the symbol slash(\\)')
print('I don\'t like to go outside')
print("The saying that goes \"an apple a day keeps the doctor way\" is not really true")


print('I am %s. I live in %s and I am %d years old, and %.2f meter tall.' %(full_name, country, age, height))
print('I am {0}. I live in {1} and I am {2} years old, and {3} meter tall. Someone who is {3} is is not a tall person.'.format(full_name, country, age, height))
print(f'I am {full_name}. I live in {country} and I am {age} years old, and {height} meter tall.')


a = 3 
b = 4 

print(f'{a} + {b}  = {a  + b}')
print(f'{a} - {b}  = {a  - b}')
print(f'{a} x {b}  = {a  * b}')
print(f'{a} / {b}  = {a  / b}')

print('{} + {}  = {}'.format(a, b, a + b))
print('{} - {}  = {}'.format(a, b, a - b))
print('{} x {}  = {}'.format(a, b, a * b))
print('{} / {}  = {}'.format(a, b, a / b))

# Accessing character using index

word = 'love'
print(word[0])
print(word[1])
print(word[2])
print(word[3])

# What is the last index 
last_index = len(word) - 1
print(word[last_index])
print(word[1:])
print(word[1:3])
print(word[0:2])
print(word[:2])

# Natural Language Processing

print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-3:-1])

print('love'[::-1])

# Checking if two words are palindrome 
# civic, level, racecar

print('level' == 'level'[::-1])
print('racecar' == 'racecar'[::-1])

language = 'Python'
pto = language[0:6:3] #
print(pto) # Pto

txt = 'thirty days of Python'
print(txt.capitalize())
print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.swapcase())
print(txt)
print(txt.strip()) # removes spaces both in the left and right side of the string
print(txt.count('o'))
print(txt.count('th'))
print(txt.count('y'))
print(txt.startswith('t'))
print(txt.startswith('thirty'))
print(txt.endswith('y'))
print(txt.endswith('n'))
print(txt.endswith('on'))

challenge = 'thirty\tdays\tof\tpython'
print(challenge)
print(challenge.expandtabs(10))   # 'thirty  days    of      python'
print(challenge.expandtabs(12)) # 'thirty    days      of        python'

print(txt.find('t'))
print(txt.find('z'))
print(txt.rfind('t'))
print(txt[17:])
print(txt.find('of'))

print(txt.index('t'))
print(txt.index('of'))
print(txt.rindex('t'))
# print(txt.index('z')) crashing

print('cat'.isalpha())
print('cat'.isalnum())
print('cat123'.isalpha())
print('cat123'.isalnum())
print('123'.isdecimal())
challenge = '\u00B2'
print(challenge.isdigit())   # True 

num = '10.5'
print(num.isnumeric()) # False

web_tech = ['HTML', 'CSS', 'JavaScript', 'React','Python', 'Data Analysis']
result = ', '.join(web_tech)
print(result) # 'HTML CSS JavaScript React'

sentence = 'I love people. People are great.'.replace('.', '').lower()
print(sentence)
words = sentence.split()
unique_words = set(words)
print(words)
print(unique_words)
total_word_count = len(words)
unique_words_count = len(unique_words)
print(unique_words_count / total_word_count )


