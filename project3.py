import random 
a = random.randint(1,100) 
b = int(input("I am guessing a number between 1 & 100 , try and guess it - "))

while True :
 if a > b : 
  b = int(input("Too low! Try again - "))

 elif a < b : 
  b = int(input("Too high! Try again - "))

 if a==b :
   break 
print("You got it !")
  
