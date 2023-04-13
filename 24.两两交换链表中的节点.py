#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        p = cur = head
        if (p and p.next):
            cur = p.next
            p.next = cur.next
            cur.next = p
            head = cur
            while (p.next and p.next.next):
                cur = p.next.next
                p.next.next = cur.next
                cur.next = p.next
                p.next = cur
                p = cur.next
        return head
# @lc code=end
