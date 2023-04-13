#
# @lc app=leetcode.cn id=2058 lang=python3
#
# [2058] 找出临界点之间的最小和最大距离
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next
        if length < 3:
            return [-1, -1]
        node = head
        t = []
        i = 0
        while node and node.next and node.next.next:
            if node.val > node.next.val and node.next.val < node.next.next.val:
                t.append(i + 1)
            if node.val < node.next.val and node.next.val > node.next.next.val:
                t.append(i + 1)
            node = node.next
            i += 1
        if len(t) < 2:
            return [-1, -1]
        return [min(t[i + 1] - t[i] for i in range(len(t) - 1)), t[-1] - t[0]]


            
# @lc code=end

