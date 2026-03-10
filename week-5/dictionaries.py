'''
Dictionary is a key value pair
'''
from pprint import pprint

empty_dict = {}
print(type(empty_dict))
print(len(empty_dict))

user = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age': 250,
    'date_of_birth':'1926',
    'country':'Finland',
    'is_married':True, 
    'skills':['HTML','CSS','JS','Python'],
    'username':'asab',
    'email':'asab@asb.com',
    'password':'123123',
    'created_at': '10/13/2026 19:28',
    'bio':'I am a fullstack engineer & instructor. I teach Pyton ...',
     'address': {
         'street':'Space Street',
         'zipcode': '02700',
         'city':'Helsinki'
     }
}
print(type(user))
print(len(user))
print(user['username'])
print(user['email'])
print(user.get('tel'))
if user.get('tel'):
    print(user.get('tel'))
else:
    user['tel'] = '0010010'

pprint(user)
user['age'] = 40

print(user)
user['address']['fax'] = 'FAX-123456666'
pprint(user)
user['skills'].append('ML')

pprint(user)

for key in user:
    print(key, '::::', user[key])

# Dictionary methods

keys = user.keys()
print('Keys::::>', keys)


values = user.values()
print('values::::>', values)

items = user.items()
print(items)

for item in items:
    print(item[1])


print('age' in user)
# del user['age']
user.pop('age')

pprint(user)
# user.clear()
print(user)
user_copy = user.copy()