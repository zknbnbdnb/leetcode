# @before-stub-for-debug-begin
from python3problem450 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return self.dfs(root, key)

    def dfs(self, root, key):
        if not root:
            return None
        if root.val == key:

        self.dfs(root.left, key)
        self.dfs(root.right, key)
        return root

# @lc code=end
