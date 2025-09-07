class Solution:
    def pattern17(self, n):
        spaces = n
        for i in range(1, n+1):
            spaces -= 1
            print(" "*spaces,end="")
            for j in range(65, 65+i):
                print(chr(j),end="")
            for j in reversed(range(65, 65+i-1)):
                print(chr(j),end="")
            print()
                            