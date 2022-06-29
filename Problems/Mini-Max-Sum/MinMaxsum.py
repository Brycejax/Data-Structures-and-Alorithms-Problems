# Explanation - we can achieve the highest 4 digits sum by simply subtracting the lowest value
# we can achieve the lowest 4 values sum by subtracting the highest value

def miniMaxSum(arr):
    print (sum(arr) - max(arr), sum(arr) - min(arr))