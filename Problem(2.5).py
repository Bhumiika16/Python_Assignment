#Length, Breadth and Heigth of both the cuboid is taken as an input from user.
dimensions_x = list(map(int, input().split(",")))
dimensions_y = list(map(int, input().split(",")))

#Initialized volume of both the cuboid as One.
volume_of_x, volume_of_y = 1, 1

#Loop is run 3 times to multiply all the 3 dimesnions of the cuboid.
for i in range(3):
    volume_of_x = volume_of_x * dimensions_x[i]
    volume_of_y = volume_of_y * dimensions_y[i]
    
print("Difference in volume of cuboid is : ",volume_of_y - volume_of_x)