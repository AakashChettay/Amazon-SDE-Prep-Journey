class Solution:
    def pattern16(self, n):
        for i in range(65, n+65):
            print(chr(i)*(i-64))

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    obj.pattern16(n)