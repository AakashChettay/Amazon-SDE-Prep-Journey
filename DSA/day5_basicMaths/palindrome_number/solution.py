class Solution:
    def isPalindrome(self, n):
        stored = n
        rev = 0
        while n != 0:
            dig = n%10
            rev = rev * 10 + dig
            n = n // 10
        return rev == stored  
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.isPalindrome(n))