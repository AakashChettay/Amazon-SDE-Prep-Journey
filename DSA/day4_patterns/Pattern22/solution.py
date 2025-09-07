class Solution:
    def pattern22(self, n):
        if n == 1:
            print(1)
        else:
            mid_num_cnt = 2*n - 3 + 2
            for i in reversed(range(1, n+1)):
                mid_num_cnt -= 2
                for j in range(n, i-1, -1):
                    print(j, end=" ")
                print((str(i)+" ")*mid_num_cnt, end="")
                for j in reversed(range(n, i-1, -1)):
                    if j==1:
                        continue
                    print(j, end=" ")
                print()
            mid_num_cnt = -1
            for i in range(2, n+1):
                mid_num_cnt += 2
                for j in range(n, i-1, -1):
                    print(j, end=" ")
                print((str(i)+" ")*mid_num_cnt, end="")
                for j in reversed(range(n, i-1, -1)):
                    print(j, end=" ")
                print()
            
if __name__ == "__main__":
    n = int(input())
    obj = Solution()
    obj.pattern22(n)