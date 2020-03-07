# -*- config: utf-8 -*-
class Employee(object):
    raise_amount = 1.1  # 연봉 인상율 클래스 변수

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first.lower() + '.' + last.lower() + '@schoolofweb.net'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def get_pay(self):
        return '현재 "{}"의 연봉은 "{}"입니다.'.format(self.full_name(), self.pay)

    # 클래스 메소드 데코레이터를 사용하여 클래스 메소드를 정의
    @classmethod
    def change_raise_amount(cls, amount):
        # 인상율이 1보다 작으면 재입력
        while amount < 1:
            print('[경고] 인상율은 "1" 보다 작을 수 없습니다.')
            amount = input('[입력] 인상율을 다시 입력하여 주십시오.\n => ')
            amount = float(amount)
        cls.raise_amount = amount
        print('인상율 "{}"가 적용 되었습니다.'.format(amount))


emp_1 = Employee('Sanghee', 'Lee', 50000)
emp_2 = Employee('Minjung', 'Kim', 60000)

# 연봉 인상 전
print(emp_1.get_pay())
print(emp_2.get_pay())

# 연봉 인상율 변경(classmethod 호출 방법)
Employee.change_raise_amount(0.9)

# 연봉 인상
emp_1.apply_raise()
emp_2.apply_raise()

# 연봉 인상 후
print(emp_1.get_pay())
print(emp_2.get_pay())
