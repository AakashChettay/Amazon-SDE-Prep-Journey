class Solution:
    def anagramStrings(self, s, t):
        # If lengths are not equal, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Sort both strings and compare
        return sorted(s) == sorted(t)
