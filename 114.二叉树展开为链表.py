# @before-stub-for-debug-begin
from python3problem114 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        list = []
        list = self.dfs(root, list)
        p = root
        for i in range(1, len(list)):
            p.right = list[i]
            p.left = None
            p = p.right
        return

    def dfs(self, root, list):
        if not root:
            return None
        list.append(root)
        self.dfs(root.left, list)
        self.dfs(root.right, list)
        return list
# @lc code=end
