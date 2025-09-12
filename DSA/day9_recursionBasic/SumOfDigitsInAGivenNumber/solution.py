class Solution:
    def recursion(self, nums, n):
        if n == 0:
            return nums[0]
        return nums[n] + self.recursion(nums, n-1)
    def arraySum(self, nums):
        return self.recursion(nums, (len(nums)-1))

    def addDigits(self, num):
        if num == 0:
            return 0
        num_sum = num
        nums = []
        while num !=0:
            dig = num % 10
            nums.append(dig)
            num //=10
        while len(nums) > 1:
            num_sum = self.arraySum(nums)
            Innums = []
            while num_sum !=0:
                dig = num_sum % 10
                Innums.append(dig)
                num_sum //=10
            nums = Innums
            
        return sum(nums)