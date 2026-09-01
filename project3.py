import random 
while True :
  d = input("Choose difficulty(Easy/Medium/Hard) - ")
  if d.strip().lower() == "easy" :
   max = 50 
  elif d.strip().lower() == "medium" :
   max = 100
  elif d.strip().lower() == "hard" :
   max = 200
  a = random.randint(1,max) 
  b = int(input(f"I am guessing a number between 1 & {max} try and guess it - "))
  while True :
    if a > b : 
     b = int(input("Too low! Try again - "))

    elif a < b : 
      b = int(input("Too high! Try again - "))
 
    if a==b :
      break 
  print("You got it !")
  c = input("Do you want to try again ? - ")
  if c.strip().lower() == "no" :   
    break 


 
  
