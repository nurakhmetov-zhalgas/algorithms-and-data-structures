# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

from math import inf


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes_rec(self, root: TreeNode) -> int:
        def helper(root: TreeNode, maxinpath: int):
            if not root:
                return 0
            is_current_good = 1 if root.val >= maxinpath else 0
            return (
                helper(root.left, max(root.val, maxinpath))
                + helper(root.right, max(root.val, maxinpath))
                + is_current_good
            )

        return helper(root, -inf)

    def goodNodes_iter(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, -inf)]
        counter = 0
        while stack:
            node, maxinpath = stack.pop()
            if node.val >= maxinpath:
                counter += 1
                maxinpath = node.val
            if node.left:
                stack.append((node.left, maxinpath))
            if node.right:
                stack.append((node.right, maxinpath))
        return counter
