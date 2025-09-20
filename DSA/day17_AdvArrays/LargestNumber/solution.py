class Solution:
    def largestElement(self, nums):
        max_ele = -10**5
        for i in range(len(nums)):
            if nums[i] > max_ele:
                max_ele = nums[i]
        return max_ele