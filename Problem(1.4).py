def polygon(length,breadth):
    
    #To check if a polygon is square
    if(length == breadth):
        return length*length
    
    else:
        return 2*(length + breadth)

#Calling a function and simultaneously taking input from user.    
result = polygon(int(input("Enter Length : ")),int(input("Enter Breadth : ")))
print(result)