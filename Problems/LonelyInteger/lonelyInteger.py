# Explaination - Once again, we are using a hash map to bring down our overall time complexity to O(n), but a tradeoff of
# space complexity to O(n) as well

def lonelyinteger(a):
    map = {}
    for i in a:
        if i in map:
            map[i] = map.get(i) + 1
        else:
            map[i] = 1
    
    for key, value in map.items():
        if value == 1:
            return key