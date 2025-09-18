class Solution:  
    def longestCommonPrefix(self, st):
        st.sort()
        first = st[0]
        last = st[len(st)-1]
        ans_str = ""
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                break
            ans_str += first[i]
        return ans_str   