/*
 * @lc app=leetcode.cn id=1343 lang=golang
 *
 * [1343] 大小为 K 且平均值大于等于阈值的子数组数目
 */

// @lc code=start
func numOfSubarrays(arr []int, k int, threshold int) int {
	res, t := 0, 0
	l, k := 0, k
	for i := 0; i < k; i++ {
		t += arr[i]
	}
	for r <= len(arr) {
		if t >= k*threshold {
			res++
		}
		t -= arr[l]
		l++
		if r < len(arr) {
			t += arr[r]
		}
		r++
	}
	return res

}

// @lc code=end

