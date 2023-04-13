#
# @lc app=leetcode.cn id=449 lang=python3
#
# [449] 序列化和反序列化二叉搜索树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
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
                next_l.append(i.left) if i.left else next_l.append(None)
                next_l.append(i.right) if i.right else next_l.append(None)
            count = 0
            for i in next_l:
                if not i:
                    count += 1
            if count == len(next_l):
                break
            temp = next_l
        return '[' + ','.join(res) + ']'

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
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
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
# @lc code=end
