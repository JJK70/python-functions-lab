# Exercise 1

# def sum_to(num):
#   sum = 0
#   for n in range(1, num + 1):
#     sum += n
#   return sum

# print(sum_to(6))
# print(sum_to(10))

# Exercise 2

# def largest(nums):
#   largest = 0
#   for num in nums:
#     if num > largest:
#       largest = num
#   return largest
# print(largest([1,2,3,4,0]))
# print(largest([10,4,2,231,91,54]))

# Exercise 3

# def occurances(string, substr):
#   stripped_string = string.replace(substr, '')
#   return (len(string) - len(stripped_string)) // len(substr)

# print(('fleep floop', 'e'))
# print(('fleep floop', 'p'))
# print(('fleep floop', 'ee'))
# print(('fleep floop', 'fe'))

# Excercise 4

def product(*args):
  finalProduct = 1
  for arg in args:
    finalProduct *= arg
  return finalProduct


print(product(-1,4))
print(product(2, 5, 5))
print(product(4, 0.5, 5))