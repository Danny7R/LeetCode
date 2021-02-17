# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        count = 0
        while(head is not None):
            count += 1
            if (count > 1e4):
                return True
            head = head.next
        return False