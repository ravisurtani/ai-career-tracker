"""

PROJECT: AI CAREER TRACKER
AUTHOR: RAVI SURTANI
PURPOSE: Track journey from banking IT to AI Engineer
Date: Week 1 - Day 7
"""

print("=" * 50)
print(" RAVI'S AI ENGINEER CAREER TRACKER")
print("=" * 50)

#Personal Info

name = "Ravi Surtani"
current_role = "Major Incident Management"
current_company = "RBL Bank via Clover Infotech"
target_role = "AI Engineer"
city = "Mumbai"

print(f"\n Name: {name}")
print(f" Current Role: {current_role}")
print(f" Current Company: {current_company}")
print(f" Target Role: {target_role}")
print(f" City: {city}")

#Skilss progress tracker
print("\n" + "=" * 50)
print("SKILLS PROGRESS")
print("=" * 50)

skills = [" Python Basics", "Varibles & Logic", "Strings", "Lists", "Loops", "Mini  Project"]
status = ["Done", "Done", "Done" , "Done", "Done", "In Progress"]


for i in range(len(skills)):
    print(f"{i+1}, {skills[i]}, {status[i]}")

completed = status.count("Done")
total = len(skills)
percentage = (completed / total) * 100

print(f"\n Progress: {completed}/{total} skills completed")
print(f"Completion: {percentage:.1f}%")

# Financial Goal Tracker

print("\n" + "=" * 50)
print("FINANCIAL GOAL TRACKER")
print("=" * 50)

current_salary = 105000
goal_salary = 200000
gap = goal_salary - current_salary
months_remaining = 5 # since week 1 done, 5, months remaining in 6 months.

monthly_growth_needed = gap / months_remaining
print(f"Current Salary: Rs{current_salary}")
print(f"Goal Salary: Rs{goal_salary}")
print(f"Gap to cover: Rs{gap}")
print(f"Months Remaining: Rs{months_remaining}")
print(f"Required Growth: Rs{monthly_growth_needed:.0f} per month")


print("\n" + "=" * 50)
print("MOTIVATION MESSAGE")
print("=" * 50)

if percentage >= 80: 
    print("EXCELLENT! You completed Week 1 successfully!")
    print("You are building real skills for your daughter's future!")
else: 
    print("Keep going ! Every steps counts!")


print("\nNext Step: Day 8 - GitHub Setup!")
print("-" * 50)







