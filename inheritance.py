# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# d = Dog()
# d.eat()
# d.bark()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def __init__(self, name, age, roll_no):
#         super().__init__(name, age)
#         self.roll_no = roll_no

#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Roll No:", self.roll_no)

# s = Student("Sejal", 20, 101)
# s.display()


# class Vehicle:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color

# class Car(Vehicle):
#     def __init__(self, brand, color, model):
#         super().__init__(brand, color)
#         self.model = model

#     def display(self):
#         print("Brand:", self.brand)
#         print("Color:", self.color)
#         print("Model:", self.model)

# c = Car("Tata", "Black", "Nexon")
# c.display()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary)
#         self.department = department

#     def display(self):
#         print("Name:", self.name)
#         print("Salary:", self.salary)
#         print("Department:", self.department)

# m = Manager("Rahul", 50000, "IT")
# m.display()


# class Mobile:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

# class Smartphone(Mobile):
#     def __init__(self, brand, price, ram, storage):
#         super().__init__(brand, price)
#         self.ram = ram
#         self.storage = storage

#     def display(self):
#         print("Brand:", self.brand)
#         print("Price:", self.price)
#         print("RAM:", self.ram)
#         print("Storage:", self.storage)

# s = Smartphone("Oppo", 25000, "8GB", "128GB")
# s.display()



# class Father:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Son(Father):
#     def display(self):
#         print("Father Name:", self.name)
#         print("Father Age:", self.age)

# s = Son("Ramesh", 45)
# s.display()



# class Person:
#     def __init__(self, name, city):
#         self.name = name
#         self.city = city

# class Student(Person):
#     def __init__(self, name, city, course):
#         super().__init__(name, city)
#         self.course = course

#     def display(self):
#         print("Name:", self.name)
#         print("City:", self.city)
#         print("Course:", self.course)

# s = Student("Sejal", "Pune", "Python")
# s.display()



# class Bank:
#     def __init__(self, bank_name):
#         self.bank_name = bank_name

# class Account(Bank):
#     def __init__(self, bank_name, acc_no, balance):
#         super().__init__(bank_name)
#         self.acc_no = acc_no
#         self.balance = balance

#     def display(self):
#         print("Bank:", self.bank_name)
#         print("Account Number:", self.acc_no)
#         print("Balance:", self.balance)

# a = Account("SBI", 12345, 50000)
# a.display()


# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed

#     def display(self):
#         print("Animal Name:", self.name)
#         print("Breed:", self.breed)

# d = Dog("Tommy", "Labrador")
# d.display()


# class Laptop:
#     def __init__(self, brand, price):
#         self.brand = brand
#         self.price = price

# class GamingLaptop(Laptop):
#     def __init__(self, brand, price, graphics):
#         super().__init__(brand, price)
#         self.graphics = graphics

#     def display(self):
#         print("Brand:", self.brand)
#         print("Price:", self.price)
#         print("Graphics Card:", self.graphics)

# g = GamingLaptop("Asus", 75000, "NVIDIA RTX")
# g.display()


# class Grandfather:
#     def show1(self):
#         print("Grandfather property: House")

# class Father(Grandfather):
#     def show2(self):
#         print("Father property: Car")

# class Son(Father):
#     def show3(self):
#         print("Son property: Bike")

# s = Son()
# s.show1()
# s.show2()
# s.show3()


# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class Puppy(Dog):
#     def weep(self):
#         print("Puppy is weeping")

# p = Puppy()
# p.eat()
# p.bark()
# p.weep()


# class Person:
#     def __init__(self, name):
#         self.name = name

# class Employee(Person):
#     def __init__(self, name, emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id

# class Manager(Employee):
#     def __init__(self, name, emp_id, department):
#         super().__init__(name, emp_id)
#         self.department = department

#     def display(self):
#         print("Name:", self.name)
#         print("Employee ID:", self.emp_id)
#         print("Department:", self.department)

# m = Manager("Rahul", 101, "IT")
# m.display()



# class Vehicle:
#     def __init__(self, brand):
#         self.brand = brand

# class Car(Vehicle):
#     def __init__(self, brand, model):
#         super().__init__(brand)
#         self.model = model

# class ElectricCar(Car):
#     def __init__(self, brand, model, battery):
#         super().__init__(brand, model)
#         self.battery = battery

#     def display(self):
#         print("Brand:", self.brand)
#         print("Model:", self.model)
#         print("Battery:", self.battery)

# e = ElectricCar("Tata", "Nexon EV", "40 kWh")
# e.display()



# class School:
#     def __init__(self, school_name):
#         self.school_name = school_name

# class Teacher(School):
#     def __init__(self, school_name, subject):
#         super().__init__(school_name)
#         self.subject = subject

# class Principal(Teacher):
#     def __init__(self, school_name, subject, name):
#         super().__init__(school_name, subject)
#         self.name = name

#     def display(self):
#         print("School:", self.school_name)
#         print("Subject:", self.subject)
#         print("Principal:", self.name)

# p = Principal("ABC School", "Maths", "Mr. Sharma")
# p.display()


# class Father:
#     def father_name(self):
#         print("Father: Ramesh")

# class Mother:
#     def mother_name(self):
#         print("Mother: Sunita")

# class Child(Father, Mother):
#     def child_name(self):
#         print("Child: Rahul")

# c = Child()
# c.father_name()
# c.mother_name()
# c.child_name()


# class Camera:
#     def click(self):
#         print("Taking a photo")

# class Phone:
#     def call(self):
#         print("Making a call")

# class Smartphone(Camera, Phone):
#     def display(self):
#         print("Smartphone features")

# s = Smartphone()
# s.click()
# s.call()
# s.display()


# class Animal:
#     def eat(self):
#         print("Animal is eating")

# class Dog(Animal):
#     def bark(self):
#         print("Dog is barking")

# class Cat(Animal):
#     def meow(self):
#         print("Cat is meowing")

# d = Dog()
# d.eat()
# d.bark()

# c = Cat()
# c.eat()
# c.meow()



# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")

# class Car(Vehicle):
#     def start(self):
#         print("Car is starting with a key")

# v = Vehicle()
# v.start()

# c = Car()
# c.start()

