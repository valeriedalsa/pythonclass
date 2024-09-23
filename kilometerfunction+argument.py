kilo_to_miles= 0.6214

def main():
    userkilo = float(input("Enter distance in kilometers: "))
    showmiles(userkilo)

def showmiles(kilometers):
    miles = kilometers * kilo_to_miles
    print(f'The conversion of {kilometers:.2f} kilometers')
    print(f'to miles is {miles:.2f} miles')
main()
