# @before-stub-for-debug-begin
from python3problem606 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ''
        res = self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return ''
        if not root.left and not root.right:
            res = str(root.val)
        elif not root.right:
            res = str(root.val) + '(' + str(self.dfs(root.left, res)) + ')'
        else:
            res = str(root.val) + '(' + str(self.dfs(root.left, res)) + \
                ')' + '(' + str(self.dfs(root.right, res)) + ')'
        return res
        # @lc code=end
