
from countries import countries
""" 
f = open('countries.txt', 'w')

for country in countries:
    if 'land' in country:
         f.write(f'Going to {country} will be my life time dream\n')
    else:
          f.write(f'I like to go to {country}.\n') """

f = open('example.txt', 'w')
for country in countries:
    if 'land' in country:
        f.write(f'Going to {country} will be a dream come true.\n')
    else:
        f.write(f'I like to go to {country}.\n')

    # print(country)
# f.write('some thing for example')
