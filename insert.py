def insertion_sort_steps(arr):
    n = len(arr)
    shifts = 0  # đếm số lần dịch chuyển
    print("Mảng ban đầu:", arr)

    # Bắt đầu từ phần tử thứ 2
    for i in range(1, n):
        key = arr[i]
        j = i - 1

        print(f"\nChèn phần tử {key}:")
        
        # Dịch các phần tử lớn hơn key sang phải
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            shifts += 1
            print("  Dịch:", arr)
        
        # Chèn key vào đúng chỗ
        arr[j + 1] = key
        print("  Sau khi chèn:", arr)

    print("\nMảng đã sắp xếp:", arr)
    print("Tổng số dịch chuyển:", shifts)


# Test với số 793501 (mảng các chữ số)
array = [7, 9, 3, 5, 0, 1]
insertion_sort_steps(array)
