#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 1:
            return head
        node = head
        i = k
        while i:
            if not node:
                return head
            node = node.next
            i -= 1
        result = self.reverse(head, node)
        head.next = self.reverseKGroup(node, k)
        return result

    def reverse(self, p1, p2):
        pre = p2
        while p1 != p2:
            temp = p1.next
            p1.next = pre
            pre = p1
            p1 = temp
        return pre
# @lc code=end
