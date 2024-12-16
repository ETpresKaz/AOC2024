import math

from itertools import permutations


print("Starting...")
with open('Day_7_test.txt') as f:
    data = f.read()

test_values = {}
tHIngS_i_WaNT_tO_ADd = []


def check_all_options(data):
    perms = []
    for perm in permutations(data):
        perms.append(perm)
        
    return perms



def parse_data(data):
   
    for line in data.splitlines():
        key, value = line.split(':')
        test_values[int(key.strip())] = [int(num) for num in value.strip().split()]
    return test_values

#print(parse_data(data))

parse_data(data)

for i in test_values:
    if sum(test_values[i]) == i:
        tHIngS_i_WaNT_tO_ADd.append(i)
    if math.prod(test_values[i]) == i:
        tHIngS_i_WaNT_tO_ADd.append(i)
    if i in check_all_options(data):
        tHIngS_i_WaNT_tO_ADd.append(i)
print("___________")
print(check_all_options(data))

