expense = input("Enter expense name: ")
amount = float(input("Enter amount: "))

with open("expenses.txt", "a") as file:
    file.write(f"{expense}: {amount}\n")

print("Expense saved successfully!")
