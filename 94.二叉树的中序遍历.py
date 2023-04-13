# @before-stub-for-debug-begin
from python3problem94 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=94 lang=python3
#
# [94] 二叉树的中序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, result):
            if root:
                helper(root.left, result)
                result.append(root.val)
                helper(root.right, result)
        result = []
        helper(root, result)
        return result
        # @lc code=end
