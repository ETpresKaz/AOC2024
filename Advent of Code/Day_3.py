import re


with open ('Day_3.txt', 'r') as file:
  data = file.read().split('\n')

pattern1 = r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)"
result = []
summation = []
on_off = False

def find_pattern(text):
  matches = re.findall(pattern1, text)
  global on_off

  for match in matches:
    if match == "do()":
      on_off = True
    elif match == "don't()":
      on_off = False
    else:
      if on_off:
        num1, num2 = int(match[4]), int(match[6])
        
        result.append((num1, num2))
        mul_num = num1 * num2
        summation.append(mul_num)
  return result



for line in data:
  find_pattern (line)

print(sum(summation))
