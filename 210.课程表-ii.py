# @before-stub-for-debug-begin
from python3problem210 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#

# @lc code=start


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # in_list = [0 for i in range(numCourses)]
        # res_list = []
        # temp = [[] for i in range(numCourses)]
        # for i in prerequisites:
        #     in_list[i[0]] += 1
        #     temp[i[1]].append(i[0])
        # for i in range(len(in_list)):
        #     if in_list[i] == 0:
        #         res_list.append(i)
        # i = 0
        # while i != len(res_list):
        #     c = res_list[i]
        #     v = temp[c]
        #     for j in v:
        #         in_list[j] -= 1
        #         if in_list[j] == 0:
        #             res_list.append(j)
        #     i += 1
        # if len(res_list) == numCourses:
        #     return res_list
        # return []

        import collections
        edges = collections.defaultdict(list)
        entry = collections.defaultdict(int)
        for a, b in prerequisites:
            edges[b].append(a)
            entry[b] += 0
            entry[a] += 1
        res = []
        out_res = []
        for node in range(numCourses):
            if node not in entry:
                out_res.append(node)
        stack = []
        for v, i in entry.items():
            if i == 0:
                stack.append(v)
        while stack:
            temp = stack.pop()
            res.append(temp)
            for j in edges[temp]:
                entry[j] -= 1
                if entry[j] == 0:
                    stack.append(j)
        res += out_res
        return res if len(res) == numCourses else []
        # @lc code=end
