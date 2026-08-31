print("For simple interest :- ")
R = float(input("Enter the rate of interest per annum(in percentage) - "))
T = float(input("Enter the Time period of interest(in annum) - "))
P = float(input("Enter the Principal amount - "))
SI = P*T*R/100 
print("The simple interest gained will be ", SI ,"over the given period of time")
print("The total amount will be ", SI + P ,"at the end of the given time period")
print("For compound interest - ")
n = int(input("Enter the amount of times interest is compounded annually -  "))
CI = P*((1 + R/(100*n))**(n*T)) - P 
A = P*((1 + R/(100*n))**(n*T))
print("The compound interest gained will be ", CI ,"over the given period of time")
print("The total amount will be ", A ,"at the end of the given time period")

