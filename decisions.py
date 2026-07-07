# Day 4 - Decisions
# Making Code think Like AI

salary = 105000
goal_salary = 200000


if salary >= goal_salary:
    print(" Goal acheved! You are earning well")
else:
    gap = goal_salary - salary
    print(f"Not yet! you need ₹{gap} more per month")
    print("Keep learning AI Engineering!")



# Multiple decisions using elif statements

print("\n --- SKILL LEVEL CHECKER --- ")

months_studied = 1

if months_studied == 6:
    print("You are job ready!, start applying")

elif months_studied == 4:
    print("Almost there!, Build your projects!")
elif months_studied == 2:
    print("Good Progress!, keep going")
elif months_studied == 1:
    print("Just started! Stay consistent")
else:
    print("Keep studing everyday!")

print(f"\nYou are on month {months_studied} of 6!")
print("Everyday counts Ravi!")



# Real Life Decision Maker

print("\n ---- COURSE DECISION MAKER --- ")

#Change these to test different situation!

have_time = True
is_free_course = False
helps_job_switch = True

if have_time and is_free_course and helps_job_switch:
    print("YES! Take this course")

elif have_time and helps_job_switch:
    print("Consider it - but check if free version exists")

elif not have_time:
    print("No time right now - focus on current plan!")

else:
    print("Skip it! Stick to your AI Engineering path!")


print("\n---- EXPENSE DECISION MAKER ---")

expense_amount = 5000
is_necessary = True
have_savings = False


if is_necessary and have_savings:
    print(f"OK to spend, RS{expense_amount}")
elif is_necessary and not have_savings:
    print(f"Necessary but no savings - delay if possible")
elif not is_necessary:
    print(f"Skip spending RS{expense_amount} - not necessary right now!")
else:
    print("Think twice before spending!")

