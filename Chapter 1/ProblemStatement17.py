#In this section we will practise a question
Amount = 120  #Avilablemoney
Withdrawl = int(input("Enter your withdrawl amount = ")) #Trying to withdraw the money
Bank_Charges = 0.50
if(Withdrawl%5==0 and Withdrawl+Bank_Charges<Amount and Withdrawl>=0): 
    Final_amount= Amount-Withdrawl+Bank_Charges # In this statement we deduct the withdrawl amount from the avilableamount
    print("Your pending amount is",Final_amount ) #printed the actual amount after succesful withdrawl
else:
    if(Withdrawl%5!=0 and Withdrawl<0):
        print("Incorrect amount value or negative amount value")
    if(Withdrawl+Bank_Charges>Amount): #checking the condition that if bank withdrawl is more then avilable money
        print("Your account does not have sufficient amount of",Withdrawl+Bank_Charges,"Your account have",Amount,"only")