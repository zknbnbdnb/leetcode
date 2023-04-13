# @before-stub-for-debug-begin
from python3problem95 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 1:
            return [TreeNode(n)]
        nums = [i for i in range(1, n+1)]
        return self.BTS(nums)

    def BTS(self, nums):
        if not nums:
            return [None]
        res = []
        for i in range(len(nums)):
            for left in self.BTS(nums[0: i]):
                for right in self.BTS(nums[i+1:]):
                    root = TreeNode(nums[i])
                    root.left = left
                    root.right = right
                    res.append(root)
        return res

        # @lc code=end
