# List is an index ordered items and they are mutable.

empty_lst = []
print(type(empty_lst))
print(len(empty_lst))

nums = [1, 2, 3, 4, 5]
names = ['Brigette','Dinushi','Rakesh', 'Unknown']
print(len(names))

shopping_list = ['Milk', 'Potatoes', 'Coffee','Tea','Sugar']
print(shopping_list[0])
print(shopping_list[1])
print(shopping_list[2])
print(shopping_list[3])
print(shopping_list[2:4])
print(shopping_list[1:4])
print(shopping_list[-1])
print(shopping_list[-2])
print(shopping_list[-3])
print(shopping_list[-3:-1])
print(shopping_list[-4:-2])
shopping_list.append('Fish')
print(shopping_list)
shopping_list.append('Beaf')
print(shopping_list)
print(len(shopping_list))

shopping_list.insert(2, 'Onion')
print(shopping_list)
shopping_list.insert(0, 'Orange')

print(shopping_list)

shopping_list[6] = 'Honey'

print(shopping_list)
shopping_list[0] = 'Mango'
print(shopping_list)

shopping_list.extend(['Tomatoes','Cabbage','Lettuce','Garlic'])
print(shopping_list)
print('Mango' in shopping_list)

shopping_list.pop()
print(shopping_list)
shopping_list.pop()
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)
shopping_list.remove('Potatoes')
print(shopping_list)
del shopping_list[0]
print(shopping_list)
del shopping_list[1:3]
print(shopping_list)

# shopping_list.clear()
# print(shopping_list)

shopping_list_copy = shopping_list.copy()

shopping_list.clear()

print(shopping_list)
print(shopping_list_copy)

positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
fruits = ['banana', 'orange', 'mango', 'lemon']
vegetables = ['Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables ) # ['banana', 'orange', 'mango', 'lemon', 'Tomato', 'Potato', 'Cabbage', 'Onion', 'Carrot']

ages = [22, 19, 24, 25, 26, 24, 25, 24]
print(ages.index(24))  
ages_copy = ages.copy()

# ages.reverse()
# print(ages)
ages.sort(reverse=True)

print(ages)