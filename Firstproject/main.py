#Expense Tracker Project #IG
expensesList = [] #List of all expenses in from of dictionary
print("Welcome to Expense Tracker : Khrcha Kam KIya Karo ")

while True:
    print("====MENU===")
    print("1.Add Expense")
    print("2.View All Expenses")
    print("3.View Total Khrcha")
    print("4.Exit")

    choice = int(input("Please Enter Your choice:"))
    #ADD Expense
    if choice == 1:
        date = input("Kis Date par Khrcha Kiya tha?:")
        category = input("Kis type ka chrcha Kiya? (Food, Travel, Makeup, Books):")
        description = input("Aur detail dedo:")
        amount = float(input("Enter the amount:"))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expensesList.append(expense)
        print("\nDONE bro. Expense is added successfully")

    #2.View All EXPENSES
    elif choice == 2:
        if len(expensesList) == 0:
            print("No Expenses Added. Jao pehle Khrcha karo.")
        else:
            print("====Ye y aapka sara expense ====")
            count = 1
            for eachkharcha in expensesList:
                print(f'Kharcha Number{count} -> {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["description"]}, {eachkharcha["amount"]}')
                count = count + 1

    #3. View TOTAL SPENDING
    elif choice == 3:
        total = 0
        for eachkharcha in expensesList:
            total = total + eachkharcha["amount"]

        print("\n TOTAL KHRCHA = ", total)

    #4.EXIT
    elif choice == 4:
        print("Dhanyawad aapbe humara system use kiya")
        break

    else:
        print("INVAID CHOICE. TRY AGAIN")
