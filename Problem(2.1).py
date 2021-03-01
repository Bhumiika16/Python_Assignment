from operator import itemgetter

num_of_people = int(input("Enter total number of people : "))
mylist = []

#Took the details of people in the form of a dictionary and appended all of the details in the list.
for i in range(num_of_people):
    dic = {}
    dic["name"] = input()
    dic["age"] = int(input())
    dic["score"] = int(input())
    mylist.append(dic)

#List is sorted using itemgetter where name, age and score are given priority respectively.    
result = sorted(mylist, key=itemgetter('name','age','score'))

#Print one by one elements in the list in ascending order.
for value in result:
    print(tuple(value.values()),end=" ")