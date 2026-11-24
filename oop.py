
# class Student:
#     def __init__(self, name, roll_no, course):
#         self.name = name
#         self.roll_no = roll_no
#         self.course = course

#     def display_details(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Course:", self.course)

# s1 = Student("Sejal", 101, "Python")
# s2 = Student("Sneha", 102, "Java")
# s3 = Student("Snehal", 103, "C++")

# s1.display_details()
# s2.display_details()
# s3.display_details()



# class Employee:
#     def __init__(self, name, emp_id, basic_salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.basic_salary = basic_salary

#     def calculate_salary(self):
#         annual_salary = self.basic_salary * 12
#         print("Employee Name:", self.name)
#         print("Employee ID:", self.emp_id)
#         print("Basic Salary:", self.basic_salary)
#         print("Annual Salary:", annual_salary)


# e1 = Employee("snehal", 101, 15000)
# e2 = Employee("Sneha", 102, 20000)
# e3 = Employee("Sejal", 103, 25000)

# e1.calculate_salary()
# e2.calculate_salary()
# e3.calculate_salary()



# class Mobile:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def display_details(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Price:", self.price)

#     def apply_discount(self, discount):
#         final_price = self.price - discount
#         print("Discount:", discount)
#         print("Final Price:", final_price)


# m1 = Mobile("Vivo", "T5", 25000)
# m2 = Mobile("Oppo", "K14", 20000)
# m3 = Mobile("Realme", "P4", 18000)

# m1.display_details()
# m1.apply_discount(2000)
# m2.display_details()
# m2.apply_discount(1500)
# m3.display_details()
# m3.apply_discount(1000)



# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount
#         print("Deposited Amount:", amount)

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#             print("Withdrawn Amount:", amount)
#         else:
#             print("Insufficient Balance")

#     def display_balance(self):
#         print("Account Holder:", self.name)
#         print("Available Balance:", self.balance)


# b1 = BankAccount("Sejal", 10000)

# b1.display_balance()
# b1.deposit(5000)
# b1.display_balance()
# b1.withdraw(2000)
# b1.display_balance()



# class Car:
#     def __init__(self, car_name, rent_per_day):
#         self.car_name = car_name
#         self.rent_per_day = rent_per_day

#     def calculate_rent(self, days):
#         total_rent = self.rent_per_day * days

#         print("Car Name:", self.car_name)
#         print("Rent Per Day:", self.rent_per_day)
#         print("Rental Days:", days)
#         print("Total Rent:", total_rent)


# c1 = Car("Swift", 1500)
# c2 = Car("Baleno", 2000)
# c3 = Car("BMW", 5000)

# c1.calculate_rent(3)
# c2.calculate_rent(5)
# c3.calculate_rent(2)



# class Laptop:
#     def __init__(self):
#         self.brand = "Dell"
#         self.ram = "16GB"
#         self.price = 55000

#     def display_details(self):
#         print("Brand:", self.brand)
#         print("RAM:", self.ram)
#         print("Price:", self.price)

# l1 = Laptop()
# l1.display_details()




# class Book:
#     def __init__(self, book_name, author_name, book_price):
#         self.book_name = book_name
#         self.author_name = author_name
#         self.book_price = book_price

#     def display(self):
#         print("Book Name:", self.book_name)
#         print("Author:", self.author_name)
#         print("Price:", self.book_price)

# b1 = Book("Python", "John", 500)
# b2 = Book("Java", "James", 600)

# b1.display()
# b2.display()



# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def calculate_area(self):
#         area = self.length * self.width
#         print("Area:", area)

# r1 = Rectangle(10, 5)
# r1.calculate_area()


# class ElectricityBill:
#     def __init__(self, customer_name, units):
#         self.customer_name = customer_name
#         self.units = units

#     def calculate_bill(self):
#         if self.units <= 100:
#             bill = self.units * 5
#         elif self.units <= 200:
#             bill = (100 * 5) + (self.units - 100) * 7
#         else:
#             bill = (100 * 5) + (100 * 7) + (self.units - 200) * 10

#         print("Customer:", self.customer_name)
#         print("Units:", self.units)
#         print("Total Bill: ₹", bill)

# e1 = ElectricityBill("Tejal", 250)
# e1.calculate_bill()




# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def display_product(self):
#         print("Product:", self.name)
#         print("Price:", self.price)
#         print("Quantity:", self.quantity)

#     def calculate_total_price(self):
#         total = self.price * self.quantity
#         print("Total Price:", total)

#     def update_quantity(self, new_quantity):
#         self.quantity = new_quantity
#         print("Updated Quantity:", self.quantity)

# p1 = Product("Laptop", 50000, 2)
# p1.display_product()
# p1.calculate_total_price()
# p1.update_quantity(5)



# class Employee:
#     company_name = "TCS"
#     employee_count = 0

#     def __init__(self, employee_name, employee_id):
#         self.employee_name = employee_name
#         self.employee_id = employee_id
#         Employee.employee_count += 1

#     def display(self):
#         print("Company:", Employee.company_name)
#         print("Name:", self.employee_name)
#         print("ID:", self.employee_id)
#         print("Total Employees:", Employee.employee_count)

# e1 = Employee("Tejal", 101)
# e2 = Employee("Priya", 102)
# e1.display()
# e2.display()


# class Student:
#     school_name = "ABC School"

#     def __init__(self, student_name, roll_number):
#         self.student_name = student_name
#         self.roll_number = roll_number

#     def display(self):
#         percentage = 85

#         print("School:", Student.school_name)
#         print("Name:", self.student_name)
#         print("Roll Number:", self.roll_number)
#         print("Percentage:", percentage)

# s1 = Student("Tejal", 1)
# s1.display()



# class ShoppingCart:
#     discount_percentage = 10

#     def __init__(self, customer_name, total_amount):
#         self.customer_name = customer_name
#         self.total_amount = total_amount

#     def calculate_discount(self):
#         discount = self.total_amount * ShoppingCart.discount_percentage / 100
#         final_amount = self.total_amount - discount

#         print("Customer:", self.customer_name)
#         print("Total Amount:", self.total_amount)
#         print("Discount:", discount)
#         print("Final Amount:", final_amount)

# c1 = ShoppingCart("Tejal", 2000)
# c1.calculate_discount()










