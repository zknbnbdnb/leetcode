# @before-stub-for-debug-begin
from python3problem543 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.result = 0
        self.dfs(root)
        return self.result

    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.result = max(self.result, left+right)
        return max(left, right) + 1
# @lc code=end
