                                            ## In this step we will practise static methods in python  ###

class banking_loan:
    global_interest_rate = 250
    def __init__(self,name,age,credit_score,amount) -> None:
        self.Name = name
        self.age = age
        self.credit_score = credit_score
        self.amount = amount
    
    @staticmethod
    def final_loan_amount(amount):
        final_amount = amount+banking_loan.global_interest_rate
        return final_amount

    def loan_details(self):
        print("Hello this is your loan amount")
        final_amount = self.final_loan_amount(self.amount)
        return f"Hello Mr {self.Name} and your age is {self.age} and your credit score is {self.credit_score} and your final amount is {final_amount}"



##Creating  the first instance 
loan_user1 = banking_loan(name="Surendra Singh Tanwar",age=24,credit_score=78,amount=25000)
print(loan_user1.loan_details())

##Creating  the second instance 
loan_user2 = banking_loan(name="Harish",age=28,credit_score=85,amount=150000000000)
print(loan_user2.loan_details())


