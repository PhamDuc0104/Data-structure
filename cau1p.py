
arr = [4, 6, 10, 15, 21, 25, 30, 36, 50]
x = 35

def binary_search(arr, x):
    left = 0                    
    right = len(arr) - 1        

    while left <= right:        
        mid = (left + right) // 2
        print(f"Kiểm tra phần tử giữa: arr[{mid}] = {arr[mid]}")

        if arr[mid] == x:       # nếu đúng thì trả về vị trí
            return mid
        elif arr[mid] < x:      # nếu phần tử giữa nhỏ hơn x → tìm nửa phải
            left = mid + 1
        else:                   # nếu phần tử giữa lớn hơn x → tìm nửa trái
            right = mid - 1

    return -1                   # không tìm thấy
pos = binary_search(arr, x)
if pos == -1:
    print(f"Không tìm thấy {x} trong mảng.")
else:
    print(f"Tìm thấy {x} tại vị trí {pos}.")
