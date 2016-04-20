# Bubble Sort

target_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

def bubble_sort(lst):
	for item in range(len(lst) - 1, 0, -1):
		for i in range(item):
			if lst[i] > lst[i + 1]:
				temp = lst[i]
				lst[i] = lst[i + 1]
				lst[i + 1] = temp
	print(lst)

bubble_sort(target_list)