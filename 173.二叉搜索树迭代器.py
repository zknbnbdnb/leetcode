# @before-stub-for-debug-begin
from python3problem173 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=173 lang=python3
#
# [173] 二叉搜索树迭代器
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.res = []
        self.dfs(root)
        self.length = len(self.res)

    def dfs(self, root):
        if not root:
            return None
        self.dfs(root.left)
        self.res.append(root.val)
        self.dfs(root.right)

    def next(self) -> int:
        temp = self.res.pop(0)
        self.length -= 1
        return temp

    def hasNext(self) -> bool:
        return not self.length == 0

        # Your BSTIterator object will be instantiated and called as such:
        # obj = BSTIterator(root)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()
        # @lc code=end
