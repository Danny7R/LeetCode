# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root return 0
        level = [root]
        depth = 0
        while level:
            depth += 1
            nextlevel = []
            for node in level:
                if node.left: nextlevel.append(node.left)
                if node.right: nextlevel.append(node.right)
            level = nextlevel
        return depth