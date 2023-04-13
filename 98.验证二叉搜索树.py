#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.isValidbst(root, -2**31-1, 2**31)

    def isValidbst(self, root, min, max):
        if not root:
            return True
        v = root.val
        return (v > min) and (v < max) and self.isValidbst(root.left, min, v) and self.isValidbst(root.right, v, max)

        # @lc code=end
