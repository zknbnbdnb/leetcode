#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.isSameTree(root.left, self.filpTree(root.right))

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val and self.isSameTree(
            p.left, q.left) and self.isSameTree(
                p.right, q.right):
            return True
        return False

    def filpTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.filpTree(root.left)
        self.filpTree(root.right)
        return root

    # @lc code=end
