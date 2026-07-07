name = "Ravi Surtani"
city = "Mumbai"
job_now = "Incident Management"
job_goal = "AI Engineer"
company_now = "RBL Bank via Clover Infotech"
company_goal = "Top Tech Company"

print("Name", name)
print("city", city)
print("Current Job", job_now)
print("Dream Job", job_goal)
print("Currently at", company_now)
print("Going To", company_goal)


print("\n ---- STRING SUPERPOWER ---- ")
print(name.upper())
print(name.lower())
print("Name has", len(name), "letters")
old_job = job_now.replace("Incident Management", "AI Engineering")
print("Upgrading from", job_now, "to", old_job)
if "Mumbai" in city:
    print("Yes! Ravi lives in Mumbai")

full_intro = "My name is " + name + " and I live in " + city
print(full_intro)


better_intro = f"My name is {name}. I am an {job_goal} in {city}!"
print(better_intro)

