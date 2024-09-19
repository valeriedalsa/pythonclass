number = int(input("Enter number: "))
if number <= 0:
    print("You can only input positive integers.")
elif number%2==0 and number%3==0 and number%5==0 and number > 0:
    print("The number is magic!")
else: 
    print("The number is not magic.")
