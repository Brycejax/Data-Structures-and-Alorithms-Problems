#Given an integer array nums, find the contigious subarray (containing at least one number)
#  which has the largest sum and return its sum

#input: [-2,1,-3,4,-1,2,1,-5,5]
#output: -6
#explaination: [4,-1,2,1] has the largest sum = 6

class Solution:
    def maxSubArray(self, nums):
        currentSum = nums[0]
        currentMax = nums[0]

        for i in range(1, len(nums)):
            currentSum = max(nums[i], nums[i] + currentSum)
            currentMax = max(currentSum, currentMax)

        return currentMax

