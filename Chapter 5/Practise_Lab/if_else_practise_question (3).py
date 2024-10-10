
##taking two input from the user 
first_input = int(input("Enter your number = "))
second_input = int(input("Enter your second number = "))

#validating that which number is bigger or not
if first_input > second_input:
    print("First number is bigger")
elif second_input > first_input:
    print("Second number is bigger")
elif first_input == second_input:
    print("Both value are same")