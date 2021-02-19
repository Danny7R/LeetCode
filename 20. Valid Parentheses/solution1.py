from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        dic = {'(': ')', '[': ']', '{': '}'}
        stack = LifoQueue(maxsize = 1e4)
        while(len(s) > 0):
            if (s[0] in dic.keys()): stack.put(dic.get(s[0]))
            elif (stack.empty()): return False
            elif (s[0] != stack.get()): return False
            s.pop(0)

        return stack.empty()