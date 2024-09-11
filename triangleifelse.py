side1 = int(input("Print one triangle side length: "))
side2 = int(input("Print the second sides' length: "))
side3 = int(input("Print the last sides' length of the triangle: "))




if side1 == side2 == side3:
    print("This is an equailateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("This is an isosceles triangle.")
else:
    print("This is a scalene triangle.")





    



