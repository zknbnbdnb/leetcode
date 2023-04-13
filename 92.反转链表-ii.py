#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or not head.next or left == right:
            return head
        count = 0
        node = ListNode(0)
        node.next = head
        p1 = node
        while count < left-1:
            p1 = p1.next
            count += 1
        p2 = p1.next
        while (right - left):
            temp = p1.next
            p1.next = p2.next
            p2.next = p2.next.next
            p1.next.next = temp
            right -= 1
        return node.next
# @lc code=end
