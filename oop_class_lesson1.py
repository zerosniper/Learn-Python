class employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return "Employee name is " + '{0} {1}'.format(self.first.capitalize(),
                                                      self.last.capitalize())


employee_1 = employee('lisa', 'mollen', '2000')
employee_2 = employee('larry', 'happy', '6000')

print(employee_1.fullname())
print(employee_2.email)
