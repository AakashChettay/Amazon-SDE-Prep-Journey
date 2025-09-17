class Solution:    
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        if s == goal:
            return True
        for _ in range(len(s)):
            goal = goal[1:] + goal[0]
            if s == goal:
                return True 
        return False