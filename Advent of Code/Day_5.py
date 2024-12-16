import re


def find_middle(s):
    nums = list(map(int, s.split(',')))
    middle_index = len(nums) // 2
    middle_num = nums[middle_index]
    sum_lst.append(middle_num)

def find_middle_v2(s):
    nums = list(map(int, s.split(',')))
    middle_index = len(nums) // 2
    middle_num = nums[middle_index]
    sum_lst_v2.append(middle_num)

with open('Day_5_input.txt') as f:
    input_lines = f.read().splitlines()

with open('Day_5_rules.txt') as f:
    rules = f.read().splitlines()

#print(input_lines)
#print(rules)
#print(len(input_lines))

counter_1 = 0
sum_lst = []

rule_dict = {}
for rule in rules:
    left, right = map(int, rule.split('|'))
    if left not in rule_dict:
        rule_dict[left] = []
    rule_dict[left].append(right)

#print(type(input_lines))
for line in input_lines:
    nums = list(map(int, line.split(',')))
    valid = True
    
    
    for left, rights in rule_dict.items():
        for right in rights:
            if left in nums and right in nums:
                if nums.index(left) > nums.index(right):
                    valid = False
                    break
        if not valid:
            break

    if valid:
        print(line)
        counter_1 += 1
        find_middle(line)

print(counter_1)
print(sum(sum_lst))


def re_order(x_rules, y_inputs):
    nums = list(map(int, y_inputs.split(',')))
    
    for left, rights in x_rules.items():
        for right in rights:
            if left in nums and right in nums:
                if nums.index(left) > nums.index(right):
                    nums.remove(left)
                    nums.insert(nums.index(right), left)
    
    fixed_input = ','.join(map(str, nums))
    find_middle_v2(fixed_input)










counter_2 = 0
sum_lst_v2 = []



for line in input_lines:
    nums = list(map(int, line.split(',')))
    valid = True
    
    for left, rights in rule_dict.items():
        for right in rights:
            if left in nums and right in nums:
                if nums.index(left) > nums.index(right):
                    valid = False
                    break
        if not valid:
            break

    if not valid:
        re_order(rule_dict, line)
        counter_2 += 1


print(counter_2)
print(sum(sum_lst_v2))