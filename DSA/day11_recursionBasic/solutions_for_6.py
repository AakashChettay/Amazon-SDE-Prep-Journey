class Solution:
    #1
    def recursion(self, s, left, right):
        if left > right:
            return s 
        temp = s[left]
        s[left] = s[right]
        s[right] = temp 
        return self.recursion(s, left + 1, right - 1)
    def reverseString(self,s):
        reverseStringList = self.recursion(list(s), 0, len(s)-1)
        return reverseStringList
    
    #2
    def recursion(self, s, left, right):
        if left > right:
            return s 
        temp = s[left]
        s[left] = s[right]
        s[right] = temp 
        return self.recursion(s, left + 1, right - 1)
    def reverseString(self,s):
        reverseStringList = self.recursion(list(s), 0, len(s)-1)
        return reverseStringList    
    def palindromeCheck(self, s):
        store = s 
        reverseStringList = self.reverseString(s)
        return s == "".join(reverseStringList)  
    
    #3
    def prime(self, num, x):
        if x > num**0.5:
            return True
        if num % x == 0:
            return False
        return self.prime(num, x+1)
    def checkPrime(self, num):
        if num <= 1:
            return False
        return self.prime(num, 2)
    
    #4
    def recursion(self,nums, l, r):
        if l > r:
            return nums 
        temp = nums[l]
        nums[l] = nums[r]
        nums[r] = temp
        return self.recursion(nums, l+1, r-1)
    def reverseArray(self, nums):
        return self.recursion(nums, 0, len(nums)-1)
    
    #5
    def recursion(self, nums, f, s):
        if f == len(nums)-2:
            return nums[f] <= nums[s]
        if nums[f] > nums[s]:
            return False
        return self.recursion(nums, f+1, s+1)
    def isSorted(self, nums):
        if len(nums) == 1:
            return True
        return self.recursion(nums, 0, 1)