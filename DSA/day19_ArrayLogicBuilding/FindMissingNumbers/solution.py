class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        tot = int(n*(n+1)/2)
        return tot - sum(nums)