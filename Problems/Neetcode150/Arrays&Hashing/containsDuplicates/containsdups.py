class Solution:
    def containsDuplicate(self, nums):
        hmap = {}
        for i in nums:
            if i in hmap:
                return True
            else:
                hmap[i] = True
        return False