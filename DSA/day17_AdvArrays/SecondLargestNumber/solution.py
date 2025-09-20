class Solution:
    def secondLargestElement(self, nums):
        fm, sm = -10**5, -10**5
        for i in range(len(nums)):
            if nums[i] > fm:
                sm = fm 
                fm = nums[i]
            elif nums[i] > sm and nums[i] < fm:
                sm = nums[i]
        if sm == -10**5:
            return -1
        else:
            return sm
        
