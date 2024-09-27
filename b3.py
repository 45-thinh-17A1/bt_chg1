import math

class PhanSo:
    def __init__(self, tu_so=0, mau_so=1):
        self.tu_so = tu_so
        self.mau_so = mau_so
        self.kiem_tra_hop_le()

    def kiem_tra_hop_le(self):
        if self.mau_so == 0:
            raise ValueError("Mẫu số không được bằng 0")

    def nhap(self):
        self.tu_so = int(input("Nhập tử số: "))
        self.mau_so = int(input("Nhập mẫu số: "))
        self.kiem_tra_hop_le()

    def in_phan_so(self):
        print(f"{self.tu_so}/{self.mau_so}")

# Chương trình chính
ps = PhanSo()
ps.nhap()
ps.in_phan_so()
