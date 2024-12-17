num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ")
match operation:
 case _ if operation == "+":
  print (f"The result is {num1 + num2}.")
 case _ if operation == "-":
  print (f"The result is {num1 - num2}.")
 case _ if operation == "*":
  print (f"The result is {num1 * num2}.")
 case _ if operation == "/":
  if num2 == 0:
   print ("Cannot devide by zero.")
  else:
   print (f"The result is {num1 / num2}.")
