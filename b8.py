class Employee:
    def __init__(self, ho_ten="", ngay_sinh=None, ngay_vao_cong_ty=None):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh if ngay_sinh else Date()
        self.ngay_vao_cong_ty = ngay_vao_cong_ty if ngay_vao_cong_ty else Date()

    def nhap(self):
        self.ho_ten = input("Nhập họ tên nhân viên: ")
        day, month, year = map(int, input("Nhập ngày sinh (dd mm yyyy): ").split())
        self.ngay_sinh = Date(day, month, year)
        day, month, year = map(int, input("Nhập ngày vào công ty (dd mm yyyy): ").split())
        self.ngay_vao_cong_ty = Date(day, month, year)

    def thong_tin(self):
        print(f"Họ tên: {self.ho_ten}")
        print("Ngày sinh:", end=" ")
        self.ngay_sinh.display()
        print("Ngày vào công ty:", end=" ")
        self.ngay_vao_cong_ty.display()

# Chương trình chính
employee = Employee()
employee.nhap()
employee.thong_tin()
