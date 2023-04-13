# @before-stub-for-debug-begin
from python3problem404 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = []
        res = self.dfs(root, res)
        return sum(res)

    def dfs(self, root, res):
        if not root:
            return None
        self.dfs(root.left, res)
        self.dfs(root.right, res)
        if root.left and not root.left.right and not root.left.left:
            res.append(root.left.val)
        return res
# @lc code=end
