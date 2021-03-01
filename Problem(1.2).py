class SwapCase:
    
    #Constructor
    def __init__(self):
        pass

    #Method will get console input from the user and store the value as self.string.    
    def get_string(self):
        string = input()
        self.string = string

    #Method will return the output in uppercase.
    def print_string(self):
        for i in self.string:
            #The ord function will convert the string into it's ascii value, thus allowing only a-z and A-Z letters to be passed and will ignore digits.
            if(ord(i) >= 97 and ord(i) <= 122 or ord(i) >= 65 and ord(i) <= 90):
                print(i.upper(),end="")
            else:
                pass

#Creating an object.
result = SwapCase()
#Passing the string to the method.
result.get_string()
#Getting the desired output.
result.print_string()