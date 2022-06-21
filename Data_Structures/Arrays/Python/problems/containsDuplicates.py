# Given an integer Array nums, return true if the array contains a duplicate
# and false if it does not

# Example
# input: nums = [1,2,3,1]
# output: true - because there are two 1's

# Example 2
# input: nums = [1,2,3,4]
# output: false - because there are no duplicates


#Answer one
class Solution:

    # Solution 1 - Brute Force
    # Explaination - We loop over each index i and compare it again to each index j.
    # In this approach, we utilize two for loops to keep track of i and j (nums[i], nums[j])
    # this however, is bad since as the problem scales we achieve O(n^2) time complexity, 
    # but space complexity remains O(1)
    # ON LEETCODE  - WE EXPERIENCE A TIME LIMIT EXCEEDED
    def containsDuplicatesBruteForce(self, nums):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    # Solution 2 - HashMap (this is likely what I would pick in an interview)
    # Explaination - We use the DS hashtable to keep track of what is entered and what is not
    # this solution is O(n) time complexity and O(n) space complexity since access to a hashmap is O(1) 
    def containsDuplicatesHashMap(self, nums):
        hash = {}
        for i in nums:
            if i in hash:
                return True
            else:
                hash[i] = i

        return False
