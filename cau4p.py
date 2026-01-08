A = [40, 15, 75, 30]

n = len(A)
for i in range(n - 1):
    for j in range(n - i - 1):
        if A[j] > A[j + 1]:
            A[j], A[j + 1] = A[j + 1], A[j]
    print(f"Sau lần lặp {i + 1}: {A}")

print("Mảng sau khi sắp xếp:", A)
