#
# @lc app=leetcode.cn id=2558 lang=python3
#
# [2558] 从数量最多的堆取走礼物
#

# @lc code=start
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            a = heapq.heappop(gifts)
            a = int(sqrt(-a))
            heapq.heappush(gifts, -a)
        return -sum(gifts)
# @lc code=end

