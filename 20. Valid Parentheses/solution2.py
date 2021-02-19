class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = []
        while(len(s) > 0):
            if (s[0] in dic.keys()): stack.append(dic.get(s[0]))
            elif (not stack): return False
            elif (s[0] != stack.pop()): return False
            s.pop(0)

        return not stack