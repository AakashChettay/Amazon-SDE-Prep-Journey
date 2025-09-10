class Solution:
    def mostFrequentElement(self, nums):
        dic = {}
        for i in nums:
            if i not in dic.keys():
                dic[i] = 1
            else:
                dic[i] += 1
        mode = -1
        large = -1
        for i in dic.keys():
            if dic[i] > large:
                large = dic[i]
                mode = i 
            elif dic[i] == large:
                large = dic[i]
                mode = min(mode, i)
        return mode