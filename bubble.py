def bubble_sort_steps(arr):
    n = len(arr)
    steps = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps += 1
    return steps

array = [7, 9, 3, 5, 0, 1]
steps = bubble_sort_steps(array)
print("Số bước đổi chỗ để sắp xếp từ thấp đến cao là:", steps)