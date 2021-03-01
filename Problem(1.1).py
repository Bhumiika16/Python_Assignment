def sum_of_integer(num):
    
    #If the value passed to the function is an integer then the if condition will work otherwise the function will return zero.
    if(type(num) == int):
        add = 0
        #The loop will run from 1 till the number and will add on with each iteration.
        for i in range(1,num+1):
            add = add + i
        return add
    else:
        return 0

#function call
output = sum_of_integer(int(input()))
print(output)