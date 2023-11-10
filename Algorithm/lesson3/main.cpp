#include <algorithm>
#include <iostream>
#include <iterator>
#include <vector>

void insertionSort(std::vector<int> &arr) {
  std::size_t n = arr.size();
  for (std::size_t i = 1; i < n; i++) {
    int key = arr[i];
    int j = i - 1;
    while (j >= 0 && arr[j] > key) {
      arr[j + 1] = arr[j];
      j--;
    }
    arr[j + 1] = key;
  }
}

int main() {
  std::size_t n;
  std::cout << "Enter the size of the array: ";
  std::cin >> n;

  std::vector<int> arr;
  arr.reserve(n);
  std::cout << "Enter the elements of the array: ";
  std::copy_n(std::istream_iterator<int>(std::cin), n, std::back_inserter(arr));

  insertionSort(arr);

  std::cout << "Sorted array: ";
  for (int num : arr) {
    std::cout << num << " ";
  }

  return 0;
}
