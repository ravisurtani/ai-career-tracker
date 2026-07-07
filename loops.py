# Day 6 - Loops
#Making code work automatically!

# Loop through your skills
skills = ["Python", "LangChain", "Prompt Engineering", "Streamlit", "Fast API"]

print("--- MY AI ENGINEERING SKILLS ---")
for skill in skills:
    print("Learning:", skill)

#Loop with number

print("\n --- MY 6 MONTH JOURNEY ---")
for month in range(1,7):
    print(f"Month {month} - Working hard!")


    # Loop + IF/else together:

    print("\n --- MONTHLY PROGRESS CHECKED ---")

    for month in range(1, 7):
        if month == 1:
            print(f"Month{month}: Learning Python basics!")
        elif month == 2:
            print(f"Month{month}: Learning LLM and AI basics!")
        elif month == 3:
            print(f"Month {month}: Building RAG systems!")
        elif month == 4:
            print(f"Month {month}: Building real projects")
        elif month == 5:
            print(f"Month {month}: Deploying and applying for jobs!")
        elif month == 6:
            print(f"{month}: Got AI Engineer job! Goal achieved!")

# Loop through expenses
print("\n ---- EXPENSE BREAKDOWN --- ")
expense_names = ["Rent", "Mom", "Wife", "Loans", "Insurance"]
expense_amounts = [33600, 10000, 15000, 20000, 6667]

total = 0
for i in range(len(expense_names)):
    print(f"{expense_names[i]}: Rs{expense_amounts[i]}")
    total = total + expense_amounts[i]



print(f"\nTotal Expenses: Rs{total}")
print(f"Salary: RS105000")
print(f"Remaining: Rs{105000 - total}")

# How AI processes multiple questions!

print("\n ---- AI PROCESSOR ---- ")


questions = [
    "What is Python?",
    "What is LanChain?",
    "What is RAG?",
    "What is Prompt Engineering?",
    "What is Streamlit?"
]

answers = [
    "Python is a programming language used for AI",
    "LangChain is a framework for building AI apps",
    "RAG is Retrievel Augmented Generation - AI reads documents!",
    "Prompt Engineering is writing better instructions for AI!",
    "Streamlit is a tool to deploy AI apps easily!"
]

for i in range(len(questions)):
    print(f"\nQ: {questions[i]}")
    print(f"A: {answers[i]}")
    print("-" * 40)


