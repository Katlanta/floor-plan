import json
from collections import defaultdict

class Staff:
    allowed_stations = ["W1", "OAT", "KITCHEN", "W2", "FRIES", "DA", "MAINT", "BEV"]
    allowed_titles = ["Crew Member", "Shift Manager","Crew Trainer"]  # Add more titles if needed

    def __init__(self, name, title, shift_time, stations):
        self.name = name
        self.title = title if title in self.allowed_titles else "Crew Member"  # Default to "Crew Member" if title is invalid
        self.shift_time = shift_time
        self.stations = stations

# Define station requirements
station_requirements = {
    "KITCHEN": 8,
    "W1": 2,
    "W2": 2,
    "OAT": 5,
    "FRIES": 1,
    "BEV": 2,
    "DA": 1,
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
