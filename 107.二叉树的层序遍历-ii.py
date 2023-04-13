#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层序遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        temp_res = [root]
        res = []
        while temp_res:
            res.append([i.val for i in temp_res])
            next_level = []
            for i in temp_res:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            temp_res = next_level
        res.reverse()
        return res
# @lc code=end
