class Solution:
    def countOddDigit(self, n):
        num_arr = [int(x) for x in list(str(n))]
        return len([x for x in num_arr if x%2==1])

if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    print(obj.countOddDigit(n))