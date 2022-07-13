class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        
        while l <= r:
            mid = l + (r - l) // 2
            midpoint = nums[mid]
            
            if(midpoint == target):
                return mid
            elif(target < midpoint):
                r = mid - 1
            else:
                l = mid + 1
        return -1