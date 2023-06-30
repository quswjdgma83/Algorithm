import random
import math
import time

#글로벌 변수 선언
comp = 0
unsorted_array = []

def compare(x,y):
    global comp
    comp += 1
    if unsorted_array[x] > unsorted_array[y]:
        return 1
    else:
        return 0

def compare2():
    global comp
    comp += 1

# Comparison 리셋
def comp_reset():
    global comp
    comp = 0

# Random array 생성

def create_random_list(n, filename):
    #파일을 쓰기 모드로 엽니다.
    with open(f"{filename}.txt","w") as file:
        # Random Array 생성
        for i in range(n):
            a = random.randint(1,99)
            file.write(f"{a}\n")
    return filename

# Random array File open 함수
def open_file(name):
    with open(f"{name}.txt", "r") as file:
        lines = file.readlines()
        lines = [line.rstrip('\n') for line in lines]
        unsorted_array = list(map(int, lines))
    return unsorted_array

#랜덤 리스트 생성 및 파일이름 정의
name = create_random_list(32 , "unsorted_array")
unsorted_array = open_file(name)

# 정렬된 array 파일로 저장하는 함수
def save_sorted_list(unsorted_array, sorted_array, comparison, time_ns, filename):
    with open(f"{filename}.txt","w") as file:
        file.write(f"unsorted array : {unsorted_array}\nsort결과 : {sorted_array}\nsort comparison 횟수 : {comparison} \nsort에 걸린 시간 : {time_ns} nano_sec\n")
        
#  @@@@@@@@@@@@@@@@@@@@@삽입정렬@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
unsorted_array = open_file(name)

def insertion_sort(unsorted_array):
    start_time = time.perf_counter_ns() #clock시작
    for end in range(1, len(unsorted_array)):
        for i in range(end, 0, -1):
            if compare((i-1), i):
                unsorted_array[i - 1], unsorted_array[i] = unsorted_array[i], unsorted_array[i - 1]
    end_time = time.perf_counter_ns() #clock 끝
    elapsed_time = end_time - start_time
    return unsorted_array, comp, elapsed_time

# Unsorted_array 출력 
print(f"unsorted_array : {unsorted_array}\n")

sorted, comparison, time_ns = insertion_sort(unsorted_array)

unsorted_array = open_file(name) #초기화

print(f"insertion_sort결과 : {sorted}")
print(f"insertion_sort comparison 횟수 : {comparison}")
print(f"insertion_sort에 걸린 시간 : {time_ns} nano_sec\n")
save_sorted_list(unsorted_array, sorted, comparison, time_ns, "Insertion_sort(n=32)_result")
comp_reset()

#@@@@@@@@@@@@@@@@@@@@@@@@@@@ 힙 정렬 @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def heapify(unsorted_array, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2
    global comp
    comp += 1

    if left < heap_size and compare(left, largest):
        largest = left

    if right < heap_size and compare(right, largest):
        largest = right
    
    if largest != index: #compare(largest, index):
        unsorted_array[largest], unsorted_array[index] = unsorted_array[index], unsorted_array[largest]
        heapify(unsorted_array, largest, heap_size)

def heap_sort(unsorted_array):
    n = len(unsorted_array)
    start_time = time.perf_counter_ns() #clock시작
    for i in range(n//2 - 1, -1, -1):
        heapify(unsorted_array, i, n)

    for i in range(n - 1, 0, -1):
        unsorted_array[0], unsorted_array[i] = unsorted_array[i], unsorted_array[0]
        heapify(unsorted_array, 0, i)
    end_time = time.perf_counter_ns() #clock 끝
    elapsed_time = end_time - start_time

    return unsorted_array, comp, elapsed_time

sorted, comparison, time_ns = heap_sort(unsorted_array)

unsorted_array = open_file(name) #초기화

print(f"heap_sort결과 : {sorted}")
print(f"heap_sort comparison 횟수 : {comparison}")
print(f"heap_sort에 걸린 시간 : {time_ns} nano_sec\n")
save_sorted_list(unsorted_array, sorted, comparison, time_ns, "Heap_sort(n=32)_result")
comp_reset()

# @@@@@@@@@@@@ Merge Sort @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def merge_sort(unsorted_array):
    def sort(start, end):
        start_time = time.perf_counter_ns() #clock시작
        if end - start < 2:
            return
        mid = (start + end) // 2
        sort(start, mid)
        sort(mid, end)
        merge(start, mid, end)
        end_time = time.perf_counter_ns() #clock 끝
        elapsed_time = end_time - start_time
        return elapsed_time

    def merge(start, mid, end):
        temp = []
        l, h = start, mid

        while l < mid and h < end:
            if compare(h, l):
            #if unsorted_array[l] < unsorted_array[h]:
                temp.append(unsorted_array[l])
                l += 1
            else:
                compare(l, h)
                temp.append(unsorted_array[h])
                h += 1
        while l < mid:
            temp.append(unsorted_array[l])
            l += 1
        while h < end:
            temp.append(unsorted_array[h])
            h += 1
        for i in range(start, end):
            unsorted_array[i] = temp[i - start]
        return comp
    
    return unsorted_array, merge(0,len(unsorted_array)//2, len(unsorted_array)), sort(0, len(unsorted_array))
    #return unsorted_array, comp, sort(0, len(unsorted_array))
sorted, comparison, time_ns = merge_sort(unsorted_array)

unsorted_array = open_file(name) #초기화

print(f"Merge_sort결과 : {sorted}")
print(f"Merge_sort comparison 횟수 : {comparison}")
print(f"Merge_sort에 걸린 시간 : {time_ns} nano_sec\n")
save_sorted_list(unsorted_array, sorted, comparison, time_ns, "Merge_sort(n=32)_result")
comp_reset()

################################# Quick Sort1 ##################################################

def find_median(unsorted_array):
    start = 0
    end = len(unsorted_array)-1
    mid = len(unsorted_array)//2

    bmp = [unsorted_array[start], unsorted_array[mid], unsorted_array[end]]
    bmp.sort()
    A = bmp[1]
    return A

def quick_sort1(unsorted_array):
    def sort(start, end):
        start_time = time.perf_counter_ns() #clock시작
        if end <= start:
            return
        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)
        end_time = time.perf_counter_ns() #clock 끝
        elapsed_time = end_time - start_time
        return elapsed_time

    def partition(start, end):
        pivot = unsorted_array[(start + end) // 2]
 
        while start <= end:
            #while compare(pivot ,start):
            while compare((start + end) // 2,start):
            #while unsorted_array[start] < pivot:
                start += 1
            #while compare(end, pivot):
            while compare(end, (start + end) // 2):
            #while unsorted_array[end] > pivot:
                end -= 1
            if start <= end:
                unsorted_array[start], unsorted_array[end] = unsorted_array[end], unsorted_array[start]
                start, end = start + 1, end - 1
        return start

    return unsorted_array, sort(0, len(unsorted_array)-1), comp

sorted, time_ns, comp = quick_sort1(unsorted_array)
unsorted_array = open_file(name) #초기화

print(f"quick_sort3결과 : {sorted}")
print(f"quick_sort3 comparison 횟수 : {comp}")
print(f"quick_sort3에 걸린 시간 : {time_ns} nano_sec\n")
save_sorted_list(unsorted_array, sorted, comparison, time_ns, "Quick_sort1(n=32)_result")
comp_reset()

####################################### Quick sort2(pivot = random)######################

def quick_sort2(unsorted_array):
    def sort(start, end):
        start_time = time.perf_counter_ns() #clock시작
        if end <= start:
            return
        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)
        end_time = time.perf_counter_ns() #clock 끝
        elapsed_time = end_time - start_time
        return elapsed_time

    def partition(start, end):
        pivot = random.randint(start, end)

        while start <= end:
            while compare(pivot, start):
                start += 1
            while compare(end, pivot):
                end -= 1
            if start <= end:
                unsorted_array[start], unsorted_array[end] = unsorted_array[end], unsorted_array[start]
                start, end = start + 1, end - 1
        return start

    return unsorted_array, sort(0, len(unsorted_array)-1), comp

sorted, time_ns, comp = quick_sort2(unsorted_array)
unsorted_array = open_file(name) #초기화

print(f"quick_sort2결과 : {sorted}")
print(f"quick_sort2 comparison 횟수 : {comp}")
print(f"quick_sort2에 걸린 시간 : {time_ns} nano_sec\n")
save_sorted_list(unsorted_array, sorted, comparison, time_ns, "Quick_sort2(n=32)_result")
comp_reset()

####################################### Quick sort3(pivot = median)#######################################################

def find_median(start, mid, end):
    bmp = [unsorted_array[start], unsorted_array[mid], unsorted_array[end]]
    bmp.sort()
    A = bmp[1]
    pivot = unsorted_array.index(A)
    return pivot

def quick_sort3(unsorted_array):
    def sort(start, end):
        start_time = time.perf_counter_ns() #clock시작
        if end <= start:
            return
        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)
        end_time = time.perf_counter_ns() #clock 끝
        elapsed_time = end_time - start_time
        return elapsed_time

    def partition(start, end):
        mid = end//2
        pivot = find_median(start, mid, end)

        while start <= end:
            while compare(pivot, start):
                start += 1
            while compare(end, pivot):
                end -= 1
            if start <= end:
                unsorted_array[start], unsorted_array[end] = unsorted_array[end], unsorted_array[start]
                start, end = start + 1, end - 1
        return start

    return unsorted_array, sort(0, len(unsorted_array)-1), comp

sorted, time_ns, comp = quick_sort3(unsorted_array)
unsorted_array = open_file(name) #초기화

print(f"quick_sort3결과 : {sorted}")
print(f"quick_sort3 comparison 횟수 : {comp}")
print(f"quick_sort3에 걸린 시간 : {time_ns} nano_sec\n")
save_sorted_list(unsorted_array, sorted, comparison, time_ns, "Quick_sort3(n=32)_result")
comp_reset()

####################################### Quick sort4(pivot = my strategy)#######################################################

def find_median(start, A, mid, B, end):
    bmp = [unsorted_array[start], A, unsorted_array[mid], B, unsorted_array[end]]
    bmp.sort()
    A = bmp[2]
    pivot = unsorted_array.index(A)
    return pivot

def quick_sort4(unsorted_array):
    def sort(start, end):
        start_time = time.perf_counter_ns() #clock시작
        if end <= start:
            return
        mid = partition(start, end)
        sort(start, mid - 1)
        sort(mid, end)
        end_time = time.perf_counter_ns() #clock 끝
        elapsed_time = end_time - start_time
        return elapsed_time

    def partition(start, end):
        mid = end//2
        A = unsorted_array[random.randint(start, end)]
        B = unsorted_array[random.randint(start, end)]
        pivot = find_median(start, A, mid, B, end)

        while start <= end:
            while compare(pivot, start):
                start += 1
            while compare(end, pivot):
                end -= 1
            if start <= end:
                unsorted_array[start], unsorted_array[end] = unsorted_array[end], unsorted_array[start]
                start, end = start + 1, end - 1
        return start

    return unsorted_array, sort(0, len(unsorted_array)-1), comp

sorted, time_ns, comp = quick_sort4(unsorted_array)
unsorted_array = open_file(name) #초기화

print(f"quick_sort4결과 : {sorted}")
print(f"quick_sort4 comparison 횟수 : {comp}")
print(f"quick_sort4에 걸린 시간 : {time_ns} nano_sec\n")
save_sorted_list(unsorted_array, sorted, comparison, time_ns, "Quick_sort4(n=32)_result")