'''
def, name, ():

'''
def do_something (para):
    print(f'i am {para}')


do_something('teaching')
do_something('learning')

'''

The name of the function is calculate_rectangle_araa. 
It takes length and width as a parameter and returns the area of the rectangle
area = length * width

Calucate the area of the rectangle with 10 and 20, 30 and 40.

'''

""" def calculate_rectangle_area(length, width):
    print ("Area of rectangle is", length * width)
    lenghth = 10
    width = 20
    return calculate_rectangle_area(length, width) """


def calculate_rectangle_area(length, width):
    area = length * width
    return  f"Area of the rectangle with length of {length} and width of {width} is {area}."


print(calculate_rectangle_area(10, 20))
print(calculate_rectangle_area(30, 40))


'''

The name of the function is sum_all_nums and it takes unlimited number of inputs or arguments and it returns the sum of all the arguments.

sum_all_nums(1, 2, 3, 4, 5, 10, 20)

'''

def sum_all_nums(*args):
    is_true = all(isinstance(item, int) for item in args)
    if is_true:
        return sum(args)
    else:
        return 'You have invalid input'



    # return sum(args)

print(sum_all_nums(1, 2, 3, 4, 5, 100, 200, -200,'apple'))



# print(isinstance(1, int))
# print(isinstance('1', int))
# print(isinstance('1', str))
# print(isinstance([], list))
# print(isinstance(True, bool))