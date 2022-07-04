def plusMinus(arr):
    posCount, negCount, zeros = 0,0,0
    size = len(arr)
    for i in arr:
        if i == 0 : zeros += 1
        elif i > 0: posCount += 1
        else: negCount += 1
        
    print(round((posCount / size), 6))
    print(round((negCount / size), 6))
    print(round((zeros / size), 6))