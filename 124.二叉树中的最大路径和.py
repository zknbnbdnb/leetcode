# @before-stub-for-debug-begin
from python3problem124 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum = -2**31
        self.dfs(root)
        return self.sum

    def dfs(self, root):
        if not root:
            return -2**31
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        temp = max(max(left + root.val, right + root.val), root.val)
        self.sum = max(max(left + right + root.val, temp), self.sum)
        return temp
# @lc code=end
