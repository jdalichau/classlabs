#A = the future value of the investment/loan, including interest
#P = the principal investment amount (the initial deposit or loan amount)
#r = the annual interest rate (decimal)
#n = the number of times that interest is compounded per year
#t = the number of years the money is invested or borrowed for

#A = P (1 + r/n) (nt)

p = int(input("How much is your principle debt?"))
r = float(input("What's your interest rate in decimal notation"))
n = int(input("How many times per year does your interest compound?"))
t = int(input("How many years will you be paying on this debt?"))

a = p*(((1 + r/n))**(n*t))

print(a)
