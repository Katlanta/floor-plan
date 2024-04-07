import json
from collections import defaultdict

def extract_employee_info(data):
    employees = []
    for line in data.split('\n'):
        if any(keyword not in line for keyword in ["Shift Manager", "Kiosk Coach/Orders", "Collect (IS)",
                                                   "Customer Experience Leader", "Dining Area",
                                                   "Show shifts in these dayparts", "Orders (DT)",
                                                   "Collect (DT)", "Drinks", "Fries", "Batch Cooker",
                                                   "Eggs", "Sausage", "Meal/break(g)", "Tempering & Prep",
                                                   "BOP", "Assembler", "Support", "No Activity Allocation",
                                                   "Overnight", "Breakfast"]):
            parts = line.split('\t')
            if len(parts) >= 2:
                name_parts = parts[0].split(', ')
                if len(name_parts) == 2:
                    last_name = name_parts[0].strip()
                    first_name = name_parts[1].strip()
                    shift_time = parts[1].strip()
                    employees.append({'first_name': first_name, 'last_name': last_name, 'shift_time': shift_time})
    return employees

unedited_data = """
    Shift Manager	Shift	Break
Kiosk Coach/Orders	Shift	Break
West, Lewis	12:00 - 20:00	
14:00
Collect (IS)	Shift	Break
Fernandes, Natalie	07:30 - 14:30	
09:30
Customer Experience Leader	Shift	Break
Paterson, Debbie	06:00 - 14:00	
09:45
Dining Area	Shift	Break
Show shifts in these dayparts
Overnight	Breakfast	Day	Evening
Positions as of
13:00
Orders (DT)	Shift	Break
Milne, Aimee	11:30 - 19:30	
13:45
Colville, Shannon	12:00 - 20:00	
14:30
Collect (DT)	Shift	Break
Melvin, Corey	06:00 - 14:00	
09:45
Cowling, Robbie	07:00 - 15:00	
09:45
Drinks	Shift	Break
Mikruta, Anna	08:00 - 14:00	
09:30
Fries	Shift	Break
Earp, Daniel	09:00 - 16:00	
13:15
Batch Cooker	Shift	Break
Swan, Angel	06:00 - 14:00	
08:00
Donocik, Oliwier	11:30 - 19:30	
15:45
Eggs	Shift	Break
Costa, Nikita	06:30 - 13:30	
09:00
Sausage	Shift	Break
Meal/break(g)	Shift	Break
Smith, Tenny	09:00 - 17:00	
12:45
Gray, Stewart	09:30 - 16:30	
12:45
Smith, Ruairidh	11:00 - 19:00	
13:00
Tempering & Prep	Shift	Break
Itteera, Naji	09:00 - 17:00	
11:15
BOP	Shift	Break
Assembler	Shift	Break
Fernandes, Domnick	05:00 - 14:00	
09:00
Ambrosimov, Mihaela	05:00 - 14:00	
08:30
Sinclair, Struan	06:00 - 14:00	
11:15
Singh, Kumari	11:00 - 19:00	
13:15
Support	Shift	Break
Smith, Norman	06:00 - 14:00	
11:00
Anderson, Jordan	06:00 - 14:00	
09:45
Nastase, Ana-Maria	11:00 - 19:00	
14:45
Tay, Isabella	11:00 - 19:00	
14:45
No Activity Allocation	Shift	Break
Hamilton, Josh	11:00 - 19:00	
13:45
"""

# Extract employee information
employees_info = extract_employee_info(unedited_data)

# Save extracted information into a JSON file
with open('employee_info.json', 'w') as file:
    json.dump(employees_info, file, indent=4)


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


# Load extracted employee information from the 'employee_info.json' file
with open('employee_info.json', 'r') as file:
    employees_info = json.load(file)


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



# Save common crew members and their information into a JSON file
with open('common_crew_members.json', 'w') as file:
    json.dump(common_crew_members, file, indent=4)

# Print common crew members and their information



class Staff:
    allowed_stations = ["W1", "OAT", "KITCHEN", "W2", "FRIES", "DA", "MAINT", "BEV"]
    allowed_titles = ["Crew Member", "Shift Manager","Crew Trainer","Support", "Customer Care"]  # Add more titles if needed

    def __init__(self, name, title, shift_time, stations):
        self.name = name
        self.title = title if title in self.allowed_titles else "Crew Member"  # Default to "Crew Member" if title is invalid
        self.shift_time = shift_time
        self.stations = stations

# Define station requirements
station_requirements = {
    "KITCHEN": 8,
    "W1": 1,
    "W2": 2,
    "OAT": 5,
    "FRIES": 1,
    "BEV": 1,
    "DA": 3,
    "MAINT": 1
}

# Load common crew members from the JSON file
with open('common_crew_members.json', 'r') as file:
    common_crew_members = json.load(file)

# Create instances of Staff class for each crew member
staff_members = [Staff(name, info['title'], info['shift_time'], info['stations']) for name, info in common_crew_members.items()]

# Create a dictionary to store station assignments
station_assignments = defaultdict(list)

# Assign staff to stations based on requirements
for staff_member in staff_members:
    assigned = False
    for station in staff_member.stations:
        if len(station_assignments[station]) < station_requirements.get(station, float('inf')):
            station_assignments[station].append((staff_member.name, staff_member.title, staff_member.shift_time))
            assigned = True
            break
    if not assigned:
        station_assignments['Unassigned'].append((staff_member.name, staff_member.title, staff_member.shift_time))

# Output the stations and staff assignments
for station, assigned_staff in station_assignments.items():
    if assigned_staff:
        staff_info = [f"{name} ({title}) - Shift: {shift_time}" for name, title, shift_time in assigned_staff]
        print(f"At station {station}: {', '.join(staff_info)}")
    else:
        print(f"At station {station}: No staff assigned")
