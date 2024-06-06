# binary search using for loop
# a=[1,5,7,8,9,12,14]
# key=14
# start,end=0,len(a)-1
# found=False
# for i in range (len(a)):
#     start<=end
#     mid=(start+end)//2
#     if a[mid]==key:
#         print(f"the key {key} is at index {mid}")
#         found=True
#         break
#     elif a[mid]<key:
#         start=mid+1
#     else:
#         end=mid-1

# if not found:
#     print(f"the key {key} is not found in the array")

#  binary search using while loop
# arr=arr=[int(x) for x in input("Enter the list of numbers seperated by spaces: ").split()]
# target=int(input("Enter the target to search: "))
# start,end=0,len(arr)-1
# found=False
# while start<=end:
#     mid = (start+end)//2
#     if arr[mid]==target:
#         print(f"Target {target} found at index {mid}.")
#         found=True
#         break
#     elif arr[mid]<target:
#         start=mid+1
#     else:
#         end=mid-1

# if not found:
#     print(f"Target {target} not found in the array.")

# to find the first and last index no of a number in an array
# def first_occ(arr, n, key):
#     s, e = 0, n - 1
#     ans = -1
#     while s <= e:
#         mid = s + (e - s) // 2
#         if arr[mid] == key:
#             ans = mid
#             e = mid - 1
#         elif key > arr[mid]:
#             s = mid + 1
#         else:
#             e = mid - 1
#     return ans

# def last_occ(arr, n, key):
#     s, e = 0, n - 1
#     ans = -1
#     while s <= e:
#         mid = s + (e - s) // 2
#         if arr[mid] == key:
#             ans = mid
#             s = mid + 1
#         elif key > arr[mid]:
#             s = mid + 1
#         else:
#             e = mid - 1
#     return ans

# def first_and_last_position(arr, k):
#     n = len(arr)
#     first = first_occ(arr, n, k)
#     last = last_occ(arr, n, k)
#     return (first, last)

# # Example usage
# arr = [1, 2, 2, 3, 3, 3, 4, 5, 5]
# k = 3
# result = first_and_last_position(arr, k)
# print(f"First and last position of {k}: {result}")

# program for authentication password.
# def authentication():
#     password="Sash123"
#     attempts=3

#     while attempts>0:
#         user_input=input("Enter the password:")

#         if user_input==password:
#             print("welcome!")
#             break
#         else:
#             attempts-=1
#             if attempts>0:
#                 print(f"wrong password! you have {attempts} attempts left.")
#             else:
#                 print("Account Blocked.")
#                 break
# authentication()