#! /usr/bin/env Python3
# Implementation of Heap sort

def heapify(arr: list, heap_size: int, current_node_index: int):
    largest_node_index = current_node_index
    left_son_index = 2 * current_node_index + 1
    right_son_index = 2 * current_node_index + 2

    if left_son_index < heap_size and arr[left_son_index] > arr[current_node_index]:
        largest_node_index = left_son_index
    if right_son_index < heap_size and arr[right_son_index] > arr[largest_node_index]:
        largest_node_index = right_son_index
    if largest_node_index != current_node_index:
        arr[current_node_index], arr[largest_node_index] = arr[largest_node_index], arr[current_node_index]
        heapify(arr, heap_size, largest_node_index)


def heap_sort(arr):
    heap_size = len(arr)

    # Maximal Heap initialization
    for i in range(heap_size // 2 - 1, -1, -1):
        heapify(arr, heap_size, i)

    for i in range(heap_size - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


arr = [4, 10, 3, 5, 1]
print(arr)
heap_sort(arr)
print(arr)
