/*
 * @lc app=leetcode.cn id=1471 lang=golang
 *
 * [1471] 数组中的 k 个最强值
 */

// @lc code=start
func getStrongest(arr []int, k int) []int {
	sort.Ints(arr)
	n := len(arr)
	mid := arr[(n-1)/2]
	sort.Slice(arr, func(i, j int) bool {
		if abs(arr[i]-mid) == abs(arr[j]-mid) {
			return arr[i] > arr[j]
		}
		return abs(arr[i]-mid) > abs(arr[j]-mid)
	})
	return arr[:k]

}
func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// @lc code=end

