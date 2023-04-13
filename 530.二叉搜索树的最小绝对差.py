#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.res = []
        self.dfs(root)
        fin = []
        for i in range(len(self.res) - 1):
            fin.append(self.res[i + 1] - self.res[i])
        return min(fin)

    def dfs(self, root):
        if not root:
            return None
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)
        # @lc code=end
