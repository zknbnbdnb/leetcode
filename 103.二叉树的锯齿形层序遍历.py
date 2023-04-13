#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        temp_res = [root]
        res = []
        count = 1
        while temp_res:
            if count % 2:
                res.append([i.val for i in temp_res])
            else:
                temp_res.reverse()
                res.append([i.val for i in temp_res])
                temp_res.reverse()
            next_level = []
            for i in temp_res:
                if i.left:
                    next_level.append(i.left)
                if i.right:
                    next_level.append(i.right)
            count += 1
            temp_res = next_level
        return res
# @lc code=end
