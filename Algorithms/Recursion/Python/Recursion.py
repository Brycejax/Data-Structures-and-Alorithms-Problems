# Write a function that returns the factorial of any number using an iteractive approach
# Non-recursive

def findFactorialIterative(num):
    answer = 1
    if num > 1:
        for i in range(1,num+1):
            answer *= i
        return answer
    else:
        return None

#print(findFactorialIterative(5))



# With recursion
def findFactorialRecursively(num):
    if num == 1:
        return
    else:
        return num * findFactorialRecursively(num - 1)

#print(findFactorialIterative(5))


# Given A number N, return the index value of the Fibonacci sequence, where the sequence
# is 0,1,1,2,3,5,8,13,21,34,55,89,144
# the pattern of the sequence is that each value is the sum of the 2 previous values. that means
# for N  = 5 -> 2+3

def fibIterative(num):
    num1 = 0
    num2 = 1
    answer = 0
    if num == 0:
        return 0
    elif num == 1:
        return 1

    for i in range(num-1):    
        answer = num1 + num2
        num1 = num2
        num2 = answer
    return answer


#print(fibIterative(7))

def fibRecursive(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibRecursive(num-1) + fibRecursive(num-2)

#print(fibRecursive(7))

# exercise, reverse a string with recursion

def reverseStringIterative(string):
    text = ""
    for i in range(len(string)-1,-1,-1):
        text += string[i]
    return text

#print(reverseStringIterative("This is a test"))

def reverseStringRecursive(string):
    if string == "":
        return string
    else:
        return reverseStringRecursive(string[1:]) + string[0]

print(reverseStringIterative("This is a test"))