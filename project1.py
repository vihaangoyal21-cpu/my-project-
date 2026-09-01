while True : 
 t = input("Enter the type of figure you want(2D/3D) - ")
 if t.strip().lower() == "2d" : 
  a = input("Choose the shape/figure - ")
  if a.strip().lower() == "circle" : 
   r = float(input("Enter the radius of the circle - "))
   from math import pi  
   print(f"The circumference of this circle is {2*pi*r} and its area is {pi*(r**2)}")
 elif a.strip().lower() == "square" :
  b = float(input("Enter the length of the side - "))
  print(f"The perimeter of this square is {4*b} and its area is {b**2}")
 elif a.strip().lower() == "rectangle" :
  l = float(input("Enter the length of the rectangle - "))
  b = float(input("Enter the breadth of the rectangle - "))
  print(f"The perimeter of this rectangle is {2*(a + b)} and its area is {a*b}")
 elif a.strip().lower() == "triangle" :
  a = float(input("Enter the length of a side of the triangle - "))
  b = float(input("Enter the length of the other side of the triangle - "))
  c = float(input("Enter the length of another side of the triangle - "))
  s = (a + b + c)/2 
  Area = ((s(s-a)(s-b)(s-c)))**(1/2)
 if a==b and b==c :
     print(f"The area of this equilateral triangle is {Area}")
 elif a==b!=c or a!=b==c or a==c!=b : 
     print(f"The area of this isosceles triangle is {Area}")
 elif a!=b!=c : 
     print(f"The area of this scalene triangle is {Area}")