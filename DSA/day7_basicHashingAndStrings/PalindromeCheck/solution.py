class Solution:    
    def reverseString(self, s):
        left = 0
        right = len(s)-1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1
        
    def palindromeCheck(self, s):
        stored = s
        #Reversing 
        s = list(s)
        self.reverseString(s)
        return stored == "".join(s)