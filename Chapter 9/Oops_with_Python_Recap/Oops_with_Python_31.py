                            ## Polymorphism with Method Overriding ##

class Payment:
    def process_payment(self, amount):
        return f"Your payment is being performed using cash mode of amount ${amount:.2f}"

class Paypal(Payment):  # Inheriting from Payment class
    def process_payment(self, amount):
        return f"Your PayPal amount of ${amount:.2f} is being transferred successfully."

class CreditCardPayment(Payment):  # Inheriting from Payment class
    def process_payment(self, amount):
        return f"Your credit card payment of ${amount:.2f} is being processed successfully."
    

def process_payment(payment_method, amount):
    print(payment_method.process_payment(amount))  # Print the result


# Create instances for each payment method
credit_card = CreditCardPayment()
paypal = Paypal()
cash = Payment()    

# Providing a static amount
amount = 100.0

# Process payments
for payment in [credit_card, paypal, cash]:
    process_payment(payment, amount)
