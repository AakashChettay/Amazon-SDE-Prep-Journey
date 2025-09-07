class Solution:
    def pattern20(self, n):
        if n==1:
            print("**")
        else:
            spaces, stars_cnt  = 2*n-2, 1
            for _ in range(n):
                print("*"*stars_cnt + " "*spaces + "*"*stars_cnt)
                spaces -= 2
                stars_cnt += 1
            spaces, stars_cnt  = 2, n-1
            for _ in range(n-1): 
                print("*"*stars_cnt + " "*spaces + "*"*stars_cnt)
                spaces += 2
                stars_cnt -= 1
            
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    obj.pattern20(n)