monthlyInvestment = float (input("SIP amount every month?"))
expectedReturns = float(input("Expected returns?"))
numberOfYears = int(input("Duration in years?"))

monthlyRate = expectedReturns/12/100
months = numberOfYears*12

totalReturns = monthlyInvestment * ((((1 + monthlyRate)**(months))-1) *(1 + monthlyRate))/monthlyRate

totalReturns = round(totalReturns)

print ("Your total returns after investing", monthlyInvestment*months, " will be" , "₹" ,totalReturns)
