def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:  # originally, this was if(s[i] = t[i]) <-- = instead of ==
            res += '0'    # this had a semicolan and was not +=
        else:
            res += '1'    # this had a semicolan and was not +=

    return res

s = input()
t = input()
print(strings_xor(s, t))
