#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
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
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        res = self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if not root:
            return None
        for i in root.children:
            self.dfs(i, res)
        res.append(root.val)
        return res


# @lc code=end
