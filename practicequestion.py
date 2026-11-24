# num = int(input("Enter a number:"))
# if num % 2 == 0:
#     print(num,"is an even number")
# else:
#     print(num,"is an odd  number")

# num = int(input("Enter a number:"))
# if num > 0:
#     print(num,"is a positive number")
# elif num <0:
#     print(num,"is a negative number")
# else:
#     print(num,"is zero")

# t = 12345
# rev = 0
# for i in range(7):
#     digit = t % 10
#     rev = digit + rev * 10
#     t = t // 10
#     print(rev)

# num = 12345
# rev = 0
# while num > 0:
#     digit = num % 10
#     rev = digit + rev * 10
#     num = num // 10
#     print(rev)

# n = int(input("Enter a number: "))
# original = n
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10
# if rev == original:
#     print(original, "is a palindrome number")
# else:
#     print(original, "is not a palindrome number")

# num = 99
# count = 0
# if num > 1:
#   for i in range(num , num + 1):
#     if num % i == 0:
#       count += 1
#     if count == 2:
#         print("prime number")
#     else:
#         print("not a prime numer") 

# for num in range(2, 101):
#     count = 0
#     for i in range(1, num + 1):
#         if num % i == 0:
#             count += 1
#     if count == 2:
#         print(num)

# num = 5
# fact = 1
# for i in range(1 , num + 1):
#   fact = fact * i
#   print("factorial :",fact)

# num = 6
# square = num ** 2
# cube = num ** 3
# print ("square:", square)
# print("cube:", cube)

# str = "python"
# rev = " " 
# for i in str:
#     rev = i + rev
#     print("Reverse string:", rev) 

# a = [10,27,30,45,50,60]
# for i in a:
#     if i % 2 == 0:
#         print ("Even:", i)
#     else:
#         print("odd:", i)

# a = [10, 15, 20, 25, 30, 35]
# even = 0
# odd = 0
# for i in a:
#     if i % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print("even count:", even)
# print("odd count:", odd)



# a = [10, 15, 20, 25, 30, 35]
# rev = []
# for i in a:
#     rev = [i]+rev
#     print(rev)

# a =[2,4,7,8,6,10,5]
# for num in a:
#     count = 0
#     for i in range(1, num+1):
#         if num % i ==0:
#             count += 1
#             if count == 2:
#                 print(num)


# a =[10,"python",20,"java",30,"sql"]
# for i in a:
#     if isinstance(i,str):
#         print(i)

# a =[10,35,56,"python",22,"sql"]
# for i in a:
#     if type(i)==int:
#         print(i)

# a =[10,35,56,"python",22,"sql"]
# for i in a:
#     if isinstance(i,int):
#         print(i)        

# t =(10,20,30,40,50,60,70)
# max = t[0]
# for i in t:
#     if i > max:
#         max = i
#         print("maximum:",max)


# t = (10, 20, 30, 40, 50, 60, 70)
# minimum = t[0]
# for i in t:
#     if i < minimum:
#         minimum = i
# print("minimum:", minimum)


# t =(10,20,30,40,50,60,70)
# total = sum (t)
# print("sum:",total)


# t =(10,20,30,40,50,60,70)
# count = 0
# for i in t:
#     count += 1
#     print("length:",count)

# t =(5,10,15,20)
# total = 0
# for i in t:
#     total += i
#     print("total:",total)

# t = (10,25,30,45,50,60,70)
# for i in t:
#     if i % 2 == 0:
#       print(i)


# students ={"name":"rahul","age":23,"city":"pune"}
# for key, value in students.items():
#      print(key,value)


# students ={"riya":89,"neha":93,"priya":78}
# total = 0
# for i in students.values():
#     total += i
#     print("total marks:",total)


# students ={"riya":89,"neha":93,"priya":78,"rahul":56}
# for key ,value in students.items():
#     if  value > 60:
#         print(key,value)
    

# students ={"riya":89,"neha":93,"priya":78,"rahul":25}
# count = 0
# for i in students.values():
#     if i > 35:
#         count += 1
#         print("passed student:",count)



# students ={"riya":89,"neha":93,"priya":78,"rahul":25}
# max = 0
# name =" "
# for key,Value in students.items():
#   if Value > max:
#     max = Value
#     name = key
#     print("highest marks:",max)
#     print("student name:",name)


# students ={"riya":89,"neha":93,"priya":78,"rahul":25}
# highest = max (students.values())
# print("highest marks:",highest)