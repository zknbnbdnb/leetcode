/*
 * @lc app=leetcode.cn id=1590 lang=golang
 *
 * [1590] 使数组和能被 P 整除
 */

// @lc code=start
func minSubarray(nums []int, p int) int {
	n := len(nums)
	pre := make([]int, n+1)
	for i := 0; i < n; i++ {
		pre[i+1] = (pre[i] + nums[i])
	}
	x := pre[n] % p
	if x == 0 {
		return 0
	}
	ans := n
	hashmap := make(map[int]int)
	for i := 0; i < n; i++ {
		y := pre[i+1] % p
		hashmap[y] = i + 1
		z := (y - x + p) % p         // 为什么要加p，因为可能出现负数
		if j, ok := hashmap[z]; ok { // go的语法糖，如果j存在，ok为true
			ans = min(ans, i+1-j)
		}
	}
	if ans < n {
		return ans
	}
	return -1
}
func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

// @lc code=end

