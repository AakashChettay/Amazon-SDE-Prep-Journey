class Solution:  
    def largeOddNum(self, s):
        s = s.strip("0")
        if not s:
            return ""
        if int(s[len(s)-1])%2==1:
            return s 
        for i in range(len(s)-1, -1, -1):
            if int(s[i])%2==1:
                return s[:i+1]
        return ""