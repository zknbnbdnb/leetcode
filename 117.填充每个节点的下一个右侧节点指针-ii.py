#
# @lc app=leetcode.cn id=117 lang=python3
#
# [117] 填充每个节点的下一个右侧节点指针 II
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
        result = []
        temp_result = [root]
        while temp_result:
            result.append([i for i in temp_result])
            next_level = []
            for i in temp_result:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            temp_result = next_level
        for i in result:
            for idx in range(len(i)):
                if idx == len(i) - 1:
                    i[idx].next = None
                    break
                i[idx].next = i[idx+1]
        return root
# @lc code=end
