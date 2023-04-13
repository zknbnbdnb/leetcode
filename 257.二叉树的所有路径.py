# @before-stub-for-debug-begin
from python3problem257 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        temp = []
        res = []
        res = self.dfs(root, res, temp)
        return res

    def dfs(self, root, list, temp):
        if not root:
            return None
        temp.append(str(root.val))
        if not root.left:
            if not root.right:
                list.append('->'.join(temp))
        self.dfs(root.left, list, temp)
        self.dfs(root.right, list, temp)
        temp.pop()
        return list
# @lc code=end
