while True:
    d = input("Choose the type of Interest to be calculated (Simple/Compound) - ")

    if d.strip().lower() == "simple":
        print("For simple interest :- ")

        R = float(input("Enter the rate of interest per annum (in percentage) - "))
        T = float(input("Enter the Time period of interest (in annum) - "))
        P = float(input("Enter the Principal amount - "))

        SI = P * T * R / 100

        print(f"The simple interest gained will be {SI} over the given period of time")
        print(f"The total amount will be {SI + P} at the end of the given time period")

    elif d.strip().lower() == "compound":
        print("For compound interest - ")

        R = float(input("Enter the rate of interest per annum (in percentage) - "))
        T = float(input("Enter the Time period of interest (in annum) - "))
        P = float(input("Enter the Principal amount - "))
        n = int(input("Enter the amount of times interest is compounded annually - "))

        CI = P * ((1 + R / (100 * n)) ** (n * T)) - P
        A = P * ((1 + R / (100 * n)) ** (n * T))

        print(f"The compound interest gained will be {CI} over the given period of time")
        print(f"The total amount will be {A} at the end of the given time period")

    k = input("Do you want to continue (Yes/No) - ")

    if k.strip().lower() == "no":
        break