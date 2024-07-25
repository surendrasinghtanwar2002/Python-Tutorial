##method to convert the user input as per the input

##get_number function
def get_number(user_number):
    try:
        if "." in user_number:
            float_number = float(user_number)
            return float_number
        else:
            int_number = int(user_number)
            return int_number
    except:
            print("You have some error due to some technical issue we will check it soon")
            return None
##List for celsius and faherniet
Celsius_list = (-273.15,-45.56,-40.00,-34.44,-28.89,-23.33,-17.78,-12.22,-6.67,-1.11,0,4.44,10.00,15.56,21.11,26.67,32.22,37,37.78,43.33,48.89,54.44,60.00,65.56,71.11,76.67,82.22,87.78,93.33,100)
fahernet_list = (-459.67,-50,-40,-30,-20,-10,0,10,20,30,32,40,50,60,70,80,90,98.6,100,110,120,130,140,150,160,170,180,190,200,212,)


##function to convert celcius to faherniet and faherneit to celcius
def multi_conversion(value):
    try:
        if value in Celsius_list:
            Fahrenheit = (value * (9/5)) + 32
            print(f"This is result of converting Celsius to fahernet {Fahrenheit} degree") 
        elif value in fahernet_list:
            Celsius = (value-32)* 5 / 9
            print(f"This is result of converting fahernet to celsius {Celsius} degree")
        else:
            print("You have given a value that cannot be proceed please check this out")
    except Exception as e:
            print(f"You have some error error due to some technical issue we will check it soon {e}")

#taking user input for the conversion
user_input = (input("Enter your number = "))

#calling get_number function and passing the argument 
result = get_number(user_input)

#calling multi_conversion function and passing the argument
new_result = multi_conversion(result)