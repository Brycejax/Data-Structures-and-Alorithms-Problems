# in python slice the string into known sections, determine if the last string AM/PM and then either add 12 or leave it

def timeConversion(s):
    first_section = int(s[:2])
    last_section = s[-2:]
    newString = ""
    
    if last_section == "PM":
        first_section += 12
        newString += str(first_section) + s[2:-2]
    elif last_section == "AM" and first_section == 12:
        first_section = "00"
        newString += str(first_section) + s[2:-2]
    else:
        newString = s[:-2]
        
    return newString