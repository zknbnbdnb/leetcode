#
# @lc app=leetcode.cn id=147 lang=python3
#
# [147] 对链表进行插入排序
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = ListNode(0)
        node.next = None
        p1 = node
        p2 = head
        while p2:
            temp = p2.next
            while p1.next and p1.next.val < p2.val:
                p1 = p1.next
            p2.next = p1.next
            p1.next = p2
            p1 = node
            p2 = temp
        return node.next
# @lc code=end
