/*
 * @lc app=leetcode.cn id=2558 lang=golang
 *
 * [2558] 从数量最多的堆取走礼物
 */

import (
	"container/heap"
	"math"
)

type IntHeap []int

func (h IntHeap) Len() int {
	return len(h)
}
func (h IntHeap) Less(i, j int) bool {
	return h[i] > h[j]
}
func (h IntHeap) Swap(i, j int) {
	h[i], h[j] = h[j], h[i]
}
func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}
func (h *IntHeap) Pop() (v interface{}) {
	*h, v = (*h)[:h.Len()-1], (*h)[h.Len()-1]
	return
}

func pickGifts(gifts []int, k int) int64 {
	h := &IntHeap{}
	heap.Init(h)
	for i := 0; i < len(gifts); i++ {
		heap.Push(h, gifts[i])
	}

	for i := 0; i < k; i++ {
		t := heap.Pop(h)
		t = int(math.Sqrt(float64(t.(int))))
		heap.Push(h, t)
	}
	ans := int64(0)
	for i := 0; i < len(gifts); i++ {
		ans += int64(heap.Pop(h).(int))
	}

	return ans
}

// @lc code=end

