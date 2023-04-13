#
# @lc app=leetcode.cn id=2225 lang=python3
#
# [2225] 找出输掉零场或一场比赛的玩家
#

# @lc code=start
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner = defaultdict(int)
        loser = defaultdict(int)
        for w_, l_ in matches:
            winner[w_] += 1
            loser[l_] += 1
        res_w, res_l = [], []
        for k, v in loser.items():
            if v == 1:
                res_l.append(k)
        for k, v in winner.items():
            if k not in loser:
                res_w.append(k)
        return [sorted(res_w), sorted(res_l)]
        


# @lc code=end

