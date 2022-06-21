#Create a function to reverse a string
#My name is Bryce
#should convert to
#ecyrB si eman yM

def reverseString(string):
    if string is not None and len(string) >= 2: 
        return string[::-1]
    elif string is None or len(string) == 0:
        return "Enter a valid string."
    else:
        return string
        

print(reverseString())