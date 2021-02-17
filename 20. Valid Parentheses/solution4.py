class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            if (char in mapping):
                if stack:
                    if (mapping[char] != stack.pop()): return False
                else: return False
            else: stack.append(char)

        return not stack