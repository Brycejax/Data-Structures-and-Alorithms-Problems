class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hmap = {}
        hmap2 = {}
        if len(s) != len(t):
            return False
        
        for i in s:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
            
        for j in t:
            if not j in hmap:
                return False
            else:
                if j in hmap2:
                    hmap2[j] += 1
                else:
                    hmap2[j] = 1
                    
        return True if hmap == hmap2 else False