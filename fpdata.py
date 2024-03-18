# Provided data
#data = """
#Shift Manager Shift Break Macpherson, Joe 16:00 - 01:00 20:00 Ambrosimov, Mihaela 11:00 - 19:00 13:00 Kiosk Coach/Orders Shift Break Kinza, Kinza 22:00 - 06:00 01:30 Smith, Kye 05:00 - 13:00 06:30 Swan, Angel 12:00 - 20:00 14:00 Lochhead, Roan 16:30 - 21:30 17:45 Kinza, Kinza 22:00 - 06:00 01:30 Collect (IS) Shift Break Customer Experience Leader Shift Break Paterson, Debbie 06:00 - 14:00 09:45 Barron, Debbie 09:45 - 14:15 11:30 Smith, Tenny 14:00 - 22:00 16:15 Dining Area Shift Break Maleszyk, Sebastian 15:00 - 23:00 17:00 Show shifts in these dayparts Overnight Breakfast Day Evening Positions as of 00:00 Orders (DT) Shift Break Choubey, Varun 23:00 - 06:00 02:15 Hamilton, Josh 06:00 - 14:00 11:45 Logunleko, Maryam 11:30 - 19:30 13:45 Masson, Kenzie 16:00 - 21:00 17:00 Gomes, Toswel 23:00 - 06:00 02:15 Collect (DT) Shift Break Martin, Charles 21:00 - 05:00 23:15 Smith, Ruairidh 14:00 - 22:00 17:30 Milne, Aimee-louise 16:30 - 21:30 19:30 Kwao, Patrick 21:00 - 05:00 23:15 Drinks Shift Break Francis, Gideon 09:30 - 14:30 10:30 Fries Shift Break Colville, Shannon 12:00 - 20:00 14:45 Batch Cooker Shift Break Kolawole, Ajoke 22:00 - 05:00 03:00 Fernandes, Natalie 06:00 - 14:00 08:00 Donocik, Oliwier 11:30 - 19:30 15:45 Kuriakose, Gheevarghese P 22:00 - 05:00 03:00 Eggs Shift Break Rutkowska, Aldona 06:30 - 13:30 09:00 Sausage Shift Break Fernandes, Domnick 05:00 - 14:00 09:00 Thottan, Joe 07:00 - 15:00 10:15 Meal/break(g) Shift Break Third, Chloe 22:00 - 06:00 00:00 Tempering & Prep Shift Break Itteera, Naji 09:00 - 17:00 11:15 Kolenchery Varkey, Alex 17:00 - 22:00 19:00 BOP Shift Break Assembler Shift Break Kwao, Patrick 22:00 - 06:00 00:45 Cowling, Robbie 11:00 - 19:00 13:15 Boyd, Lewis 11:45 - 19:45 15:30 Beattie, Cameron 14:00 - 21:00 16:15 Melvin, Corey 16:00 - 23:00 20:00 Martin, Charles 22:00 - 06:00 00:45 Support Shift Break Basha, Assim 00:00 - 08:00 02:00 Cadger, Scott 00:00 - 08:00 02:00 Davidson, Fraser 05:00 - 14:00 08:30 Smith, Norman 06:00 - 14:00 11:00 Sinclair, Struan 06:00 - 14:00 11:15 Tait, Callum 08:00 - 16:00 11:00 Graham, Rosie 08:00 - 16:00 10:15 Chung, Kalib 09:00 - 17:00 12:45 Kounelis, Katia 09:00 - 17:00 12:45 Kennedy, Jack 15:00 - 23:00 18:00 Lumsden, Glen 15:00 - 23:00 18:45 Third, Chloe 22:00 - 06:00 00:00 No Activity Allocation Shift Break Okanta, Julius 23:00 - 06:00 02:30 Mikruta, Anna 07:00 - 14:00 11:30 Ross, Jacob 15:00 - 23:00 18:15 Martin, Sommer 16:00 - 22:00 17:00 Campbell, Taylor 17:00 - 22:00 18:45 Dougan, Kieran 17:00 - 00:00 19:30
#"""

# Words/phrases to remove
#remove_words = [
#    "Shift Manager", "Shift Break", "Kiosk Coach/Orders Shift Break", "Collect (IS)",
#    "Customer Experience Leader", "Dining Area", "Show shifts in these dayparts",
#    "Overnight", "Breakfast", "Day", "Evening", "Positions as of 00:00", "Orders (DT)",
#   "Collect (DT)", "Drinks", "Batch Cooker", "Eggs", "Meal/break(g)", "Tempering & Prep",
#    "BOP", "Assembler", "Support"
#]

# Remove specified words/phrases
#for word in remove_words:
#    data = data.replace(word, "")

# Splitting lines and reformatting
#lines = data.split('\n')
#formatted_lines = []
#for line in lines:
#    words = line.split()
#    for i in range(0, len(words), 3):
#        name = ' '.join(words[i:i+2])
#        time_ranges = ' '.join(words[i+2:i+3])
#        # Fixing the format of time ranges
#        time_ranges = time_ranges.split()
#        if len(time_ranges) >= 3:  # Ensure enough elements in time_ranges
#            time_range = f"{time_ranges[0]} {time_ranges[1]} - {time_ranges[2]}"
#            formatted_line = f"{name} {time_range}"
#            formatted_lines.append(formatted_line)

# Joining the lines back
#formatted_data = '\n'.join(formatted_lines)
#
# Print the modified data
#print(formatted_data)

# Unedited dataset
# Unedited dataset
unedited_data = """
Shift Manager	Shift	Break
Kennedy, Jack	15:00 - 23:00	
18:00
Kiosk Coach/Orders	Shift	Break
Ambrosimov, Mihaela	11:00 - 19:00	
13:00
Swan, Angel	12:00 - 20:00	
14:00
Lochhead, Roan	16:30 - 21:30	
17:45
Collect (IS)	Shift	Break
Customer Experience Leader	Shift	Break
Smith, Tenny	14:00 - 22:00	
16:15
Dining Area	Shift	Break
Show shifts in these dayparts
Overnight	Breakfast	Day	Evening
Positions as of
17:00
Orders (DT)	Shift	Break
Logunleko, Maryam	11:30 - 19:30	
13:45
Collect (DT)	Shift	Break
Milne, Aimee-louise	16:30 - 21:30	
19:30
Drinks	Shift	Break
Fries	Shift	Break
Donocik, Oliwier	11:30 - 19:30	
15:45
Batch Cooker	Shift	Break
Colville, Shannon	12:00 - 20:00	
14:45
Ross, Jacob	15:00 - 23:00	
18:15
Eggs	Shift	Break
Sausage	Shift	Break
Meal/break(g)	Shift	Break
Maleszyk, Sebastian	15:00 - 23:00	
17:00
Masson, Kenzie	16:00 - 21:00	
17:00
Martin, Sommer	16:00 - 22:00	
17:00
Tempering & Prep	Shift	Break
Kolenchery Varkey, Alex	17:00 - 22:00	
19:00
BOP	Shift	Break
Assembler	Shift	Break
Cowling, Robbie	11:00 - 19:00	
13:15
Boyd, Lewis	11:45 - 19:45	
15:30
Beattie, Cameron	14:00 - 21:00	
16:15
Melvin, Corey	16:00 - 23:00	
20:00
Support	Shift	Break
Lumsden, Glen	15:00 - 23:00	
18:45
No Activity Allocation	Shift	Break
Smith, Ruairidh	14:00 - 22:00	
17:30
Campbell, Taylor	17:00 - 22:00	
18:45
Dougan, Kieran	17:00 - 00:00	
19:30
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
                                           "BOP", "Assembler", "Support", "No Activity Allocation"]):
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