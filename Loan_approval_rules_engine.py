print("~~~Loan Approval Rules Engine~~~")

name = input("Enter your name: ") # Making name input
ready = input(f"Hi {name}! Are you ready? Please answer with yes or no^^: ").lower().strip()

while ready != "yes" and ready != "no": # Input must be 'yes' or 'no'
    print("Please answer with yes or no^^")
    ready = input("Are you ready? ").lower().strip() 

if ready == "yes": # If the answer is 'yes', the program will run
    input("Press enter to start")

    while True:
        try:
            monthly_income = float(input("Please input your monthly income : ")) # Input monthly income
            if monthly_income >= 0: # If your monthly income is >= 0, you can continue 
                break
            while float(monthly_income) < 0: # You can't continue if your monthly income < 0
                monthly_income = float(input("Please input your monthly income : "))
        except ValueError:
            print("Input should be a number") # If the input is not a number, you can't continue
    input("Press enter to continue")

    while True:
        try:
            monthly_debt = float(input("Please input your monthly debt: ")) # Input monthly debt
            if monthly_debt >= 0 : # If your monthly debt >= 0, you can continue
                break
            while float(monthly_debt) < 0: # You can't continue if your monthly debt < 0
                monthly_debt = float(input("Please input your monthly debt: "))
        except ValueError:
            print("Input should be a number!") # If the input is not a number, you can't continue
    input("Press enter to continue")

    while True:
        try:
            loan = float(input("Enter loan: ")) # Input loan
            if loan > 0: # If the loan > 0, you can continue
                break
            while float(loan) <= 0 : # You can't continue if the loan <= 0,
                loan = float(input("Enter loan: "))
        except ValueError: 
            print("Input should be a number!") # If the input is not a number, you can't continue

    debt_ratio = monthly_debt / monthly_income * 100 # Calculating debt ratio 
    if debt_ratio > 40 and loan > (12*monthly_income): # If debt ratio more than 40 and loan more than your monthly income in a year, your loan is denied
        print("Loan denied! Debt ratio and loan amount too high.")
    elif loan > (12 * monthly_income): # If loan more than your monthly income in a year, your loan is denied
        print("Loan denied! Loan amount too high.")
    elif debt_ratio > 40: # If debt ratio more than 40, your lean is denied
        print("Loan denied! debt ratio too high.")
    else: 
        print("Loan approved!") # If your debt ratio is less than 40 and the loan is less than your monthly income in a year, your loan is approved

if ready == "no":
    print("Alright, good bye!") # If your answer is no, the program will ends.
