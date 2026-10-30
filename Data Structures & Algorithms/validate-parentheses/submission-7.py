class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []
        pairs ={
            ')':'(',
            '}':'{',
            ']':'['
        }
        for c in s:
            if c in pairs:
                if not stack or stack.pop() != pairs[c]:
                    return False
            else:
                stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
             return False