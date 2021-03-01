l = [3,4,5,5,12,13,9,11,13,7,24,25] 

#Initialized an empty list.
output_list = []

for length in l:
    for breadth in l:
        for hypotaneous in l:
            #Pythagoras condition is checked.
            if(length**2 + breadth**2 == hypotaneous**2):
                #Tuples of length,breadth and hypotaneous are created
                x = length,breadth,hypotaneous,
                y = breadth,length,hypotaneous,

                #Conditional statement is applied so as to ignore appending of repetetive elements.
                if x not in output_list and y not in output_list:
                    output_list.append(x)
                    
print(output_list)