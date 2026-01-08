# Danh sách các khóa
keys = [1533, 3471, 1363, 2564]
M = 5  # kích thước bảng băm

print("Bảng băm (M = 5):")
for key in keys:
    h = key % M
    print(f"h({key}) = {key} % {M} = {h}")