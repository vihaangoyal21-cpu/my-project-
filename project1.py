from math import pi

while True:

    t = input("Enter the type of figure you want (2D/3D) - ")

    if t.strip().lower() == "2d":
     
         while True : 
        
          print("Options - Circle , Square , Rectangle , Parallelogram , Triangle , Trapezium")
        
          a = input("Choose the shape/figure - ")

          if a.strip().lower() == "circle":
            
            r = float(input("Enter the radius of the circle - "))
            
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

          Condition1 = input("Do you want to continue with 2D figures(Yes/No) - ")
          if Condition1.strip().lower() == "no" : 
           break 

    elif t.strip().lower() == "3d":  
      
         while True : 
           
          print("Options - Cube , Cuboid , Sphere , Hemisphere , Right circular Cylinder , Right circular Cone , Torus(Donut shape) , Disc")
    
          q = input("Choose the shape/figure - ")   

          if q.strip().lower() == "cube" : 
            
            m = float(input("Enter the length of the cube's side - "))
            
            print(f"The lateral and total surface area of this cube is {4*(m**2)} and {6*(m**2)} and the volume is {m**3}")
            
          elif q.strip().lower() == "cuboid" :
           n = float(input("Enter the length of the cuboid - "))
           o = float(input("Enter the breadth of the cuboid - "))
           p = float(input("Enter the height of the cuboid - "))
           
           print(f"The lateral and total surface area of this cuboid is {2*p*(n + o)} and *{2*(o*n + n*p + p*n)} and the volume is {n*o*p}") 

          elif q.strip().lower() == "sphere" :
            r = float(input("Enter the radius of the sphere - "))
            
            print(f"The total surface area of the sphere is {4*pi*(r**2)} and the volume is {(4/3)*pi*(r**3)}")
            
          elif q.strip().lower() == "hemisphere" :
            u = float(input("Enter the radius of the hemisphere - "))
            
            print(f"The curved and total surface area of this hemisphere is {2*pi*(r**2)} and {3*pi*(r**2)} and the volume is {(2/3)*pi*(r**3)}")
            
          elif q.strip().lower() == "rightcircularcylinder" or q.strip().lower() == "disc":
            v = float(input(f"Enter the height of the {q.strip().lower()} - "))
            w = float(input(f"Enter the radius of the {q.strip().lower()}- "))
            
            print(f"The curved and total surface area of this {q.strip().lower()} is {2*pi*v*w} and {2*pi*w*(v + w)} and the volume is {pi*(w**2)*v}")

          elif q.strip().lower() == "rightcircularcone" :
            x = float(input("Enter the height of the cone - "))
            y = float(input("Enter the radius of the cone - "))
            
            print(f"The curved and total surface area of the cone is {pi*y*((x**2) + (y**2))**(1/2)} and the volume is {(1/3)*pi*(y**2)*x}")

          elif q.strip().lower == "torus" : 
            R = float(input("Enter the major radius of the torus - "))
            rad = float(input("Enter the minor radius of the torus - "))
            
            print(f"The total surface area of this torus is {4*(pi**2)*R*rad} and the volume is {2*(pi**2)*R*(rad**2)}")

          Condition2 = input("Do you want to continue with 3D figures(Yes/No) - ")
          if Condition2.strip().lower() == "no" :
           break

    Condition3 = input("Do you want to continue(Yes/No) - ")    
    if Condition3.strip().lower() == "no" : 
     break
