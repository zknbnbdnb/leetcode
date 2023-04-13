# @before-stub-for-debug-begin
import collections
from python3problem297 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=297 lang=python3
#
# [297] 二叉树的序列化与反序列化
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = []
        temp = [root]
        while temp:
            for i in temp:
                res.append(str(i.val)) if i else res.append('None')
            next_l = []
            for i in temp:
                if not i:
                    continue
                next_l.append(i.left if i.left else None)
                next_l.append(i.right if i.right else None)
            count = 0
            for i in next_l:
                if not i:
                    count += 1
            if count == len(next_l):
                break
            temp = next_l
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        data = data[1:-1].split(',')
        idx = 1
        root = TreeNode(int(data[0]))
        queue = collections.deque([root])
        while queue:
            if idx == len(data):
                break
            node = queue.popleft()
            if data[idx] != 'None':
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
            idx += 1
            if data[idx] != 'None':
                node.right = TreeNode(int(data[idx]))
                queue.append(node.right)
            idx += 1
        return root
        # Your Codec object will be instantiated and called as such:
        # ser = Codec()
        # deser = Codec()
        # ans = deser.deserialize(ser.serialize(root))
        # @lc code=end
