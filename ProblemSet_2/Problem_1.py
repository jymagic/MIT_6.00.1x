UnpaidBalance=0
Interest=0
i=1

while i <= 12:
    minpayment= monthlyPaymentRate * balance
    UnpaidBalance= balance - minpayment
    Interest= annualInterestRate / 12 * UnpaidBalance
    balance= UnpaidBalance + Interest
    i+=1

balance = round(balance,2)
print ("Remaining balance: %s" % round(balance,2))