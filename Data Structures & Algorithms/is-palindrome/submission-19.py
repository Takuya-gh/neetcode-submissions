class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s) - 1
        while left < right: # check if = is needed
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left + 1, right - 1
        return True
        
"""
string -> boolean
compare left and right -> Broute force (T: O(n), S: O(1)) or Two pointers (T: O(n), S: O(1))
-> reverse is inefficient (T: O(n), S: O(n)) -> adopt TP this time
space should be removed.
each char should be turned into lower case.
"""