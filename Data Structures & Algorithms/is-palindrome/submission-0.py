class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatted_str = [c.lower() for c in s if c.isalnum()]
        left,right = 0,len(formatted_str)-1

        while left < right:
            if formatted_str[left] != formatted_str[right]:
                return False
            left += 1
            right -= 1
        
        return True