/*
 * @lc app=leetcode.cn id=1338 lang=golang
 *
 * [1338] 数组大小减半
 */

// @lc code=start
func minSetSize(arr []int) int {
	m := Counter(arr)
	pairs := make(Pairs, 0, len(m))
	for k, v := range m {
		pairs = append(pairs, Pair{k, v})
	}
	sort.Sort(pairs)
	n := len(arr)
	ans := 0
	for i := 0; i < len(pairs); i++ {
		ans++
		n -= pairs[i].Value
		if n <= len(arr)/2 {
			break
		}
	}
	return ans

}
func Counter(arr []int) map[int]int {
	m := make(map[int]int)
	for _, v := range arr {
		m[v]++
	}
	return m
}

type Pair struct {
	Key   int
	Value int
}

type Pairs []Pair

func (p Pairs) Len() int           { return len(p) }
func (p Pairs) Less(i, j int) bool { return p[i].Value > p[j].Value }
func (p Pairs) Swap(i, j int)      { p[i], p[j] = p[j], p[i] }

// @lc code=end

