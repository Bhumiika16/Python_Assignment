#Took input of comma separated integers
input_list = list(map(int, input().split(",")))

#Used list comprehension to append the negative of the list elements.
output_list = [-(integer) for integer in input_list]
print(output_list)