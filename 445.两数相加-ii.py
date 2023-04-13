#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        t_node = node
        t_list1 = []
        t_list2 = []
        p1 = l1
        p2 = l2
        a = 0
        b = 0
        while l1:
            a += 1
            l1 = l1.next
        while l2:
            b += 1
            l2 = l2.next
        if a >= b:
            while p1:
                t_list1.append(str(p1.val))
                p1 = p1.next
            while (a - b):
                t_list2.append(str(0))
                a -= 1
            while p2:
                t_list2.append(str(p2.val))
                p2 = p2.next
        else:
            while p2:
                t_list2.append(str(p2.val))
                p2 = p2.next
            while (b - a):
                t_list1.append(str(0))
                b -= 1
            while p1:
                t_list1.append(str(p1.val))
                p1 = p1.next
        t_str1 = ''.join(t_list1)
        t_str2 = ''.join(t_list2)
        temp = str(int(t_str1) + int(t_str2))
        result = list(temp)
        for i in result:
            p = ListNode(0)
            p.val = int(i)
            node.next = p
            node = node.next
        return t_node.next
# @lc code=end
