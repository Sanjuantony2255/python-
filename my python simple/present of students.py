# Get the number of students
n = int(input("Enter the number of students: "))

# Get the total number of working days
total_working_days = int(input("Enter the total number of working days: "))

# Initialize an empty dictionary to store student names and their attendance percentage
attendance_dict = {}

# Read the names and attendance of n students
for i in range(n):
    name = input(f"Enter the name of student {i + 1}: ")
    
    # Read the number of days present
    days_present = int(input(f"Enter the number of days {name} is present within {total_working_days} working days: "))
    
    # Calculate attendance percentage
    attendance_percentage = (days_present / total_working_days) * 100
    
    # Add to the dictionary
    attendance_dict[name] = attendance_percentage

# Display the dictionary of student names and attendance percentage
print("Dictionary of student names and attendance percentage:", attendance_dict)
