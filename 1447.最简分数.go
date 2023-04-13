/*
 * @lc app=leetcode.cn id=1447 lang=golang
 *
 * [1447] 最简分数
 */

// @lc code=start
func simplifiedFractions(n int) []string {
	ans := []string{}
	for i := 2; i <= n; i++ {
		for j := 1; j < i; j++ {
			if gcd(i, j) == 1 {
				ans = append(ans, fmt.Sprintf("%d/%d", j, i))
			}
		}
	}
	return ans

}
func gcd(a, b int) int {
	if b == 0 {
		return a
	}
	return gcd(b, a%b)
}

// @lc code=end

