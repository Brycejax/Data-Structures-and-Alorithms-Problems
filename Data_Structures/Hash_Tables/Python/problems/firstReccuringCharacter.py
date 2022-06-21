# Given an array = [2,5,1,2,3,5,1,2,4]
# it should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]
# it should return 1

# Given an array = [2,3,4,5]
# it should return undefined

# Here is the brute force solution - this is bad as we are
# using two for loops so the time complexity would be O(n^2)
# we can achieve better time using a hash table, and trade off space for time
def firstRecCharNaive(arr):
    for i in range(1,len(arr)):
        for j in range(0,len(arr)-i):
            if arr[j] == arr[j+i]:
                return arr[i]
    return None


# Using a hashmap to bring down the big-o notation to O(n) but a space of O(n)
def firstRecChar(arr):
    hash = {}

    for i in arr:
        if i in hash:
            return i
        else:
            hash[i] = True
        
    return None


#testing
print("Testing the brute-force solution")
print(firstRecCharNaive([2,5,1,2,3,5,1,2,4]))
print(firstRecCharNaive([2,3,4,5]))
print(firstRecCharNaive([2,1,1,2,3,5,1,2,4]))

print("Testing the hash table function")
print(firstRecChar([2,5,1,2,3,5,1,2,4]))
print(firstRecChar([2,3,4,5]))
print(firstRecChar([2,1,1,2,3,5,1,2,4]))