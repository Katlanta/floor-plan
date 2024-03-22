
#Current best practice for cleaning the dataset (and storing it in a jason file)
#Using this file to compare to the original employee list to gather the data on who is working, their stations and titles.

import json

# Function to extract relevant information from unedited data
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
Rolland, Megan	15:00 - 23:00	
18:00
Kiosk Coach/Orders	Shift	Break
Bradeanu, Andreea	11:00 - 19:00	
13:00
Dougan, Kieran	12:00 - 20:00	
14:00
Chalmers, Max	16:30 - 21:30	
17:45
Collect (IS)	Shift	Break
Customer Experience Leader	Shift	Break
Hurnik, Mateusz	14:00 - 22:00	
16:15
Dining Area	Shift	Break
Show shifts in these dayparts
Overnight	Breakfast	Day	Evening
Positions as of
17:00
Orders (DT)	Shift	Break
Rudra, Priti	11:30 - 19:30	
13:45
Collect (DT)	Shift	Break
Meikle, Amy	12:30 - 20:30	
14:45
Drinks	Shift	Break
Wielgosz, Jakub	11:30 - 19:30	
13:30
Roszkiewicz, Ariel	17:00 - 22:00	
18:15
Fries	Shift	Break
Dyce, James	11:45 - 19:45	
13:45
Batch Cooker	Shift	Break
Harkess, Dana	10:00 - 18:00	
12:45
Davidson, Remy	15:00 - 23:00	
19:30
Eggs	Shift	Break
Sausage	Shift	Break
Meal/break(g)	Shift	Break
Morrice, Kayden	14:00 - 22:00	
17:00
Macdonald, Nicole	15:00 - 23:00	
17:00
Tempering & Prep	Shift	Break
BOP	Shift	Break
Assembler	Shift	Break
Logunleko, Maryam	11:00 - 19:00	
13:15
Ross, Jacob	11:00 - 20:00	
14:30
Adurojaiye, Sefia	11:30 - 19:30	
14:00
Awid, Cailean	12:00 - 20:00	
15:45
Milne, Aimee-louise	14:00 - 21:00	
16:15
Third, Chloe	14:00 - 20:15	
16:00
15:00 - 22:00	
17:30
Healey, Daniel	16:00 - 00:00	
20:00
Ross, Jorja	16:00 - 22:00	
18:30
MacNicol, Blair	16:00 - 00:00	
18:30
Support	Shift	Break
No Activity Allocation	Shift	Break
Bain, Finlay	14:00 - 22:00	
17:15
Milne, Aimee	15:00 - 23:00	
17:30
Maleszyk, Sebastian	15:30 - 21:00	
18:00
Beattie, Cameron	15:30 - 22:00	
18:30
Yule, Zack	15:30 - 21:30	
18:30
Smith, Ruairidh	17:00 - 23:30	
19:30
"""

# Extract employee information
employees_info = extract_employee_info(unedited_data)

# Save extracted information into a JSON file
with open('employee_info.json', 'w') as file:
    json.dump(employees_info, file, indent=4)

# Print extracted information
for employee in employees_info:
    print(f"Name: {employee['first_name']} {employee['last_name']} Shift Time: {employee['shift_time']}")
    