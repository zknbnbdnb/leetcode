#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.temp = 0
        if not root:
            return None
        self.dfs(root)
        return root

    def dfs(self, root):
        if not root:
            return 0
        self.dfs(root.right)
        root.val += self.temp
        self.temp = root.val
        self.dfs(root.left)

# @lc code=end
