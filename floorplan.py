#Code to create a floorplan making tool

class Staff:
    allowed_stations = ["W1", "OAT", "KITCHEN", "W2", "FRIES", "DA", "MAINT", "BEV"]
    allowed_titles = ["Crew", "Crew Trainer", "Shift Manager"]

    def __init__(self, name, title, shift_time, *stations):
        self.name = name
        self.title = title if title in self.allowed_titles else "Crew"  # Default to "Crew" if title is invalid
        self.shift_time = shift_time
        self.stations = self.allowed_stations if self.title in ["Crew Trainer", "Shift Manager"] else []
        for station in stations:
            if station.upper() in self.allowed_stations:
                self.stations.append(station.upper())


# Define station requirements
station_requirements = {
    "W1": 2,
    "W2": 2,
    "OAT": 12,
    "FRIES": 1,
    "BEV": 2,
    "DA": 1,
    "MAINT": 1
}

# Create instances of Staff class for each staff member
staff_members = [
    Staff("Chloe", "Crew", "22:00 - 06:00", "W1"),
    Staff("Jess", "Shift Manager", "11:00 - 19:00", "KITCHEN", "BEV"),
    Staff("Mac", "Crew Trainer", "16:00 - 01:00", "W2", "BEV", "MAINT"),
    Staff("John", "Crew", "12:00 - 20:00", "W2", "FRIES"),
    Staff("Emma", "Crew", "15:00 - 23:00", "W2", "BEV"),
    Staff("Alex", "Shift Manager", "22:00 - 06:00", "BEV", "W2")
]

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
        print(f"At station {station}: No staff assigned")