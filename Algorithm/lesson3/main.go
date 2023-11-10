package main

import (
	"fmt"
	"strconv"
	"strings"
)

func insertionSort(arr []int) {
	n := len(arr)
	for i := 1; i < n; i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
}

func main() {
	var input string
	fmt.Print("Enter the elements of the array (separated by spaces): ")
	fmt.Scanln(&input)

	strArr := strings.Split(input, " ")
	arr := make([]int, len(strArr))

	for i, str := range strArr {
		num, err := strconv.Atoi(str)
		if err != nil {
			fmt.Println("Invalid input:", str)
			return
		}
		arr[i] = num
	}

	insertionSort(arr)

	fmt.Println("Sorted array:", arr)
}
