# tuple demo
def add_to_tuple(t, value):
    """ check every elemennt in tuple to determine wether the element is mutable"""
    for element in t:
        if type(element) is list:
            element.append(value)
        elif type(element) is tuple:
            print(f'tuple is immutable. ')
        elif type(element) is set:
            element.add(value)
        elif type(element) is dict:
            print('need key to modify the dictionary.')
        else:
            print(type(value))
t1 = ([1,2],('apple', 'orange'),{5,11},{1:'one',2:'tow'},78)
add_to_tuple(t1,67)
print(t1)
