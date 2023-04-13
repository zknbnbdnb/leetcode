# @before-stub-for-debug-begin
from python3problem199 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        list = []
        res = []
        temp = [root]
        while temp:
            res.append([i.val for i in temp])
            next_level = []
            for i in temp:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            temp = next_level
        for i in res:
            list.append(i[-1])
        return list
# @lc code=end
