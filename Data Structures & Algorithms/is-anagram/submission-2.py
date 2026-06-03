class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = [0] * 26

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            seen[ord(s[i]) - ord('a')] += 1
            seen[ord(t[i]) - ord('a')] -= 1
        
        if set(seen) == {0}:
            return True
        return False