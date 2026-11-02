print("~~~Loan Approval Rules Engine~~~")

name = input("Enter your name: ")
ready = input(f"Hi {name}! Are you ready? Please answer with yes or no^^: ").lower().strip()

while ready != "yes" and ready != "no":
    print("Please answer with yes or no^^")
    ready = input("Are you ready? ").lower().strip()

if ready == "yes":
    input("Press enter to start")

    while True:
        try:
            monthly_income = float(input("Please input your monthly income : "))
            if monthly_income >= 0:
                break
            while float(monthly_income) < 0:
                monthly_income = float(input("Please input your monthly income : "))
        except ValueError:
            print("Input harus berupa angka!")
    input("Tekan enter untuk lanjut")

    while True:
        try:
            monthly_debt = float(input("Please input your monthly debt: "))
            if monthly_debt >= 0 :
                break
            while float(monthly_debt) < 0:
                monthly_debt = float(input("Please input your monthly debt: "))
        except ValueError:
            print("Input harus berupa angka!")

    input("Tekan enter untuk lanjut")

    while True:
        try:
            loan = float(input("Enter loan: "))
            if loan > 0:
                break
            while float(loan) <= 0 :
                loan = float(input("Enter loan: "))
        except ValueError:
            print("Input harus berupa angka!")

    debt_ratio = monthly_debt / monthly_income * 100 
    if debt_ratio > 40 and loan > (12*monthly_income):
        print("Loan denied! Debt ratio and loan amount too high.")
    elif loan > (12 * monthly_income):
        print("Loan denied! Loan amount too high.")
    elif debt_ratio > 40:
        print("Loan denied! debt ratio too high.")
    else:
        print("Loan approved!")

if ready == "no":
    print("Alright, good bye!")