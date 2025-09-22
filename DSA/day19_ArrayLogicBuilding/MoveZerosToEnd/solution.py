class Solution:
    def moveZeroes(self, nums):
        zp = 0
        for i in range(len(nums)):
            if nums[zp] == 0:
                break
            zp += 1
        cp = zp + 1
        while cp < len(nums):
            if nums[cp] != 0:
                temp = nums[cp]
                nums[cp] = nums[zp]
                nums[zp] = temp
                zp+=1
                cp+=1
            else:
                cp += 1