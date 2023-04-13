# @before-stub-for-debug-begin
from python3problem589 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
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
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        res = self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return None
        res.append(root.val)
        for i in root.children:
            self.dfs(i, res)
        return res
# @lc code=end
