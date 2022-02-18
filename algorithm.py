# Алгоритм быстрой сортировки
def partition(start, end, array):
	pivot_index = start
	pivot = array[pivot_index]
	while start < end:
		while start < len(array) and array[start] <= pivot:
			start += 1
		while array[end] > pivot:
			end -= 1
		if(start < end):
			array[start], array[end] = array[end], array[start]
	array[end], array[pivot_index] = array[pivot_index], array[end]
	return end
def quick_sort(start, end, array):
	if (start < end):
		p = partition(start, end, array)
		quick_sort(start, p - 1, array)
		quick_sort(p + 1, end, array)

# Алгоритм бинарного поиска

def binary_search(left, right, array, X):
	if (array != array.sorted()):
		quick_sort(0, len(list) - 1, list)
	while (left < right):
		middle = (left + right) / 2
		if (array[middle] < X):
			left = middle
		elif (array[middle] > X):
			right = middle
		else:
			return middle + 1
	return -1