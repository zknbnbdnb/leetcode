#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        p1 = head
        del_list = []
        while p1.next:
            if p1.val == p1.next.val:
                if p1.val not in del_list:
                    del_list.append(p1.val)
                p1.next = p1.next.next
            else:
                p1 = p1.next
        p2 = head
        p3 = head
        count = 0
        while p3:
            count += 1
            p3 = p3.next
        if count == len(del_list):
            return None
        while p2.next:
            if p2.val in del_list:
                head = head.next
                p2.next = None
                p2 = head
                continue
            if p2.next.val in del_list:
                p2.next = p2.next.next
                continue
            else:
                p2 = p2.next
        return head

        # if head == None or head.next == None:
        #     return head
        # node = ListNode(0)
        # node.next = head
        # head = node
        # flag = False
        # p1, p2 = head.next, head.next.next
        # while p1 and p2:
        #     if p1.val != p2.val and flag:
        #         head.next = head.next.next
        #         p1, p2 = head.next, head.next.next
        #         flag = False
        #         continue
        #     if p1.val == p2.val:
        #         head.next = head.next.next
        #         p1, p2 = head.next, head.next.next
        #         flag = True
        #     else:
        #         head = head.next
        #         p1, p2 = head.next, head.next.next
        #         flag = False
        # if head.next and flag:
        #     head.next = None
        # return node.next
        # @lc code=end
