class Solution:
    def twoSum(self, nums, target):
        hmap = {}
        
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in hmap:
                return i, hmap.get(target - nums[i])
            else:
                hmap[nums[i]] = i
        