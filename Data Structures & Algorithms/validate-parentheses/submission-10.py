class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        for c in s:
            if c in pairs:
                if not stack or pairs[c] != stack.pop():
                    return False
            else:
                stack.append(c)
        
        return not stack

                