#Code to create a floorplan making tool

class Staff:
    allowed_stations = ["W1", "OAT", "KITCHEN", "W2", "FRIES", "DA", "MAINT", "BEV"]

    def __init__(self, name, title, shift_time, *stations):
        self.name = name
        self.title = title if title in self.allowed_titles else "Crew"  # Default to "Crew" if title is invalid
        self.shift_time = shift_time

# Define station requirements
station_requirements = {
    "KITCHEN":12,
    "W1": 2,
    "W2": 2,
    "OAT": 12,
    "FRIES": 1,
    "BEV": 2,
    "DA": 1,
    "MAINT": 1
}

# Create instances of Staff class for each staff member
staff_members = []

# Create a dictionary to store station assignments
station_assignments = {station: [] for station in Staff.allowed_stations}

# Assign staff to stations based on requirements
for staff_member in staff_members:
    for station in staff_member.stations:
        if len(station_assignments[station]) < station_requirements.get(station, float('inf')):
            station_assignments[station].append((staff_member.name, staff_member.shift_time))
            break

# Output the stations and staff assignments
for station, assigned_staff in station_assignments.items():
    if assigned_staff:
        staff_info = [f"{name} ({title}) - Shift: {shift_time}" for name, title, shift_time in assigned_staff]
        print(f"At station {station}: {', '.join(staff_info)}")
    else:
        print(f"At station {station}: No staff assigned")


