# from libs import qsort
from libs.qsort.qsort_tester import test_small_arr
from libs.trees.bin_tree_viz import insert, visualize_binary_tree

# arr = [2, 8, 7, 1, 3, 5, 6, 4]
# q = QuickSort(arr)
# q.qsort(0, len(arr) - 1)
# q.print()

# arr = [1, 1, 1, 1, 1, 1, 1, 1]
# q = QuickSort(arr)
# q.qsort(0, len(arr) - 1)
# q.print()

test_small_arr()

# Example usage:
# root = None
# keys = [5, 3, 7, 2, 4, 6, 8]
# for key in keys:
#     root = insert(root, key)
#
# visualize_binary_tree(root)
