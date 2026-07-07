# Day 5 - Lists
# Ravi's AI Engineering Jorney

# A list stores multiple items together

skills_to_learn = ["Python", "Langchain", "RAG", "Prompt Engineering", "Streamlit"]
companies_to_apply = ["Razorpay", "Groww", "JP Morgan Tech", "Citi Tech", "Smallcase"]
monthly_expenses = [33600, 10000, 15000, 20000, 6667]

#Print full lists
print("Skills to Learn", skills_to_learn)
print('Target companies:', companies_to_apply)
print("Monthly expenses:", monthly_expenses)


# Print single items

print("\n--- SINGLE ITEMS ---")

print("First skill", skills_to_learn[0])
print("Second skill:", skills_to_learn[1])
print("Second Skill:", skills_to_learn[2])
print("Dream company:", companies_to_apply[0])
print("Rent amount: Rs", monthly_expenses[0])


# List Superpowers!

print("\n --- LIST SUPERPOWERS ---")

#1. How many items in list 
print("Total skills to learn", len(skills_to_learn))

# 2. Add new skkill
skills_to_learn.append("FastAPI")
print("After adding Fast API:", skills_to_learn)

# 3. Remove an item
companies_to_apply.remove("Smallcase")
print("Updatd companies:", companies_to_apply)


# 4. Check if item exists
if "Python" in skills_to_learn:
    print("Yes! Python is in your learning list!")

# 5. Total expenses
total = sum(monthly_expenses)
print(f"Total monthly expenses: Rs{total}")

# 6. Most expensive item
print(f"Biggest expense: Rs{max(monthly_expenses)}")

# 7. Last item in list
print("Last skill to learn:", skills_to_learn[-1])


# How AI Chatbots use lists!
print("\n --- AI CHATBOT MEMORY --- ")
# This is exactly how Chat GPT/Claude stores conversations!

conversation =[]

# User asks something
conversation.append("User: What is Langchain?")

# Ai responds
conversation.append("AI: LangChain is a framework for building AI applications!")

# User asks again
conversation.append("User: How do I learn it?")

# Ai responds again
conversation.append("AI: Start with Python basics, then LangChain documentation!")

#Print full conversation
print("Full conversation history:")
for message in conversation:
    print(message)

print(f"\n Total message in conversation: {len(conversation)}")
print("Latest message!:", conversation[-1])

