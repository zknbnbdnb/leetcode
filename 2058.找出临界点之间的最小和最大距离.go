/*
 * @lc app=leetcode.cn id=2058 lang=golang
 *
 * [2058] 找出临界点之间的最小和最大距离
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func nodesBetweenCriticalPoints(head *ListNode) []int {
	length := 0
	for p := head; p != nil; p = p.Next {
		length++
	}
	if length < 3 {
		return []int{-1, -1}
	}
	t := []int{}
	i := 0
	for p := head; p != nil && p.Next != nil && p.Next.Next != nil; p = p.Next; i++ {
		if (p.Val < p.Next.Val && p.Next.Val > p.Next.Next.Val) || (p.Val > p.Next.Val && p.Next.Val < p.Next.Next.Val) {
			t = append(t, i)
		}
	}
	if len(t) < 2 {
		return []int{-1, -1}
	}
	min_d, max_d := 1e6, t[len(t)-1]-t[0]
	for i := 0; i < len(t)-1; i++ {
		if t[i+1]-t[i] < min_d {
			min_d = t[i+1] - t[i]
		}
	}
	return []int{min_d, max_d}

}
// @lc code=end

