class Solution:
    def pattern12(self, n):
        spaces = 2*n
        for i in range(1, n+1):
            spaces -= 2
            for j in range(1, i+1):
                print(j, end="")
            print(" "*spaces,)
            for j in reversed(range(1, i+1)):
                print(j, end="")
            print()

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    obj.pattern12(n)