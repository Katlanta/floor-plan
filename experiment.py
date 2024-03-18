# Prompt the user to input the unedited dataset
print("Paste the unedited dataset below:")
unedited_data = input()

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
print("Edited dataset:")
print(edited_data)