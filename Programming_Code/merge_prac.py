import sys

unsorted_array = [27, 99, 52, 49, 29, 82, 67, 26]
tmp = []
def merge_sort(start, end):
    if end - start < 1: return
    mid = int(start + (end - start)/2)
    merge_sort(start, mid)
    merge_sort(mid+1, end)
    for i in range(end):
        tmp.append(unsorted_array[i])
    k = start
    index1 = start
    index2 = mid+1
    while index1 <= mid and index2 <= (end-1):#두 그룹을 병합하는 로직
        if tmp[index1] > tmp[index2]:
            unsorted_array[k] = tmp[index2]
            k += 1
            index2 += 1
        else:
            unsorted_array[k] = tmp[index2]
            k += 1
            index1 += 1
    while index1 <= mid:
        unsorted_array[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= (end-1):
        unsorted_array[k] = tmp[index2]
        k += 1
        index2 += 1
    return unsorted_array

A = merge_sort(0, len(unsorted_array))
print(A)