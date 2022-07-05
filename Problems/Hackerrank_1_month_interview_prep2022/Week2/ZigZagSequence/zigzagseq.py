def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2) - 1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2  # this should be - 2 instead of -1, we already have the lowest on the right since we performed a swap
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 # this should decrement instead of increment

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)

