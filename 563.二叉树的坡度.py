# @before-stub-for-debug-begin
from python3problem563 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.res = []
        self.dfs(root)
        return sum(self.res)

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res.append(abs(left-right))
        return root.val + left + right
# @lc code=end
