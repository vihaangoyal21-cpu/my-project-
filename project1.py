while True:
    t = input("Enter the type of figure you want (2D/3D) - ")

    if t.strip().lower() == "2d":
        print("Options - Circle , Square , Rectangle , Parallelogram , Triangle , Trapezium")
        
        a = input("Choose the shape/figure - ")

        if a.strip().lower() == "circle":
            r = float(input("Enter the radius of the circle - "))
            from math import pi
            print(f"The circumference of this circle is {2 * pi * r} and its area is {pi * (r ** 2)}")

        elif a.strip().lower() == "square":
            b = float(input("Enter the length of the side - "))
            print(f"The perimeter of this square is {4 * b} and its area is {b ** 2}")

        elif a.strip().lower() == "rectangle" or a.strip().lower() == "parallelogram":
            z = a.strip().lower()
            l = float(input(f"Enter the length of the {z} - "))
            h = float(input(f"Enter the breadth of the {z} - "))
            print(f"The perimeter of this {z} is {2 * (l + h)} and its area is {l * h}")

        elif a.strip().lower() == "triangle":
            e = float(input("Enter the length of a side of the triangle - "))
            f = float(input("Enter the length of the other side of the triangle - "))
            c = float(input("Enter the length of another side of the triangle - "))

            s = (e + f + c) / 2
            Area = (s * (s - e) * (s - f) * (s - c)) ** (1 / 2)

            if f == e == c:
                print(f"The area of this equilateral triangle is {Area}")

            elif f == e != c or e != f == c or c == f != e:
                print(f"The area of this isosceles triangle is {Area}")

            elif f != e != c : 
                print(f"The area of this scalene triangle is {Area}")

        elif a.strip().lower() == "trapezium":
            g = float(input("Enter the length of its parallel side - "))
            i = float(input("Enter the length of its other parallel side - "))
            j = float(input("Enter the perpendicular distance between them - "))

            print(f"The area of this trapezium is {(1 / 2) * (g + i) * j}")
    elif t.strip().lower() == "3d":  
           
        print("Options - Cube , Cuboid , Sphere , Hemisphere , Right circular Cylinder , Right circular Cone , Ring , Disc")
        
        q = input("Choose the shape/figure - ")   

        if q.strip().lower() == "cube" : 
            