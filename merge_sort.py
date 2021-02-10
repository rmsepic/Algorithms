from typing import List

# Not a leetcode problem

def merge_sort(arr: List[int]):
	# Merge sort has two part
		# Divide
		# Conquer
			# Basically just skip to conquer. Sun Tsu

	curr = 1
	while curr < len(arr):
		left = 0	
		while left < len(arr) - 1:
			mid = min(left + curr, len(arr) - 1)
			right = min(left + 2 * curr, len(arr))
			merge(arr[left:mid], arr[mid:right], left)
			left = left + 2 * curr
			
		curr = curr * 2 # Exponential increase

def merge(left: List[int], right: List[int], index: int):
	i = 0
	j = 0
	print(left)
	print(right)
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			arr[index] = left[i]
			i += 1
		else:
			arr[index] = right[j]
			j += 1

		index += 1

	while i < len(left):
		arr[index] = left[i]
		i += 1
		index += 1

	while j < len(right):
		j += 1
		index += 1



if __name__ == "__main__":
	arr = [81,81,4,91,72,66,4,21]

	merge_sort(arr)
	print(arr)