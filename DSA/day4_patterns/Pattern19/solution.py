class Solution:
    def pattern19(self, n):
        spaces, left_stars, right_stars = -2, n+1, n+1
        for i in range(1, n+1):
            left_stars -= 1
            right_stars -= 1
            spaces += 2 
            print("*"*left_stars + " "*spaces + "*"*right_stars)
        spaces, left_stars, right_stars = 2*n, 0, 0
        for i in range(1, n+1):
            left_stars += 1
            right_stars += 1
            spaces -= 2 
            print("*"*left_stars + " "*spaces + "*"*right_stars)
        
# Driver code
if __name__ == "__main__":
    n = int(input())
    ob = Solution()
    ob.pattern19(n)