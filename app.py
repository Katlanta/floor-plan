"""# Import the Staff class from floorplan.py
from floorplan import Staff

# Import the function get_formatted_dataset from fpdata.py
from fpdata import get_formatted_dataset

# Define station requirements
station_requirements = {
    "KITCHEN": 12,
    "W1": 2,
    "W2": 2,
    "OAT": 12,
    "FRIES": 1,
    "BEV": 2,
    "DA": 1,
    "MAINT": 1
}

# Get the formatted dataset directly from fpdata.py
formatted_dataset = get_formatted_dataset()

# Create a list to store Staff objects
staff_members = []

# Parse each line of the dataset to create Staff objects
for line in formatted_dataset.split('\n'):
    parts = line.strip().split('\t')
    if len(parts) >= 2:
        name = parts[0]
        shift_time = parts[1]
        staff_members.append(Staff(name, "Crew", shift_time))  # Assuming title is always "Crew"
    else:
        print("Skipping line:", line)

# Create a dictionary to store station assignments
station_assignments = {station: [] for station in Staff.allowed_stations}

# Assign staff to stations based on requirements
for staff_member in staff_members:
    for station in staff_member.stations:
        if len(station_assignments[station]) < station_requirements.get(station, float('inf')):
            station_assignments[station].append((staff_member.name, staff_member.title, staff_member.shift_time))
            break

# Output the stations and staff assignments
for station, assigned_staff in station_assignments.items():
    if assigned_staff:
        staff_info = [f"{name} ({title}) - Shift: {shift_time}" for name, title, shift_time in assigned_staff]
        print(f"At station {station}: {', '.join(staff_info)}")
    else:
        print(f"At station {station}: No staff assigned")"""

