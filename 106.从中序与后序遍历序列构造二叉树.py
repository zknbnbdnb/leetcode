#
# @lc app=leetcode.cn id=106 lang=python3
#
# [106] 从中序与后序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(postorder) == 0:
            return None
        root = TreeNode(postorder[-1])
        for idx, node in enumerate(inorder):
            if node == root.val:
                root.left = self.buildTree(
                    inorder[0: idx], postorder[0: idx])
                root.right = self.buildTree(
                    inorder[idx + 1:], postorder[idx: -1])
        return root

        # @lc code=end
