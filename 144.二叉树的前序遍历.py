#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root, result):
            if root:
                result.append(root.val)
                helper(root.left, result)
                helper(root.right, result)
        result = []
        helper(root, result)
        return result
# @lc code=end
