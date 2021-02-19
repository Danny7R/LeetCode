class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic2 = {")": "(", "}": "{", "]": "["}
        for char in s:
            if char in dic2:
                top_element = stack.pop() if stack else '#'
                if dic2[char] != top_element: return False
            else: stack.append(char)

        return not stack