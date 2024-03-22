import json

# Function to extract crew members from the 'crewlist.txt' file
def extract_crew_members(file_path):
    crew_members = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            if len(parts) >= 2:
                name = parts[0].strip()
                title = parts[1].strip()
                stations = [station.strip() for station in parts[2:]] if len(parts) > 2 else []
                crew_members[name] = {'title': title, 'stations': stations}
    return crew_members

# Load crew members from the 'crewlist.txt' file
crew_members = extract_crew_members('crewlist.txt')
print("Crew Members from 'crewlist.txt':", crew_members)

# Load extracted employee information from the 'employee_info.json' file
with open('employee_info.json', 'r') as file:
    employees_info = json.load(file)
print("Employee Information from 'employee_info.json':", employees_info)

# Find crew members in common between both files
common_crew_members = {}
for employee_info in employees_info:
    name = f"{employee_info['first_name']} {employee_info['last_name']}"
    shift_time = f"{employee_info['shift_time']}"
    if name in crew_members:
        common_crew_members[name] = {
            'title': crew_members[name]['title'],
            'stations': crew_members[name]['stations'],
            'shift_time': shift_time
        }

print("Common Crew Members:", common_crew_members)

# Save common crew members and their information into a JSON file
with open('common_crew_members.json', 'w') as file:
    json.dump(common_crew_members, file, indent=4)

# Print common crew members and their information
for name, info in common_crew_members.items():
    print(f"Name: {name}, Title: {info['title']}, Stations: {', '.join(info['stations']) if info['stations'] else 'None'}, Shift Time: {info['shift_time']}")