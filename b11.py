class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def chu_vi(self):
        return self.a + self.b + self.c

class TamGiacVuong(TamGiac):
    def __init__(self, a, b):
        super().__init__(a, b, (a**2 + b**2)**0.5)

class TamGiacCan(TamGiac):
    def __init__(self, canh_ben, day):
        super().__init__(canh_ben, canh_ben, day)

class TamGiacDeu(TamGiacCan):
    def __init__(self, canh):
        super().__init__(canh, canh)

# Chương trình chính
tam_giac_vuong = TamGiacVuong(3, 4)
print("Chu vi tam giác vuông:", tam_giac_vuong.chu_vi())  # Output: 12.0

tam_giac_deu = TamGiacDeu(5)
print("Chu vi tam giác đều:", tam_giac_deu.chu_vi())  # Output: 15
