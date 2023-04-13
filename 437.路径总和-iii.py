# @before-stub-for-debug-begin
from python3problem437 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        res = self.findPath(root, targetSum)
        res += self.pathSum(root.left, targetSum)
        res += self.pathSum(root.right, targetSum)
        return res

    def findPath(self, root, targetSum):
        if not root:
            return 0
        res = 0
        if targetSum == root.val:
            res += 1
        res += self.findPath(root.left, targetSum - root.val)
        res += self.findPath(root.right, targetSum - root.val)
        return res
        # @lc code=end
