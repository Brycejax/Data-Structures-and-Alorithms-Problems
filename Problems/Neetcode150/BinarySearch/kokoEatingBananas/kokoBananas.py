import math
class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1 , max(piles)
        answer = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i / k)
            
            if hours <= h:
                answer = min(answer, k)
                r = k-1
            else:
                l = k+1
                
        return answer