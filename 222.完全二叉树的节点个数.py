# @before-stub-for-debug-begin
from python3problem222 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        res_list = []
        temp = [root]
        while temp:
            res_list.append([i.val for i in temp])
            next_level = []
            for i in temp:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            temp = next_level
        for i in res_list:
            res += len(i)
        return res
# @lc code=end
