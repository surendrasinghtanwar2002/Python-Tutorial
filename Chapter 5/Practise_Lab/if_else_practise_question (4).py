##taking user input from the and calculating its discount


##predefined bill no list to validate
bill_no = ([x*2 for x in range(10000)])


##minimum and maximum amount value
min_value = 50
max_value = 100

##function to find the discount price
def discountvalidation(* token_no):
    try:
        amount_value,bill_value = token_no ##unwrap the tupple
        if bill_value in bill_no:
            if amount_value >= max_value:
                max_discount_claimed = (amount_value /100)*20
                max_final_amount = amount_value- int(max_discount_claimed)
                return max_final_amount
            elif amount_value>= min_value and amount_value < max_value:
                min_discount_claimed = (amount_value/100) *20
                min_final_amount = amount_value- int(min_discount_claimed)
                return min_final_amount
        else:
            if bill_value not in bill_no:
                print(f"Your given bill no {bill_no} is not valid. Please try again later")
            else:
                print(f"Your amount is not right please check it again {amount_value}")
                return None
    except:
            print("Your value is not working")


#taking user input
user_amount =int(input("Enter your amount you have purchased = "))
bill_receipt = int(input("Enter your bill receipt number please ="))

#calling function and passing values
result = discountvalidation(user_amount,bill_receipt)

print(f"This is your discounted price after deduction {result}$")