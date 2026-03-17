
from countries import countries

nums = [1, 2, 3, 4, 5] # [1, 4, 9, 16, 25]


new_lst = []
for num in nums:
    new_lst.append(num * num)
print(new_lst)

squared_list = [num * num for num in nums]
print(squared_list)

# countries = ['Finland','Sweden','Norway','Denmark','Iceland']
# country_codes = [country.upper()[:3] for country in countries]
# print(country_codes)
# countries_with_land = [c for c in countries if 'land' in c]
# print(countries_with_land)

lst_lst =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_lst = []
for lst in lst_lst:
    flattened_lst.extend(lst)
    # for num in lst:
    #     flattened_lst.append(num)
print(flattened_lst)

country_codes = [ country.upper()[:3] for country in countries]
print(country_codes)

countries_with_land = [country for country in countries if 'land' in country]
print(countries_with_land)


countries_with_stan = [country for country in countries if 'stan' in country]
print(countries_with_stan)