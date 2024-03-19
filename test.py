# Unedited dataset
unedited_data = """
    Shift Manager	Shift	Break
Healey, Daniel	08:00 - 16:00	
11:00
Kiosk Coach/Orders	Shift	Break
Itteera, Naji	11:00 - 19:00	
13:00
Colville, Shannon	12:00 - 20:00	
14:00
Collect (IS)	Shift	Break
Customer Experience Leader	Shift	Break
Paterson, Debbie	06:00 - 14:00	
09:45
Dining Area	Shift	Break
Barron, Debbie	09:45 - 14:15	
11:30
Show shifts in these dayparts
Overnight	Breakfast	Day	Evening
Positions as of
12:00
Orders (DT)	Shift	Break
Costa, Nikita	08:00 - 14:00	
11:00
Collect (DT)	Shift	Break
Walker, Murray	11:45 - 19:45	
14:45
Drinks	Shift	Break
Trufin, Robert	07:30 - 14:30	
10:30
Fries	Shift	Break
Trufin, Mihaela	07:00 - 15:00	
09:45
Batch Cooker	Shift	Break
Fernandes, Natalie	06:00 - 14:00	
08:00
Eggs	Shift	Break
Rutkowska, Aldona	06:30 - 13:30	
09:00
Sausage	Shift	Break
Meal/break(g)	Shift	Break
Hamilton, Josh	10:00 - 18:00	
11:45
Tempering & Prep	Shift	Break
BOP	Shift	Break
Assembler	Shift	Break
Fernandes, Domnick	05:00 - 14:00	
09:00
Davidson, Fraser	05:00 - 14:00	
08:30
Ambrosimov, Mihaela	08:00 - 16:00	
11:15
Kolenchery Varkey, Alex	11:30 - 19:30	
15:15
Support	Shift	Break
Smith, Norman	06:00 - 14:00	
11:00
Graham, Rosie	08:00 - 16:00	
12:45
Chung, Kalib	09:00 - 17:00	
12:45
MacNicol, Blair	11:00 - 19:00	
14:45
Kounelis, Katia	11:00 - 19:00	
14:45
No Activity Allocation	Shift	Break
pires, meefa	06:00 - 14:00	
09:45
Francis, Gideon	09:30 - 14:30	
11:30
Cowling, Robbie	11:00 - 19:00	
14:45
Purushu, Amal	11:30 - 19:30	
13:45
    """

# Split the data into lines
lines = unedited_data.strip().split('\n')

# Initialize an empty list to store the edited lines
edited_lines = []

# Iterate through each line
for line in lines:
    # Skip lines containing unnecessary information
    if any(keyword in line for keyword in ["Shift Manager", "Kiosk Coach/Orders", "Collect (IS)",
                                           "Customer Experience Leader", "Dining Area",
                                           "Show shifts in these dayparts", "Orders (DT)",
                                           "Collect (DT)", "Drinks", "Fries", "Batch Cooker",
                                           "Eggs", "Sausage", "Meal/break(g)", "Tempering & Prep",
                                           "BOP", "Assembler", "Support", "No Activity Allocation",
                                           "Overnight", "Breakfast"
                                           ]):
        continue

    # Extract name and time range
    parts = line.split('\t')

    # Ensure parts contain at least 2 elements
    if len(parts) >= 2:
        name_parts = parts[0].split(', ')
        if len(name_parts) == 2:
            last_name = name_parts[0].strip()
            first_name = name_parts[1].strip()
            shift_time = parts[1].strip()

            # Format the edited line
            edited_line = f"Name: {first_name} {last_name} Shift Time: {shift_time}"

            # Append the edited line to the list
            edited_lines.append(edited_line)
        else:
            print("Skipping line:", line)

# Print the edited lines
for line in edited_lines:
    print(line)


#Create "ALL" for stations, similar to managers but for crew. Will be important when manager specific roles get introduced.