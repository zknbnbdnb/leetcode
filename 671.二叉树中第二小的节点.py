# @before-stub-for-debug-begin
from python3problem671 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        res = []
        temp = [root]
        while temp:
            for i in temp:
                res.append(i.val)
            next_l = []
            for i in temp:
                if i.left:
                    next_l.append(i.left)
                if i.right:
                    next_l.append(i.right)
            temp = next_l
        res = list(set(res))
        res.sort()
        if len(res) == 1:
            return -1
        return res[1]
# @lc code=end
