def my_func(int_one,int_two):
    
    if(int_one < int_two):
        output_list = []
        #As for loop runs one less then the end point so one is added with the end point.
        for i in range(int_one,int_two+1):
            output_list.append(i)
        return output_list
    
    else:
        return 0
            
#Calling a function and simultaneously taking input from user
result = my_func(int(input("Enter First Integer : ")), int(input("Enter Second Integer : ")))
print(result)