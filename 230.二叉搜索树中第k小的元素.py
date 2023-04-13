# @before-stub-for-debug-begin
from python3problem230 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=230 lang=python3
#
# [230] 二叉搜索树中第K小的元素
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        list = []
        list = self.inorder(root, list)
        return list[k-1]

    def inorder(self, root, list):
        if not root:
            return None
        self.inorder(root.left, list)
        list.append(root.val)
        self.inorder(root.right, list)
        return list
# @lc code=end
