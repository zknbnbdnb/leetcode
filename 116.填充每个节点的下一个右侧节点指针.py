# @before-stub-for-debug-begin
from python3problem116 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=116 lang=python3
#
# [116] 填充每个节点的下一个右侧节点指针
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        reslut = []
        temp = [root]
        while temp:
            reslut.append([i for i in temp])
            next_level = []
            for i in temp:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            temp = next_level
        for i in reslut:
            for idx in range(len(i)):
                if idx == len(i) - 1:
                    i[idx].next = None
                    break
                i[idx].next = i[idx + 1]
        return root
        # @lc code=end
