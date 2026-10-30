class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            while l < r and not s[l].isalnum():
                l += 1
                print("l", l)
            while l < r and not s[r].isalnum():
                r -= 1
                print("r", r)
            if s[l].lower() != s[r].lower():
                print(s[l], s[r])
                return False
            else:
                l += 1
                r -= 1
        return True
