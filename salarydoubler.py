salaryperday = 0.1
days = int(input("How many days did you work? "))
earnedtotal = 0
day = 1
print("Days \t\t Money made")
while day <= days:
    print(f"day \t\t   {float(salaryperday):,.2f}")
    earnedtotal = earnedtotal + salaryperday 
    salaryperday *= 2
    day += 1
print(f"Earned total:\t   {float(earnedtotal):,.2f}") 
