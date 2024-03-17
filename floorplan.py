#Code to create a floorplan making tool

class Staff:
    allowed_stations = ["W1", "OAT", "KITCHEN", "W2", "FRIES", "DA", "MAINT", "BEV"]

    def __init__(self, name, *stations):
        self.name = name
        self.stations = []
        for station in stations:
            if station.upper() in self.allowed_stations:
                self.stations.append(station.upper())


# Define station requirements
station_requirements = {
    "W1": 2,
    "W2": 2,
    "OAT":12,
    "FRIES": 1,
    "BEV": 2,
    "DA": 1,
    "MAINT":1

}

# Create instances of Staff class for each staff member
staff_members = [
    Staff("Chloe", "W1"),
    Staff("Jess", "KITCHEN", "BEV"),
    Staff("Mac", "W2", "BEV", "MAINT"),
    Staff("John", "W2", "FRIES"),
    Staff("Emma", "W2", "BEV"),
    Staff("Alex", "BEV", "W2")
]

# Create a dictionary to store station assignments
station_assignments = {station: [] for station in Staff.allowed_stations}

# Assign staff to stations based on requirements
for staff_member in staff_members:
    for station in staff_member.stations:
        if len(station_assignments[station]) < station_requirements.get(station, float('inf')):
            station_assignments[station].append(staff_member.name)
            break

# Output the stations and staff assignments
for station, assigned_staff in station_assignments.items():
    if assigned_staff:
        print(f"At station {station}: {', '.join(assigned_staff)}")
    else:
        print(f"At station {station}: No staff assigned")