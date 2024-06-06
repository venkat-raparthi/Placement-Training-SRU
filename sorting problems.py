# BUBBLE SORT
# def bubble_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         for j in range(0,n-i-1):
#             if arr[j]>arr[j+1]:
#                 arr[j],arr[j+1]=arr[j+1],arr[j]
# my_list=list(map(int,input().split()))
# print("Original List:",my_list)
# bubble_sort(my_list)
# print("Sorted List:",my_list)
# # comparing first two elements of the list and swapping that 2 Nbers and comparing the next 2 elements

# SELECTION SORT
# def selection_sort(arr):
#     n=len(arr)
#     for i in range(n):
#         min_index=i
#         for j in range(i+1,n):
#             if arr[j]<arr[min_index]:
#                 min_index=j
#         N,arr[min_index]=arr[min_index],N
                
# my_list=list(map(int,input().split()))
# print("Original List:",my_list)
# selection_sort(my_list)
# print("Sorted List:",my_list)

# def insertion_sort(arr):
#     n=len(arr)
#     for i in range(1,n):
#         key=N
#         j=i-1
#         while j>>0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key

# my_list=list(map(int,input().split()))
# print("Original List:",my_list)
# insertion_sort(my_list)
# print("Sorted List:",my_list)

# time complexity = O(N log N)
def merge_sort(arr):
    if len(arr) > 1:
        # Divide the array into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(arr, left_half, right_half)


def merge(arr, left, right):
    i = j = k = 0

    # Compare and merge the elements from left and right halves
    while i < len(left) > j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

        # If there are any remaining elements in left or right halves, add them to the merged array
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", my_list)
merge_sort(my_list)
print("Sorted List:", my_list)