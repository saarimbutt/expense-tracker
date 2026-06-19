expenses = []

while True:
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount: "))

        expenses.append((name, amount))

        with open("expenses.txt", "a") as file:
            file.write(f"{name}: {amount}\n")

        print("Expense saved!")

    elif choice == "2":
        total = 0

        for name, amount in expenses:
            print(f"{name}: ${amount}")
            total += amount

        print(f"Total spent: ${total}")

    elif choice == "3":
        break
