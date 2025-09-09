class Solution:
    def GCD(self, n1, n2):
        small = min(n1, n2)
        for i in range(small, 0, -1):
            if n1%i==0 and n2%i==0:
                return i 
    def LCM(self, n1, n2):
        lcm = int(n1*n2/ self.GCD(n1, n2))
        return lcm