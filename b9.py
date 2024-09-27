class DaGiac:
    def __init__(self, so_canh, do_dai_canh):
        self.so_canh = so_canh
        self.do_dai_canh = do_dai_canh

    def chu_vi(self):
        return sum(self.do_dai_canh)

class HinhBinhHanh(DaGiac):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__(4, [chieu_dai, chieu_rong, chieu_dai, chieu_rong])
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong

class HinhChuNhat(HinhBinhHanh):
    pass  # Kế thừa toàn bộ từ Hình Bình Hành

class HinhVuong(HinhChuNhat):
    def __init__(self, canh):
        super().__init__(canh, canh)

# Chương trình chính
hinh_vuong = HinhVuong(5)
print("Chu vi hình vuông:", hinh_vuong.chu_vi())  # Output: 20
print("Diện tích hình vuông:", hinh_vuong.dien_tich())  # Output: 25
