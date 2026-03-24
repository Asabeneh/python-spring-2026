user = {'name':'Asab', 'age': 250, 'email':'asab@gmail.com'}

print(user)
print(user['name'])
print(user['age'])
print(user['email'])

# print(user['gender'])
print(user.get('gender'))

if 'gender' not in user:
    print(user['name'], 'does not have gender')