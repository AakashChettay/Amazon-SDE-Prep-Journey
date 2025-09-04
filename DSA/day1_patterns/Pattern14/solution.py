class Solution:
    def pattern14(self, n):
        for i in range(1, n+1):
            for j in range(65, i+65):
                print(chr(j), end = "")
            print()

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    obj.pattern14(n)