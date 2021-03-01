#Comma separated input from user
input_list = list(map(int, input().split(",")))

#List comprehension where square of all the odd number is appended to the list.
output_list = [num**2 for num in input_list if num % 2 != 0]
print(output_list)