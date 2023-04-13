# @before-stub-for-debug-begin
from python3problem113 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        list = []
        temp = []
        i = 0
        res = []
        list = self.dfs(root, temp, list, i)
        for i in range(0, len(list), 2):
            if list[i] == targetSum:
                res.append(list[i+1])
        return res

    def dfs(self, root, temp, list, i):
        if not root:
            return 0
        i += root.val
        temp.append(root.val)
        if not root.left:
            if not root.right:
                list.append(i)
                list.append(temp.copy())
        self.dfs(root.left, temp, list, i)
        self.dfs(root.right, temp, list, i)
        temp.pop()
        return list
# @lc code=end
