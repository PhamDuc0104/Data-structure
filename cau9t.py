import heapq

def smallest_range(arrays):
    # Priority queue: (value, array_idx, element_idx)
    min_heap = []
    max_val = float('-inf')
    
    # Khởi tạo với phần tử đầu của mỗi mảng
    for i, arr in enumerate(arrays):
        heapq.heappush(min_heap, (arr[0], i, 0))
        max_val = max(max_val, arr[0])
    
    result_range = [float('-inf'), float('inf')]
    
    while min_heap:
        min_val, arr_idx, elem_idx = heapq.heappop(min_heap)
        
        # Cập nhật kết quả nếu tốt hơn
        if max_val - min_val < result_range[1] - result_range[0]:
            result_range = [min_val, max_val]
        
        # Nếu hết phần tử trong mảng này, dừng
        if elem_idx + 1 >= len(arrays[arr_idx]):
            break
        
        # Thêm phần tử tiếp theo
        next_val = arrays[arr_idx][elem_idx + 1]
        heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))
        max_val = max(max_val, next_val)
    
    return result_range

# Với ví dụ: A1={1,2,5,7,8}, A2={1,4,6,7,8}, A3={2,5,9,10,12}
# Kết quả: [8,9]