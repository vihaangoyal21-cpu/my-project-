while True : 
 a = int(input("Please enter the number - "))
 b = int(input("Please enter the number with which you want to check the divisibility - "))

 if b==0 :
  print("You cannot check the divisibilty by 0")
 elif a % b == 0 :
  print(f"The given number is divisble by {b}")
 else :
  print(f"The given number is not divisble by {b}")

 c = input("Do you want to continue - ")

 if c.strip().lower() == "no" :
  break 