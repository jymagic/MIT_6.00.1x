balance = 320000
annualInterestRate = 0.2

init_balance = balance
minpayment=0
UnpaidBalance=0
Interest=0
i=1
Monthlypaymentlb = balance / 12
Monthlypaymentub = (balance * ((1 + annualInterestRate / 12) ** 12)) / 12
epsilon= 0.03

while abs(balance) > epsilon:
    balance = init_balance
    UnpaidBalance = 0
    Interest = 0
    i = 1
    minpayment = (Monthlypaymentlb+Monthlypaymentub)/2

    while i <= 12:
        UnpaidBalance= balance - minpayment
        Interest= annualInterestRate / 12 * UnpaidBalance
        balance= UnpaidBalance + Interest
        i+=1

    if balance > epsilon:
        Monthlypaymentlb = minpayment
    elif balance < -epsilon:
        Monthlypaymentub = minpayment

print ("Lowest Payment: %s" % round(minpayment,2))
