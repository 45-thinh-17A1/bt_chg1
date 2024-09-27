class Date:
    def __init__(self, day=1, month=1, year=2000):
        self.day = day
        self.month = month
        self.year = year

    def display(self):
        print(f"{self.day}/{self.month}/{self.year}")

    def next_day(self):
        # Giả định mỗi tháng có 30 ngày để đơn giản hóa
        self.day += 1
        if self.day > 30:
            self.day = 1
            self.month += 1
        if self.month > 12:
            self.month = 1
            self.year += 1

# Chương trình chính
date = Date(30, 12, 2023)
date.display()  # Output: 30/12/2023
date.next_day()
date.display()  # Output: 1/1/2024
