class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if (char in dic): stack.append(dic.get(char))
            elif (not stack): return False
            elif (char != stack.pop()): return False

        return not stack