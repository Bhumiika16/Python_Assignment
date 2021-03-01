#The number of directions the person wants to give, which will decide how many times the loop will run.
number_of_directions = int(input())
length = 0
breadth = 0

#In this loop input is taken and simulataneously the distance is being added or subtracted accordingly. 
for i in range(number_of_directions):
    
    directions = list(map(str, input().split(" ")))
    
    if(directions[0] == "UP"):
        length = length + int(directions[1])
        
    elif(directions[0] == "DOWN"):
        length = length - int(directions[1])
        
    elif(directions[0] == "LEFT"):
        breadth = breadth - int(directions[1])
        
    elif(directions[0] == "RIGHT"):
        breadth = breadth + int(directions[1])
        
    else:
        print("Wrong Input")

#Applied Pythagoras theorem for finding the shortest distance. Where distance is considered as hypotaneous.        
distance = ((length**2) + (breadth**2))**0.5
print(int(distance))