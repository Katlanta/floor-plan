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
Third, Chloe	15:00 - 22:15	
18:00
Kiosk Coach/Orders	Shift	Break
Ambrosimov, Mihaela	11:00 - 19:00	
13:00
Dimitrova, Evgenia	12:00 - 20:00	
14:00
Jolly, Mackenzie	16:30 - 21:30	
17:45
Izuka, Chisom	22:00 - 06:00	
01:30
Collect (IS)	Shift	Break
Hebenton, Ashton	16:00 - 22:00	
19:15
West, Lewis	16:00 - 22:00	
19:15
Trufin, Mihaela	17:00 - 22:00	
18:45
Morrice, Kayden	17:30 - 23:00	
21:00
Customer Experience Leader	Shift	Break
Milne, Aimee-louise	14:00 - 22:00	
16:15
Dining Area	Shift	Break
Smith, Tenny	11:45 - 19:45	
15:30
Show shifts in these dayparts
Overnight	Breakfast	Day	Evening
Positions as of
17:00
Orders (DT)	Shift	Break
Donocik, Oliwier	11:30 - 19:30	
13:45
Fyvie, David	23:00 - 06:00	
02:15
Collect (DT)	Shift	Break
Richardson, Amy	16:30 - 22:00	
20:15
Okanta, Julius	21:00 - 05:00	
23:15
Drinks	Shift	Break
Pirie, Keira	17:00 - 22:00	
18:15
Cowie, Liam	18:00 - 22:00	
19:15
Silva, Richard	22:00 - 06:00	
02:15
Adurojaiye, David	23:00 - 06:00	
03:00
Fries	Shift	Break
Gray, Stewart	09:00 - 17:00	
11:30
Yule, Zack	16:30 - 22:00	
19:15
Bain, Finlay	17:00 - 22:00	
19:30
Batch Cooker	Shift	Break
Sinclair, Struan	11:30 - 19:30	
14:45
Tay, Isabella	17:00 - 00:00	
20:15
Nastase, Ana-Maria	22:00 - 05:00	
03:00
Eggs	Shift	Break
Sausage	Shift	Break
Meal/break(g)	Shift	Break
Healey, Daniel	12:00 - 20:00	
16:30
Adurojaiye, Sefia	15:00 - 23:00	
17:00
Martin, Sommer	16:00 - 21:00	
17:00
Tempering & Prep	Shift	Break
Logunleko, Abdulbarr	09:00 - 17:00	
11:15
Trufin, Robert	17:00 - 22:00	
19:00
BOP	Shift	Break
Assembler	Shift	Break
Harkess, Dana	11:00 - 19:00	
13:15
Walker, Murray	11:45 - 19:45	
15:45
Tait, Callum	14:00 - 21:00	
16:15
Bell, Louis	16:00 - 01:00	
20:00
Graham, Rosie	22:00 - 06:00	
00:45
Sinclair, Tyler	22:00 - 06:00	
01:30
Support	Shift	Break
Chung, Kalib	22:00 - 06:00	
00:00
No Activity Allocation	Shift	Break
Dyce, James	11:00 - 20:00	
13:45
Colville, Shannon	15:00 - 23:00	
17:30
Dempster, Callum	16:30 - 21:30	
18:30
Roszkiewicz, Ariel	18:00 - 00:00	
20:00
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
