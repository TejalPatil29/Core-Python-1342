grade = 90
match grade:
 case 90|91|92|93|94|95:
  print("grade A")
 case 80|81|82|83|84|85:
  print("grade B")
 case 70|71|72|73|74|75:
  print("grade c")
 case 60|61|62|63|64|65:
  print("grade D")
 case _:
  print("Invalid")  

month =input("enter the month")
match month:
 case "jan"|"feb"|"march":
  print("quarter 1")
 case "april"|"may"|"june":
  print("quarter 2")
 case "july"|"augst"|"sept":
  print("quarter 3")
 case "oct"|"nov"|"dec":
  print("quarter 4")
 case _:
  print ("Invalid Input")   
  

a = int(input("enter first number:"))
b = int(input("enter second number:"))
operator ="+"
match operator:
    case "+":
        print("Addition of",a+b)
    case "-":
        print("Subtraction of",a-b)
    case "*":
        print ("Multiplication",a*b)
    case "/":
        print("Division of",a/b)
    case _:
        print("Invalid Input")  


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        print("Result:", a / b if b != 0 else "Cannot divide by zero")
    case _:
        print("Invalid operator")

                 
ch = input("Enter a character: ").lower()
match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("It is a vowel")
    case _:
        print("It is not a vowel")        

 
day = int(input("Enter day number (1-7): "))
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number") 


n = int(input("Enter a number: "))
match n % 2:
    case 0:
        print("Even number")
    case 1:
        print("Odd number") 
    case _:
        print("Invalid") 



light = input("Enter traffic light color: ").lower()
match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Get ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")                


print("1. Hello")
print("2. Good Morning")
print("3. Good Night")
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        print("Hello!")
    case 2:
        print("Good Morning!")
    case 3:
        print("Good Night!")
    case _:
        print("Invalid choice")


n = int(input("Enter a number: "))
match n:
    case x if x > 0:
        print("Positive number")
    case x if x < 0:
        print("Negative number")
    case _:
        print("Zero")




ch = input("Enter a character: ")
match ch:
    case x if len(x) == 1 and x.isupper():
        print("Uppercase letter")
    case x if len(x) == 1 and x.islower():
        print("Lowercase letter")
    case _:
        print("Not a single alphabet letter")