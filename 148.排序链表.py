#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        lenght = 0
        p1 = head

        while p1:
            lenght += 1
            p1 = p1.next

        p2 = self.middlenode(head)
        temp = p2.next
        p2.next = None
        p2 = temp

        left = self.sortList(head)
        right = self.sortList(p2)

        return self.mergeTwoLists(left, right)

    def middlenode(self, head):
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
        return p1

    def mergeTwoLists(self, l1, l2):
        p = ListNode(1)
        cur = p
        while(l1 and l2):
            if(l1.val <= l2.val):
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 if l1 else l2
        return p.next

        # @lc code=end
