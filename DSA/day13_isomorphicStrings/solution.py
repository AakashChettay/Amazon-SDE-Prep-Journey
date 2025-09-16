class Solution:
    def isomorphicString(self, s, t):
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        m = {}
        for i in range(len(s)):
            if s[i] not in m.keys():
                m[s[i]] = t[i]
            elif s[i] in m.keys():
                if m[s[i]] != t[i]:
                    return False 
        return True