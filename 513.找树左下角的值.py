#
# @lc app=leetcode.cn id=513 lang=python3
#
# [513] 找树左下角的值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        res = []
        tem = [root]
        while tem:
            res.append([i.val for i in tem])
            next_l = []
            for i in tem:
                if i.left:
                    next_l.append(i.left)
                if i.right:
                    next_l.append(i.right)
            tem = next_l
        return res[-1][0]
# @lc code=end
