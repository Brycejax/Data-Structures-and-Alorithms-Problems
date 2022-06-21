# given an integer array nums, moce all 0's to the end of it while
# maintaining the relative order of the non zero elements
# example:
# input: nums = [0,1,0,3,12]
# output: [1,3,12,0,0]

# solution explaination -
# since we are putting all valid numbers at the beginning of the array,
# we can have a placeholder that starts at the beginning of the array
# we can initialize a swap sequence on a condition where the nums[i] != 0
# and then increment the placeholder after a swap is performed to fill the next
# available spot. We end up with all 'valid' values on the left and '0's on the right


class Solution:
    def moveZeros(self, nums):
        placeholder = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                temp = nums[placeholder]
                nums[placeholder] = nums[i]
                nums[i] = nums[temp]
                placeholder += 1