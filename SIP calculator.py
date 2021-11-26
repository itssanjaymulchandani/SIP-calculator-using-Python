print("SIP amount every month?")
monthlyInvestment = float (input())
print("Expected returns?")
expectedReturns = float(input())
print("Duration in years?")
numberOfYears = int (input())

monthlyRate = expectedReturns/12/100
months = numberOfYears*12

totalReturns = monthlyInvestment * ((((1 + monthlyRate)**(months))-1) *(1 + monthlyRate))/monthlyRate

totalReturns = round(totalReturns)

print ("Your total returns after", numberOfYears, " years will be" , "₹" ,totalReturns)
