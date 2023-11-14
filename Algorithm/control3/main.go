package main

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
)

func findMaxElement(tree []int) int {
	sort.Ints(tree)
	return tree[len(tree)-1]
}

func main() {
	var n int
	fmt.Scan(&n)

	var input string
	fmt.Scan(&input)

	treeStr := strings.Split(input, " ")
	tree := make([]int, n)
	for i := 0; i < n; i++ {
		tree[i], _ = strconv.Atoi(treeStr[i])
	}

	maxElement := findMaxElement(tree)
	fmt.Println(maxElement)
}
