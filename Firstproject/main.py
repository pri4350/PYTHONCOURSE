#Expense Tracker Project #IG
expensesList = [] #List of all expenses in from of dictionary
print("Welcome to Expense Tracker : Khrcha Kam KIya Karo ")

while True:
    print("====MENU===")
    print("1.Add Expense")
    print("2.View All Expenses")
    print("3.View Total Expenses")
    print("4.Exit")

    choice = int(input("Please Enter Your choice:"))
    #ADD Expense
    if choice == 1:
        date = input("Enter the date of the expense: ")
        category = input("Enter the category (Food, Travel, Makeup, Books): ")
        description = input("Enter a description/details: ")
        amount = float(input("Enter the amount: " ))

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
            print("No Expenses Added. Please add an expense First.")
        else:
            print("==== Here are all your expenses ====")
            count = 1
            for eachkharcha in expensesList:
                print(f'Expense Number{count} -> {eachkharcha["date"]}, {eachkharcha["category"]}, {eachkharcha["description"]}, {eachkharcha["amount"]}')
                count = count + 1

    #3. View TOTAL SPENDING
    elif choice == 3:
        total = 0
        for eachkharcha in expensesList:
            total = total + eachkharcha["amount"]

        print("\n TOTAL EXPENSES = ", total)

    #4.EXIT
    elif choice == 4:
        print("Thank you for using Expense Tracker. Have a nice day!")
        break

    else:
        print("INVALID CHOICE. TRY AGAIN")
