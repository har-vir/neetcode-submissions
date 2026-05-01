class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_stack = []
        opening_chars = set(["{", "[", "("])
        closing_chars = {"}":"{", "]":"[", ")":"("}

        for char in s:
            if char in opening_chars:
                open_stack.append(char)
            if char in closing_chars:
                if open_stack and open_stack[-1] == closing_chars[char]:
                    open_stack.pop()
                else:
                    return False
        
        if open_stack:
            return False
        return True

