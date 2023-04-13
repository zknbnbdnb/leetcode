#
# @lc app=leetcode.cn id=1096 lang=python3
#
# [1096] 花括号展开 II
#
import collections
from typing import List
# @lc code=start


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        # use a set to store the final result
        set_ = set()
        # use a queue to store the intermediate result
        deque = collections.deque()
        # push the whole expression to the queue
        deque.append(expression)
        # loop until the queue is empty
        while deque:
            # pop the first element out of the queue
            s = deque.popleft()
            # find the index of the first right brace
            right = s.find('}')
            # if there is no right brace, add the string to the set and skip the rest of the loop
            if right == -1:
                set_.add(s)
                continue
            # if there is a right brace, find the index of the first left brace
            left = right
            while s[left] != '{':
                left -= 1
                # if there is no left brace, add the string to the set and skip the rest of the loop
                if left == -1:
                    set_.add(s)
                    break
            # if the left brace is found
            if left != -1:
                # split the string into 3 parts
                s1 = s[:left]
                s2 = s[left + 1:right]
                s3 = s[right + 1:]
                # for each element in the second part, push the combination of the 3 parts to the queue
                for str in s2.split(','):
                    deque.append(s1 + str + s3)
        # return the sorted list of the set
        return sorted(set_)
# @lc code=end
