# @before-stub-for-debug-begin
from python3problem429 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=429 lang=python3
#
# [429] N 叉树的层序遍历
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        temp = [root]
        while temp:
            res.append([i.val for i in temp])
            next_l = []
            for i in range(len(temp)):
                k = temp.pop(0)
                for j in k.children:
                    next_l.append(j)
            temp = next_l
        return res

        # @lc code=end
