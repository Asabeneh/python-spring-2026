""" a = 0

if a > 0:
    print(f'{a} is positive number')
elif a == 0:
    print(f'{a} is a zero')
else:
    print(f'{a} is a negative number')


is_raining = False 

if is_raining == True:
    print('Go out with an umbrella')
else:
    print('Go out freely') """
    


weather = input('What is the weather today? ').lower()
print(weather)

if weather == 'rainy':
    print('Go out with raincoat')
elif weather == 'sunny':
    print('Just go out freely it a shinny day')
elif weather == 'cloud':
    print('There might be rainy')
elif weather == 'foggy':
    print('There might be visibility issues')
elif weather == 'snowy':
    print('It might be slippery')
else:
    print('No one knows about today weather')


