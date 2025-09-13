class Solution:
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