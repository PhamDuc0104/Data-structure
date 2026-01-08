def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Chọn phần tử giữa làm pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

array = [18, 35, 28, 56]
sorted_array = quick_sort(array)
print("Mảng sau khi sắp xếp tăng dần:", sorted_array)