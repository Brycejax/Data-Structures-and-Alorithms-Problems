# non-dynamic programming fibbonacci sequence

def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

#print(fib(40))

# fibonacci using memoization - non imported help

def fibm():
    cache = {}
    def insideFib(n):
        if n in cache:
            return cache[n]
        else:
            if n < 2:
                return n
            else:
                cache[n] = insideFib(n-1) + insideFib(n-2)
                return cache[n]
    return insideFib

# fibvar = fibm()
# print(fibvar(100))

#fibonacci using bottom-up approach

def fibBottomUp(n):
    answer = [0, 1]
    for i in range(2,n,1):
        answer.append(answer[i-2] + answer[i-1])
    return answer[-1]



print(fibBottomUp(100))