'''
map
filter
reduce
'''
from functools import reduce
from countries import countries
nums = [1, 2, 3, 4, 5]  # [1, 4, 9, 16, 25]

squared_numbers = list(map(lambda n: n ** 2, nums))
print(squared_numbers)

evens = list(filter(lambda n: n % 2 == 0, nums))
print(evens)
countries_code = list(map(lambda country: country.upper()[:2], countries))
print(countries_code)

countries_code = list(map(lambda country: country.upper()[:2], countries))
print(countries_code)

countries_with_land = list(filter(lambda country: 'land' in country, countries))
print(countries_with_land)


# total = 0
# for num in nums:
#     total = total + num
#     print(num)

# print(total)

sum_total = reduce(lambda acc, cur: acc + cur, nums)
print(sum_total)




