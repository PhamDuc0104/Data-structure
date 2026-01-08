def max_meetings(meetings):
    # Sắp xếp theo thời điểm kết thúc
    meetings.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -1
    
    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count

# Độ phức tạp: O(n log n)