def count_pairs_sum_less_than_k(arr, k):
    arr.sort()  # O(n log n)
    count = 0
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] + arr[right] < k:
            # Tất cả các cặp từ left đến right-1 đều hợp lệ
            count += (right - left)
            left += 1
        else:
            right -= 1
    
    return count