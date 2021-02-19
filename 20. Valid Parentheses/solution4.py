class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic2 = {")": "(", "}": "{", "]": "["}
        for char in s:
            if (char in dic2):
                if stack:
                    if (dic2[char] != stack.pop()): return False
                else: return False
            else: stack.append(char)

        return not stack