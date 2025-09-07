class Solution:
    def pattern21(self, n):
        if n==1:
            print("*")
        else:
            print("*"*n)
            spaces = n-2
            for _ in range(n-2):
                print("*"+" "*spaces+"*")
            print("*"*n)