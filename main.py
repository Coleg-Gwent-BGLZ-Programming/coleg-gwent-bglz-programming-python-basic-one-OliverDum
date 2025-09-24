name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = 2025
birth_year = current_year - age
year_info = (birth_year, current_year)

hobbies = set()
print("Enter hobbies (type 'done' to finish):")
while True:
    hobby = input("Hobby: ")
    if hobby.lower() == "done":
        break
    hobbies.add(hobby)

user_data = {
    "Name": name,
    "Age": age,
    "Hobbies": list(hobbies),
    "Year Info": year_info
}

print(f"\nHello {user_data['Name']}, age {user_data['Age']}.")
print(f"Born in {user_data['Year Info'][0]}, current year {user_data['Year Info'][1]}.")
print("Hobbies:", ", ".join(user_data["Hobbies"]))
