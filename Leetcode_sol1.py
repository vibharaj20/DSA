"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true 
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setArray = set()
        for i in nums:
        # checks if the element is already present in the set, if yes returns true 
            if i in setArray:
                return True
        # if the element is not present then it gets added into the set
            else:
                setArray.add(i)

        return False