# daily_reminder.py

# Prompt the user for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Start constructing the reminder message
message = f"Reminder: '{task}' is a {priority} priority task"

# Modify message if the task is time-bound
if time_bound == "yes" and priority in ["high", "medium"]:
    message += " that requires immediate attention today!"
elif time_bound == "yes":
    message += ". Consider completing it soon."
elif priority == "low":
    message += ". Consider completing it when you have free time."
else:
    message += "."

# Print the reminder
print(message)

