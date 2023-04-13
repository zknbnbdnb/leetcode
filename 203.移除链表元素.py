#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        node = ListNode(0)
        node.next = head
        p = node
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return node.next
# @lc code=end
