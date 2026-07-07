# My Personal Details
#(# means comment - Python ignores these lines)



my_name = "Ravi"
my_age = 36
my_current_salary = 105000
my_goal_salary = 200000
my_city = "Mumbai"
my_daughter = "My Princess"


print("Name", my_name)
print("Age", my_age)
print("City", my_city)
print("Current Salary", my_current_salary)
print("Goal Salary", my_goal_salary)
print("Fighting for", my_daughter)


# Salary Math

salary_gap = my_goal_salary - my_current_salary
months = 6
monthly_increase_needed = salary_gap / months

print("\n--- MY GOAL CALCULATOR --")
print("Salary gap: ₹", salary_gap)
print("months to achieve", months)
print("Monthly increase needed: ₹", monthly_increase_needed)

rent = 33600
mom = 10000
wife = 15000
outside_loans = 20000
insurance = 80000 / 12 # yearly divided by 12

total_expenses = rent + mom + wife + outside_loans + insurance
remaining = my_current_salary - total_expenses

print("\n--- MY MONTHLY BUDGET ---")
print("Rent: ₹", rent)
print("mom: ₹", mom)
print("Wife ₹", wife)
print("loans ₹", outside_loans)
print("insurance monthly: ₹", insurance)
print("Total expesnes ₹", total_expenses)
print("Remaining: ₹", remaining)


if remaining > 0:
    print("You have some savings possible")
else:
    print("Expenses exceed income - need salary increase urgently!")


      
