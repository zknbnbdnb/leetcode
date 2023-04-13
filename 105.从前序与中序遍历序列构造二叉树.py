#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        for idx, node in enumerate(inorder):
            if node == root.val:
                root.left = self.buildTree(
                    preorder[1: idx + 1], inorder[0: idx])
                root.right = self.buildTree(
                    preorder[idx + 1:], inorder[idx + 1:])
        return root

# @lc code=end
