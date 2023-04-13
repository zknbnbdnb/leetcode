# @before-stub-for-debug-begin
from python3problem129 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=129 lang=python3
#
# [129] 求根节点到叶节点数字之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        temp = []
        res = []
        res = self.dfs(root, temp, res)
        return sum(res)

    def dfs(self, root, temp, list):
        if not root:
            return None
        temp.append(str(root.val))
        if not root.left:
            if not root.right:
                list.append(int(''.join(temp)))
        self.dfs(root.left, temp, list)
        self.dfs(root.right, temp, list)
        temp.pop()
        return list
# @lc code=end
