import algorithm

l = [9, 1, 2, 11, -55]
#-55 1 2 9 11
algorithm.quick_sort(0, len(l) - 1, l)
k = algorithm.binary_search(0, len(l) - 1, l, 18);
print(k)
print(l)
