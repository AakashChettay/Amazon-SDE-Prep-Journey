class Solution:
    def secondMostFrequentElement(self, nums):
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1   # cleaner counting

        freq1, freq2 = 0, 0
        mode1, mode2 = -1, -1

        for i in dic.keys():
            if dic[i] > freq1:
                freq2, mode2 = freq1, mode1
                freq1, mode1 = dic[i], i
            elif dic[i] == freq1:
                if i < mode1:
                    mode1 = i
            elif dic[i] > freq2:
                freq2, mode2 = dic[i], i  
            elif dic[i] == freq2 and (i < mode2):
                mode2 = i

        return mode2
