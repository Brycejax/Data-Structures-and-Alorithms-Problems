# Explaination - instead of looping through each arrays, causing the time complexity to become O(n^2),
# we can use a dictionary (hash map) to reduce the time complexity to O(n), (O(3n) to be exact


def matchingStrings(strings, queries):
    hash = {}
    values = []
    for i in queries:
        hash[i] = 0
    for i in strings:
        if i in hash:
            hash[i] = hash.get(i) + 1
    
    for i in queries:
        values.append(hash[i]) 
    
    return values