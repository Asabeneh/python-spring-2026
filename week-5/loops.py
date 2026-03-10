'''
Loops

print('Hello World')
Loops allows to solve repetive problems


'''
from countries import countries

nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num)

# countries = ['Finland','Sweden','Norway','Denmark','Iceland']
# for country in countries:
#     print(country, country.upper(), country.upper()[:3])


print(list(range(0, 11, 10)))

for i in range(1, 11):
    print(f'{i} - Hello World!')


for country in countries:
    if 'land' in country:
        print(country)

# print(countries)

shopping_list = ['Milk-R','Meat-R','Apple-RT','Coffe-RT','Tea-RT','Sugar-RT','Honey-RT','Yoghurt-R']

for item in shopping_list:
    if item.endswith('-R'):
        print(item.strip('-R'))


for country in countries:
    if 'stan' in country:
        print(country)


print('======= Countries with two or more words ==========')
for country in countries:
    words = country.split()
    if len(words) > 1:
        print(country)

'''

Sum all the number from 0 to 100

'''
nums = list(range(10, -1, -1))  # 0 to 100 range takes to input
print(nums)
total = sum(nums)
print(total)

nums = [10, -25, 30, 50, 40, 35, 90, 100]
print(sum(nums))

total = 0 # 0 + 10 = 10 => 10 - 25 = -15 => -15 + 30 = 15 => 15 + 50 = 65 => 65 + 40 = 105 => 105 + 35 = 110
for num in nums:
    total = total + num
    print(total)


'''

Sum all the even numbers from 0 to 100

'''
evens = list(range(0, 101, 2))
total = sum(evens)
print(total)

total = 0 
for even in evens:
    total = total  + even 

print(total)

countries = ['Finland','Sweden','Norway','Denmark','Iceland'] # ['Iceland', 'Denmark', ...]

# ['FIN', 'SWE', 'NOR', 'DEN', 'ICE']

""" country_codes = []

for country in countries:
    code = country.upper()[0:3]
    country_codes.append(code)

print(country_codes)


nums = []

for c in countries:
    nums.append(c.upper())

print(nums)


names = ['John','David' ,'Robort', 'Asabeneh']

for name in names:
    if len(name) > 7:
        print(f'{name} - You got a long name')
    else:
         print(f'{name} - You got a short name') """


countries_reversed_order = []
for i in range(len(countries)-1, -1, -1):
    country = countries[i]
    countries_reversed_order.append(country)

print(countries_reversed_order)


# While loop 

for i in range(6):
    print(i)


print(' ====== While loop ===============')

i = 0 
while i < 101:
    print(i)
    i = i  + 2


# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1

i = 10 
while i >= 0:
    print(i)
    i = i - 1


'''
Number guessing age

'''

number = 55
""" attempts = 0

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
   """

import random

def play_game():
    # Setup the game
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    print("=" * 50)
    print("🎯 WELCOME TO THE NUMBER GUESSING CHALLENGE! 🎯")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to find it. Good luck!")
    print("=" * 50)

    while attempts < max_attempts:
        try:
            # Display remaining lives and get input
            remaining = max_attempts - attempts
            print(f"\n❤️  Attempts left: {remaining}")
            user_input = int(input('Enter your guess: '))
            
            attempts += 1

            # Check the guess
            if user_input == secret_number:
                print(f"\n✨ {'=' * 10} BOOM! YOU DID IT! {'=' * 10}")
                print(f"CONGRATULATIONS! You won in {attempts} attempts!!!!!")
                return # Exit the function/game

            # Provide smart hints
            if user_input > secret_number:
                diff = "slightly" if user_input - secret_number < 10 else "much"
                print(f"❌ {user_input} is {diff} too HIGH.")
            else:
                diff = "slightly" if secret_number - user_input < 10 else "much"
                print(f"❌ {user_input} is {diff} too LOW.")

        except ValueError:
            print("⚠️  That's not a number! Please enter a valid integer.")
            # Note: We don't count invalid inputs as an attempt!

    # Out of attempts
    print("\n" + "☠️" * 15)
    print(f"GAME OVER! You've run out of tries.")
    print(f"My secret number was: {secret_number}")
    print("Better luck next time!")
    print("☠️" * 15)

if __name__ == "__main__":
    play_game()


