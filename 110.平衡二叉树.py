# @before-stub-for-debug-begin
from python3problem110 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        m, n = self.height(root.left), self.height(root.right)
        return abs(m - n) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(
                root.right)

    def height(self, root):
        if not root:
            return 0
        return max(self.height(root.left), self.height(root.right)) + 1


# @lc code=end
