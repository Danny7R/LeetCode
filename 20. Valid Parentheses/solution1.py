from queue import LifoQueue

class Solution:
    def isValid(self, s: str) -> bool:
        s = list(s)
        dict = {'(': ')', '[': ']', '{': '}'}
        stack = LifoQueue(maxsize = 1e4)
        while(len(s) > 0):
            if (s[0] in dict.keys()): stack.put(dict.get(s[0]))
            elif (stack.empty()): return False
            elif (s[0] != stack.get()): return False
            s.pop(0)

        return stack.empty()