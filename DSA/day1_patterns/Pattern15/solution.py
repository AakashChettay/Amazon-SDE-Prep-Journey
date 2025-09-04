class Solution:
    def pattern15(self, n):
        for i in range(n, 0, -1):
            for j in range(65, i+65):
                print(chr(j), end = "")
            print()
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    obj.pattern15(n)