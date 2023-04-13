/*
 * @lc app=leetcode.cn id=1381 lang=golang
 *
 * [1381] 设计一个支持增量操作的栈
 */

// @lc code=start
type CustomStack struct {
	Stack   []int
	MaxSize int
}

func Constructor(maxSize int) CustomStack {
	return CustomStack{
		Stack:   make([]int, 0, maxSize),
		MaxSize: 0,
	}

}

func (this *CustomStack) Push(x int) {
	if this.MaxSize < cap(this.Stack) {
		this.Stack = append(this.Stack, x)
		this.MaxSize++
	}

}

func (this *CustomStack) Pop() int {
	if this.MaxSize == 0 {
		return -1
	}
	fmt.Println(this.Stack)
	top := this.Stack[this.MaxSize-1]
	this.Stack = this.Stack[:this.MaxSize-1]
	this.MaxSize--
	return top

}

func (this *CustomStack) Increment(k int, val int) {
	if k > this.MaxSize {
		k = this.MaxSize
	}
	for i := 0; i < k; i++ {
		this.Stack[i] += val
	}

}

/**
 * Your CustomStack object will be instantiated and called as such:
 * obj := Constructor(maxSize);
 * obj.Push(x);
 * param_2 := obj.Pop();
 * obj.Increment(k,val);
 */
// @lc code=end

