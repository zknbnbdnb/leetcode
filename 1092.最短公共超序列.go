/*
 * @lc app=leetcode.cn id=1092 lang=golang
 *
 * [1092] 最短公共超序列
 */

// @lc code=start
func shortestCommonSupersequence(str1 string, str2 string) string {
	n, m := len(str1), len(str2)
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, m)
	}

	var dfs func(i, j int) int
	dfs = func(i, j int) int {
		if i < 0 {
			return j + 1
		}
		if j < 0 {
			return i + 1
		}
		p := &memo[i][j]
		if *p > 0 {
			return *p
		}
		if str1[i] == str2[j] {
			*p = dfs(i-1, j-1) + 1
		} else {
			*p = min(dfs(i-1, j), dfs(i, j-1)) + 1
		}
		return *p
	}

	var makeAns func(i, j int) string
	makeAns = func(i, j int) string {
		if i < 0 {
			return str2[:j+1]
		}
		if j < 0 {
			return str1[:i+1]
		}
		if str1[i] == str2[j] {
			return makeAns(i-1, j-1) + string(str1[i])
		}
		if dfs(i, j) == dfs(i-1, j)+1 {
			return makeAns(i-1, j) + string(str1[i])
		}
		return makeAns(i, j-1) + string(str2[j])
	}

	dfs(n-1, m-1)
	return makeAns(n-1, m-1)
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end
