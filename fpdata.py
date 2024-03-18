# Unedited dataset
unedited_data = """
Shift Manager	Shift	Break
Rolland, Megan	15:00 - 23:00	
18:00
Kiosk Coach/Orders	Shift	Break
Smith, Ruairidh	12:00 - 20:00	
14:00
Richardson, Amy	16:30 - 21:30	
17:45
Collect (IS)	Shift	Break
Customer Experience Leader	Shift	Break
Foster, Aimee	14:00 - 22:00	
16:15
Dining Area	Shift	Break
Show shifts in these dayparts
Overnight	Breakfast	Day	Evening
Positions as of
17:00
Orders (DT)	Shift	Break
MacGill, Kitty	11:30 - 19:30	
13:45
Collect (DT)	Shift	Break
Bell, Louis	14:00 - 22:00	
17:45
Robertson, Scott	17:00 - 00:00	
20:45
Drinks	Shift	Break
Ambrosimov, Mihaela	11:00 - 19:00	
13:45
Roszkiewicz, Ariel	17:00 - 22:00	
18:15
Fries	Shift	Break
Walker, Murray	11:45 - 19:45	
14:45
Batch Cooker	Shift	Break
Kennedy, Jack	11:30 - 19:30	
13:30
Cowling, Robbie	15:00 - 23:00	
18:45
Eggs	Shift	Break
Sausage	Shift	Break
Meal/break(g)	Shift	Break
Wielgosz, Jakub	15:00 - 23:00	
17:00
Logunleko, Abdulbarr	16:00 - 21:00	
17:00
Hutton, Nathan	16:00 - 22:00	
17:00
Tempering & Prep	Shift	Break
Davidson, Remy	17:00 - 22:00	
19:00
BOP	Shift	Break
Assembler	Shift	Break
Masson, Kenzie	11:00 - 19:00	
13:15
Purushu, Amal	14:00 - 21:00	
16:15
Dimitrova, Evgenia	16:00 - 01:00	
20:00
Carter, Jude	16:30 - 21:30	
18:30
Support	Shift	Break
Kounelis, Katia	14:00 - 22:00	
17:45
No Activity Allocation	Shift	Break
Colville, Shannon	12:00 - 20:00	
15:30
Earp, Daniel	17:00 - 22:00	
18:30
Morrice, Lana	17:00 - 22:00	
19:15
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
        name = parts[0].strip()
        time_range = parts[1].strip()
        
        # Format the edited line
        edited_line = f"{name}\t{time_range}"
        
        # Append the edited line to the list
        edited_lines.append(edited_line)
    else:
        print("Skipping line:", line)

# Join the edited lines with newline characters
edited_data = '\n'.join(edited_lines)

# Print the edited data

print(edited_data)

