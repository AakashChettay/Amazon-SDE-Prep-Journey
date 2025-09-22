class Solution:
    def findMaxConsecutiveOnes(self, nums):
        max_con_ones, temp_cnt = 0, 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp_cnt+=1 
            else:
                max_con_ones = max(temp_cnt, max_con_ones)
                temp_cnt = 0
        return max(max_con_ones, temp_cnt)