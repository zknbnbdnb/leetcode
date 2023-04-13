#
# @lc app=leetcode.cn id=1282 lang=python3
#
# [1282] 用户分组
#

# @lc code=start
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        for idx, val in enumerate(groupSizes):
            d[val].append(idx)
        res = []
        for k, v in d.items():
            for i in range(0, len(v), k):
                res.append(v[i: i + k])
        return res
# @lc code=end

