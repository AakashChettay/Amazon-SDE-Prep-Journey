class Solution:
    def sumHighestAndLowestFrequency(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1

        bigEle = 0
        smallEle = 0
        large = -1
        small = 10**5
        for i in dic.keys():
            if dic.get(i) > large:
                large = dic.get(i)
                bigEle = i 
                
            elif dic.get(i) == large:
                large = dic.get(i)
                bigEle = min(bigEle, i)
        for i in dic.keys():
            if dic.get(i) < small:
                small = dic.get(i)
                smallEle = i 
                
            elif dic.get(i) == small:
                smallEle = max(smallEle, i)
        
        return large + small