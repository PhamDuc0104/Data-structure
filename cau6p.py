# Câu 6: Phương pháp chia
# h(x) = x % M
keys = [1, 2, 42, 4, 12, 14, 17, 13, 37]
M = 20  # kích thước bảng băm

print("Bảng băm (M = 20):")
for key in keys:
    h = key % M
    print(f"h({key}) = {key} % {M} = {h}")
