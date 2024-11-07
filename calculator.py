class Calculator:

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b  # เปลี่ยนจาก 'b - a' เป็น 'a - b'

    def multiply(self, a, b):
        result = 0
        for i in range(abs(b)):  # รองรับเลขติดลบ
            result = self.add(result, abs(a))
        # จัดการกรณีที่ b หรือตัวใดตัวหนึ่งเป็นลบ
        return result if (a >= 0 and b >= 0) or (a < 0 and b < 0) else -result

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")  # จัดการกรณีหารด้วยศูนย์
        result = 0
        remainder = abs(a)
        while remainder >= abs(b):
            remainder = self.subtract(remainder, abs(b))
            result += 1
        # จัดการกรณีที่ผลลัพธ์ควรเป็นลบ
        return result if (a >= 0 and b > 0) or (a < 0 and b < 0) else -result

    def modulo(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")  # จัดการกรณี mod ด้วยศูนย์
        remainder = abs(a)
        while remainder >= abs(b):
            remainder = remainder - abs(b)
        # จัดการกรณีที่ a เป็นลบ
        return remainder if a >= 0 else -remainder