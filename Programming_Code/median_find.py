
def find_median(start, mid, end):
    bmp = [unsorted_array[start], unsorted_array[mid], unsorted_array[end]]
    bmp.sort()
    A = bmp[1]
    pivot = unsorted_array.index(A)
    return pivot
