from collections import deque

def sort_with_two_queues(arr):
    q1 = deque(arr)
    q2 = deque()
    n = len(arr)
    
    for i in range(n):
        min_val = float('inf')
        # Tìm min trong q1
        for _ in range(len(q1)):
            val = q1.popleft()
            if val < min_val:
                min_val = val
            q2.append(val)
        
        # Chuyển lại q1, trừ min
        found = False
        while q2:
            val = q2.popleft()
            if val == min_val and not found:
                found = True
                continue
            q1.append(val)
    
    return result