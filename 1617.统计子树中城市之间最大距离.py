#
# @lc app=leetcode.cn id=1617 lang=python3
#
# [1617] 统计子树中城市之间最大距离
#
'''
给你 n 个城市，编号为从 1 到 n 。同时给你一个大小为 n-1 的数组 edges ，其中 edges[i] = [ui, vi] 表示城市 ui 和 vi 之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵 树 。

一棵 子树 是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。

对于 d 从 1 到 n-1 ，请你找到城市间 最大距离 恰好为 d 的所有子树数目。

请你返回一个大小为 n-1 的数组，其中第 d 个元素（下标从 1 开始）是城市间 最大距离 恰好等于 d 的子树数目。

请注意，两个城市间距离定义为它们之间需要经过的边的数目。

输入：n = 4, edges = [[1,2],[2,3],[2,4]]
输出：[3,4,0]
解释：
子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
不存在城市间最大距离为 3 的子树。

'''
from collections import defaultdict
from typing import List
# @lc code=start
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(u, d: int = 0):
            nonlocal mx, nxt, msk 
            '''
            mx 和 nxt 分别记录了当前最长直径长度和相应的下一个节点，msk 记录了子图中已经访问过的点。
            '''
            if mx < d:
                mx, nxt = d, u
            msk ^= 1 << u 
            '''
            用于将msk中二进制的第u位取反，并将取反后的结果存储回msk。这一操作的目的是为了记录子图中已经被访问过的点，
            其中 msk 的二进制表示中，每一位表示对应的点是否被访问，如果该位为1，表示该点已经被访问，
            '''
            for v in g[u]:
                if msk >> v & 1:
                    dfs(v, d + 1)
                    
        g = defaultdict(list)
        for u, v in edges:
            
            u, v = u - 1, v - 1
            g[u].append(v)
            g[v].append(u)
        ans = [0] * (n - 1)
        nxt, mx = 0, 0
        for mask in range(1, 1 << n):
            if mask & (mask - 1) == 0:
                continue
            msk, mx = mask, 0
            cur = msk.bit_length() - 1
            dfs(cur)
            if msk == 0:
                msk, mx = mask, 0
                dfs(nxt)
                ans[mx - 1] += 1
        return ans


n = 4
edges = [[1,2],[2,3],[2,4]]
print(Solution().countSubgraphsForEachDiameter(n, edges))
# @lc code=end

