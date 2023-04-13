# @before-stub-for-debug-begin
from python3problem337 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=337 lang=python3
#
# [337] 打家劫舍 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        a, b = self.dfs(root)
        return max(a, b)

    def dfs(self, root):
        if not root:
            return 0, 0
        l0, l1 = self.dfs(root.left)
        r0, r1 = self.dfs(root.right)
        v1 = max(l0, l1) + max(r0, r1)
        v2 = root.val + l0 + r0
        return v1, v2


# @lc code=end
