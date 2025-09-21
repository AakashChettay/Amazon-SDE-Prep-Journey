class Solution:
    def rotateArray(self, nums, k):
        k = k % len(nums)
        temp = []
        for i in range(k):
            temp.append(nums[i])
        for i in range(k, len(nums)):
            nums[i-k] = nums[i]
        index = 0
        for i in range(len(nums)-k, len(nums)):
            nums[i] = temp[index]
            index += 1
        