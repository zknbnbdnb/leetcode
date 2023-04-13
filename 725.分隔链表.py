#
# @lc app=leetcode.cn id=725 lang=python3
#
# [725] 分隔链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        p1 = head
        lenght = 0
        while p1:
            lenght += 1
            p1 = p1.next
        size = int(lenght / k)
        index = lenght % k
        p1 = head
        count = 1
        result_list = []
        while p1:
            if count == size + 1 and index:
                temp = p1.next
                p1.next = None
                result_list.append(head)
                head = temp
                p1 = temp
                count = 1
                index -= 1
                continue
            if count == size and not index:
                temp = p1.next
                p1.next = None
                result_list.append(head)
                head = temp
                p1 = temp
                count = 1
                continue
            p1 = p1.next
            count += 1
        i = k-len(result_list)
        if not p1 and len(result_list) < k:
            while i:
                result_list.append(None)
                i -= 1
        return result_list
        # @lc code=end
