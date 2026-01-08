def binary_search(arr, key):
    # Bước 1: Khởi tạo chỉ số biên trái (left) và phải (right)
    left = 0
    right = len(arr) - 1   
    step = 0               

    # Bước 2: Lặp khi còn phạm vi tìm kiếm
    while left <= right:
        step += 1
        print(f"Step {step}: left={left}, right={right}")  

        # Tính chỉ số giữa
        mid = (left + right) // 2
        print(f"   mid={mid}, arr[mid]={arr[mid]}")

        # TH1: Tìm thấy phần tử
        if key == arr[mid]:
            print("   ✅ Tìm thấy key tại vị trí", mid)
            return mid

        # TH2: key nhỏ hơn phần tử giữa → bỏ nửa phải
        if key < arr[mid]:
            right = mid - 1
            print("   🔽 Dời right sang", right)
        else:
            # TH3: key lớn hơn phần tử giữa → bỏ nửa trái
            left = mid + 1
            print("   🔼 Dời left sang", left)

    # Nếu thoát khỏi vòng lặp → không tìm thấy
    return -1


# -----------------------------
# Input
arr = [0, 4, 5, 9, 13, 15, 18, 24, 28, 29, 35]
key = 40

# Gọi hàm
result = binary_search(arr, key)

# Output
print("Vị trí tìm kiếm thu được là:", result)
