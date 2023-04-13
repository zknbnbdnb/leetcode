# @before-stub-for-debug-begin
from python3problem112 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        list = []
        list = self.dfs(root, 0, list)
        if targetSum in list:
            return True
        return False

    def dfs(self, root, i, list):
        if not root:
            return 0
        i += root.val
        self.dfs(root.left, i, list)
        self.dfs(root.right, i, list)
        if not root.left:
            if not root.right:
                list.append(i)
        return list
# @lc code=end
