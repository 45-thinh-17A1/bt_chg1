class ThiSinh:
    def __init__(self, ho_ten="", diem_toan=0, diem_ly=0, diem_hoa=0):
        self.ho_ten = ho_ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def nhap(self):
        self.ho_ten = input("Nhập họ tên thí sinh: ")
        self.diem_toan = float(input("Nhập điểm Toán: "))
        self.diem_ly = float(input("Nhập điểm Lý: "))
        self.diem_hoa = float(input("Nhập điểm Hóa: "))

    def tong_diem(self):
        return self.diem_toan + self.diem_ly + self.diem_hoa

    def thong_tin(self):
        print(f"Họ tên: {self.ho_ten}, Tổng điểm: {self.tong_diem()}")

# Chương trình chính
danh_sach_thi_sinh = []
so_thi_sinh = int(input("Nhập số lượng thí sinh: "))

for i in range(so_thi_sinh):
    ts = ThiSinh()
    ts.nhap()
    danh_sach_thi_sinh.append(ts)

# Sắp xếp danh sách thí sinh theo tổng điểm
danh_sach_thi_sinh.sort(key=lambda ts: ts.tong_diem(), reverse=True)

# In ra danh sách thí sinh trúng tuyển (điểm chuẩn là 20)
print("\nDanh sách thí sinh trúng tuyển:")
for ts in danh_sach_thi_sinh:
    if ts.tong_diem() >= 20:
        ts.thong_tin()
