/*
 * @lc app=leetcode.cn id=2570 lang=golang
 *
 * [2570] 合并两个二维数组 - 求和法
 */

// @lc code=start
func mergeArrays(nums1 [][]int, nums2 [][]int) [][]int {
	d_1, d_2 := map[int]int{}, map[int]int{}
	for i := 0; i < len(nums1); i++ {
		d_1[nums1[i][0]] = nums1[i][1]
	}
	for i := 0; i < len(nums2); i++ {
		d_2[nums2[i][0]] = nums2[i][1]
	}
	for k, v := range d_1 {
		if _, ok := d_2[k]; ok {
			d_2[k] += v
		} else {
			d_2[k] = v
		}
	}
	res := [][]int{}
	for k, v := range d_2 {
		res = append(res, []int{k, v})
	}
	sort.Slice(res, func(i, j int) bool {
		return res[i][0] < res[j][0]
	})
	return res

}

// @lc code=end

