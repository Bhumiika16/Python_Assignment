#Took comma separated input from the user.
input_list = list(map(int, input().split(",")))

#Initialized the value as one.
list_len = 1

for num in range(len(input_list)-1):
    
    #Check if consecutive number has a difference of one, otherwise it will print the number and break the loop.
    if(input_list[num+1] - input_list[num] == 1):
        list_len += 1
        continue
        
    else:
        print(input_list[num+1])
        break
        
if(list_len == len(input_list)):
    print("Null")        