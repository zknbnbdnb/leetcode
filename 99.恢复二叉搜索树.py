# @before-stub-for-debug-begin
from python3problem99 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=99 lang=python3
#
# [99] 恢复二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = []
        x = y = None
        temp = self.dfs(root, temp)
        p = temp[0]
        for i in range(1, len(temp)):
            if p.val > temp[i].val:
                y = temp[i]
                if not x:
                    x = p
            p = temp[i]
        if x and y:
            x.val, y.val = y.val, x.val

    def dfs(self, root, list):
        if not root:
            return None
        self.dfs(root.left, list)
        list.append(root)
        self.dfs(root.right, list)
        return list
# @lc code=end
