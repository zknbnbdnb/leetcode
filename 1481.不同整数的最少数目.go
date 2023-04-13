/*
 * @lc app=leetcode.cn id=1481 lang=golang
 *
 * [1481] 不同整数的最少数目
 */

// @lc code=start
func findLeastNumOfUniqueInts(arr []int, k int) int {
	d := map[int]int{}
	for i := 0; i < len(arr); i++ {
		d[arr[i]]++
	}
	res := 0
	tmp := [][]int{}
	for k, v := range d {
		tmp = append(tmp, []int{k, v}) // 要将map转换为二维数组，才能使用sort.Slice
	}
	sort.Slice(tmp, func(i, j int) bool {
		return tmp[i][1] < tmp[j][1]
	})
	for i := 0; i < len(tmp); i++ {
		if k >= tmp[i][1] {
			k -= tmp[i][1]
		} else {
			res++
		}
	}
	return res

}

// @lc code=end

