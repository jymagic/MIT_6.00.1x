init_balance = balance
minpayment=0
UnpaidBalance=0
Interest=0
i=1

while balance >=0:
    balance = init_balance
    UnpaidBalance = 0
    Interest = 0
    i = 1
    minpayment+=10

    while i <= 12:
        UnpaidBalance= balance - minpayment
        Interest= annualInterestRate / 12 * UnpaidBalance
        balance= UnpaidBalance + Interest
        i+=1

print ("Lowest Payment: %s" % minpayment)