expenses = [10.50, 8, 5, 15, 20, 5, 3]
# sum() iterates for us
total = sum(expenses)

# "string", variable replaces "string" + str(variable)
# sep='' empty string replaces separations
print("You spent $", total, " on lunch this week.", sep='')

# becomes

total = 0
expenses = []
for i in range(7):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep='')

# what if our number of expenses changes?
total = 0
expenses = []
num_expenses = int(input("Enter # of expenses:"))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expense:")))

total = sum(expenses)

print("You spent $", total, sep='')