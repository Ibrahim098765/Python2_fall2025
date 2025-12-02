d = {}
print(f'{type(d)}')
#empty setr
s = set()
d = {1:'one',2:'tow',3:'three'}
print(f'display d:{d}')
# generate dic using dic comrehension
num_dict = {k:k*2 for k in range(1,11)}
print(f'number dict:{num_dict}')
# access vaalue from key
print(f'd[1] = {d[1]}')
print(f'd[4] = {d.get(4, 'key does not exist')}')
# remove key value pair
print(f'popping item = {d.pop(4, 'key does not exist')}')