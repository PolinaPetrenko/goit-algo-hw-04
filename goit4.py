import timeit
import random

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    
    sizes = [1000, 10000, 100000]
    for size in sizes:
        arr = [random.randint(0, 1000) for _ in range(size)]
        
        
        merge_sort_time = timeit.timeit(stmt="merge_sort(arr)", setup=f"from __main__ import merge_sort; arr={arr}", number=1)
        print(f"Merge Sort Execution Time for {size} elements: {merge_sort_time}")

       
        insertion_sort_time = timeit.timeit(stmt="insertion_sort(arr)", setup=f"from __main__ import insertion_sort; arr={arr}", number=1)
        print(f"Insertion Sort Execution Time for {size} elements: {insertion_sort_time}")

        
        timsort_time = timeit.timeit(stmt="sorted(arr)", setup=f"arr={arr}", number=1)
        print(f"Timsort Execution Time for {size} elements: {timsort_time}")
        print()

if __name__ == "__main__":
    main()


