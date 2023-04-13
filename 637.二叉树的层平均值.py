#
# @lc app=leetcode.cn id=637 lang=python3
#
# [637] 二叉树的层平均值
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        res = []
        temp = [root]
        while temp:
            res.append([i.val for i in temp])
            next_l = []
            for i in temp:
                if i.left:
                    next_l.append(i.left)
                if i.right:
                    next_l.append(i.right)
            temp = next_l
        fin = []
        for i in res:
            fin.append(sum(i) / len(i))
        return fin
# @lc code=end
