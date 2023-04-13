#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root:
            m = self.minDepth(root.left) + 1
            n = self.minDepth(root.right) + 1
        if m == 1:
            return n
        if n == 1:
            return m
        return m if m < n else n
# @lc code=end
