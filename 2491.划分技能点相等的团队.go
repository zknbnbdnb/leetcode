/*
 * @lc app=leetcode.cn id=2491 lang=golang
 *
 * [2491] 划分技能点相等的团队
 */

// @lc code=start
func dividePlayers(skill []int) int64 {
	s, n := 0, len(skill)
	if n == 2 {
		return int64(skill[0]) * int64(skill[1])
	}
	for _, v := range skill {
		s += v
	}
	sort.Ints(skill)
	if s%(n/2) == 0 {
		l, r := 0, n-1
		res := int64(0)
		for l < r {
			if skill[l]+skill[r] != s/(n/2) {
				return -1
			}
			res += int64(skill[l]) * int64(skill[r])
			l++
			r--
			return res
		}
	}
	return -1
}

// @lc code=end

