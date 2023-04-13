#
# @lc app=leetcode.cn id=108 lang=python3
#
# [108] 将有序数组转换为二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not len(nums):
            return None
        root = TreeNode(nums[int(len(nums) / 2)])
        root.left = self.sortedArrayToBST(nums[0: int(len(nums) / 2)])
        root.right = self.sortedArrayToBST(nums[int(len(nums) / 2) + 1:])
        return root
# @lc code=end
