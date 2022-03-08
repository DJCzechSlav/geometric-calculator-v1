import math

continu = 'a'
while continu == 'a':
    bruh = input("What do you want to calculate (sphere / circle / oval): ")  # decide

    if bruh == "sphere":  # sphere

        neco2 = input("surface or volume?:")

        if neco2 == "surface":  # sphere surface
            r = int(input("Enter the radius: "))
            res = 4 * math.pi * r ** 2
            print("Surface of sphere is: ", res)

        elif neco2 == "volume":  # sphere volume
            r = float(input("Enter the radius: "))
            res = 4/3 * math.pi * r ** 3
            print("Volume of sphere is: ", res)

    elif bruh == "circle":  # circle

        neco3 = input("circumference or area?: ")

        if neco3 == "circumference":  # circle circ
            r = float(input("Enter the radius: "))
            res = 2 * math.pi * r
            print("Circumference of circle is: ", res)

        elif neco3 == "area":  # circle area
            r = float(input("Enter the radius"))
            res = math.pi * r
            print("Area of circle is: ", res)

    elif bruh == "oval":  # oval

        neco4 = input("circumference or area?: ")

        if neco4 == "circumference":  # oval circ
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            res = math.pi * math.sqrt(2 * (a ** 2 + b ** 2))
            print("Circumference of oval is: ", res)

        elif neco4 == "area":  # oval are
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            res = math.pi * a * b
            print("Area of oval is: ", res)

    end = input("Do you want to continue (y/n): ")  # end decision
    if end == "y":
        continu = "y"
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    elif end == "n":
        continu = "n"
