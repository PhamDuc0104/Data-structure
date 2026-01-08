class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinhVien:
    def __init__(self, ma_so, ten, diem_tb):
        self.ma_so = ma_so
        self.ten = ten
        self.diem_tb = diem_tb
    
    def __str__(self):
        return f"Mã: {self.ma_so}, Tên: {self.ten}, ĐTB: {self.diem_tb}"
