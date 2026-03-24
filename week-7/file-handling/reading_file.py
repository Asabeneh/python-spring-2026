
def read_file_content():
    f = open('./countries.txt')
    lines = f.read().splitlines()
    countries = []
    for line in lines:
        words = line.replace('.', '')
        if 'Going' in words:
            print(words)
            some_part_of_str = words[8:]
            index_of_will = some_part_of_str.index(' will')
            print('land country:', some_part_of_str[0: index_of_will:])
            country = some_part_of_str[0: index_of_will:]
            countries.append(country)
        else:
            start = len('I like to go to ')
            country = words[start:]
            countries.append(country)



countries = []
f = open('./example.txt')
lines = f.read().splitlines()
for line in lines:
    txt = 'I like to go to'
    if line.startswith(txt):
        n = len(txt)
        country = line[n:].replace('.', '')
        countries.append(country)

    else:
        txt = ' will be a dream come true.'
        middle_part = line[8:]
        start_index = middle_part.index(' will')
        country = middle_part[0: start_index]
        countries.append(country)

print(countries)
 
    
    

     
     
       


