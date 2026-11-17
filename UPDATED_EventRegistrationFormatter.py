
# Version 2: Student Event Registration

# Ask for student information
first_name = input("Enter student first name: ").strip()
last_name = input("Enter student last name: ").strip()
section = input("Enter section: ").strip()

# Ask for event information
event_name = input("Enter event name: ").strip()
year = input("Enter event year: ")
month = input("Enter event month: ")
day = input("Enter event day: ")

# Format information
full_name = (first_name + " " + last_name).title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_event = event_name.title()

# Display formatted information
print("\nStudent Event Registration Summary")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Event:", formatted_event)
print("Year:", year)
print("Month:", month)
print("Day:", day)
