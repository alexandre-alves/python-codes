#!/usr/bin/env python3
print ("type the first value")
first_input = int(input())
print ("type the operation")
operation = input()
print ("type the second value")
second_input = int(input())
if operation == "+":
    result = first_input + second_input
    print (result)
elif operation == "-":
    result = first_input - second_input
    print (result)
elif operation == "*":
    result = first_input * second_input
    print (result)
elif operation == "/":
    result = first_input / second_input
    print (result) 
  


