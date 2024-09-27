class Diem:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Elip(Diem):
    def __init__(self, ban_kinh_lon, ban_kinh_nho, x=0, y=0):
        super().__init__(x, y)
        self.ban_kinh_lon = ban_kinh_lon
        self.ban_kinh_nho = ban_kinh_nho

    def dien_tich(self):
        return 3.14 * self.ban_kinh_lon * self.ban_kinh_nho

class DuongTron(Elip):
    def __init__(self, ban_kinh, x=0, y=0):
        super().__init__(ban_kinh, ban_kinh, x, y)

# Chương trình chính
elip = Elip(5, 3)
print("Diện tích elip:", elip.dien_tich())  # Output: Diện tích elip: 47.1

duong_tron = DuongTron(5)
print("Diện tích đường tròn:", duong_tron.dien_tich())  # Output: Diện tích đường tròn: 78.5
