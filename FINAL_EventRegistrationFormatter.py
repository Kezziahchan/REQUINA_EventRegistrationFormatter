
# Version 3: Student Event Registration Formatter

from datetime import datetime

# Ask for student information
print("=== Student Event Registration ===")

first_name = input("Enter student first name: ").strip()
last_name = input("Enter student last name: ").strip()
section = input("Enter section: ").strip()

# Ask for event information
event_name = input("Enter event name: ").strip()

year = int(input("Enter event year: "))
month = int(input("Enter event month: "))
day = int(input("Enter event day: "))

# Format student information
full_name = (first_name + " " + last_name).title()
name_code = full_name.upper()
formatted_section = section.upper()
formatted_event = event_name.title()

# Format event date
event_date = datetime(year, month, day)

formatted_date = (
    f"{event_date.strftime('%B')} "
    f"{event_date.day}, {event_date.year}"
)

# Display registration summary
print("\n=== Student Event Registration Summary ===")
print("Name:", full_name)
print("Name Code:", name_code)
print("Section:", formatted_section)
print("Event:", formatted_event)
print("Event Date:", formatted_date)
print("Language Used: Python")
print("String Feature Used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime")
print("Registration record created successfully.")
