# @before-stub-for-debug-begin
from python3problem559 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=559 lang=python3
#
# [559] N 叉树的最大深度
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
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
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
        return len(res)


# @lc code=end
