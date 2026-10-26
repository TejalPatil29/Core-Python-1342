# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# i = 1
# while i <= 50:
#      print(i)
#      i += 1

# i = 10 
# while i >= 1:
#     print(i)
#     i -= 1

# i = 2
# while i <= 20:
#     print(i)
#     i +=2

# i = 1
# while i <= 50:
#     print(i)
#     i += 2

# i = 1
# while i <= 100:
#     print(i)
#     i += 5

# i = 10
# while i <= 100:
#     print(i)
#     i += 10

# i = -10
# while i <= 10:
#     print(i)
#     i += 1

# i = -5
# while i <= -1:
#     print(i)
#     i += 1

# i = 1
# while i <= 10:
#     print("2 x", i, "=", 2 * i)
#     i += 1

# i = 1
# while i <= 10:
#     print("5 x", i, "=", 5 * i)
#     i += 1

# n = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1

# i = 1
# while i <= 10:
#     print("Sejal")
#     i += 1

# i = 1
# while i <= 20:
#     print("Hello World")
#     i += 1

# i = 100
# while i >= 50:
#     print(i)
#     i -= 1

# i = 1
# total = 0
# while i <= 10:
#     total += i
#     i += 1
# print("Sum:", total)


# i = 1
# total = 0
# while i <= 100:
#     total += i
#     i += 1
# print("Sum:", total)


#  i = 2
# total = 0
# while i <= 50:
#     total += i
#     i += 2
# print("Sum:", total)


# i = 1
# total = 0
# while i <= 50:
#     total += i
#     i += 2
# print("Sum:", total)


# i = 1
# count = 0
# while i <= 100:
#     count += 1
#     i += 1
# print("Count:", count)


# i = 2
# count = 0
# while i <= 50:
#     count += 1
#     i += 2
# print("Count:", count)


# i = 1
# count = 0
# while i <= 100:
#     count += 1
#     i += 2
# print("Count:", count)


# n = int(input("Enter N: "))
# i = 1
# total = 0
# while i <= n:
#     total += i
#     i += 1
# print("Sum:", total)


# i = 10
# total = 0
# while i >= 1:
#     total += i
#     i -= 1
# print("Sum:", total)


# i = 1
# product = 1
# while i <= 5:
#     product *= i
#     i += 1
# print("Product:", product)


# n = int(input("Enter a number: "))
# factorial = 1
# i = 1
# while i <= n:
#     factorial *= i
#     i += 1
# print("Factorial:", factorial)

# n = int(input("Enter a number: "))
# number = abs(n)
# reverse = 0
# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number //= 10
# if n < 0:
#     reverse = -reverse
# print("Reversed number:", reverse)


# n = abs(int(input("Enter a number: ")))
# count = 0
# if n == 0:
#     count = 1
# else:
#  while n > 0:
#         count += 1
#         n //= 10
# print("Number of digits:", count)


# n = abs(int(input("Enter a number: ")))
# total = 0
# while n > 0:
#     total += n % 10
#     n //= 10
# print("Sum of digits:", total)



# n = abs(int(input("Enter a number: ")))
# product = 1
# if n == 0:
#     product = 0
# else:
#     while n > 0:
#         product *= n % 10
#         n //= 10
# print("Product of digits:", product)


# n = int(input("Enter a number: "))
# original = abs(n)
# number = original
# reverse = 0
# while number > 0:
#     reverse = reverse * 10 + number % 10
#     number //= 10
# if n >= 0 and original == reverse:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

# n = int(input("Enter a non-negative number: "))
# digits = len(str(n))
# number = n
# total = 0
# while number > 0:
#     digit = number % 10
#     total += digit ** digits
#     number //= 10
# if total == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")

# 
# n = int(input("Enter a number: "))
# divisor = 2
# is_prime = n >= 2
# while divisor * divisor <= n and is_prime:
#     if n % divisor == 0:
#         is_prime = False
#     divisor += 1
# if is_prime:
#     print("Prime number")
# else:
#     print("Not a prime number")

# terms = int(input("Enter the number of terms: "))
# a = 0
# b = 1
# count = 0
# while count < terms:
#     print(a, end=" ")
#     a, b = b, a + b
#     count += 1

# n = abs(int(input("Enter a number: ")))
# largest = 0
# while n > 0:
#     digit = n % 10
#     if digit > largest:
#         largest = digit
#     n //= 10
# print("Largest digit:", largest)

# number = 1
# while number <= 100:
#     if number % 5 != 0:
#         print(number)
#     number += 1

# number = 1
# while number < 25:
#     print(number)
#     number += 1

# number = int(input("Enter a number (0 to stop): "))
# while number != 0:
#     number = int(input("Enter another number (0 to stop): "))
# print("You entered 0.")

# total = 0
# number = float(input("Enter a number (0 to finish): "))
# while number != 0:
#     total += number
#     number = float(input("Enter another number (0 to finish): "))
# print("Sum:", total)

# correct_password = "python123"
# password = input("Enter the password: ")
# while password != correct_password:
#     password = input("Incorrect. Try again: ")
# print("Access granted.")