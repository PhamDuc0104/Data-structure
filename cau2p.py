# Mảng tăng dần, tìm x = 12
arr = [1, 2, 4, 5, 6, 8, 12, 15]
x = 12

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"Kiểm tra phần tử giữa: arr[{mid}] = {arr[mid]}")

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

pos = binary_search(arr, x)
if pos == -1:
    print(f"Không tìm thấy {x} trong mảng.")
else:
    print(f"Tìm thấy {x} tại vị trí {pos}.")
