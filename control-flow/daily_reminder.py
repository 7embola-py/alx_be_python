# daily_reminder.py

# Prompt the user for a single task
task = input("Enter your task: ")

# Prompt for the task's priority
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match-case to handle priority
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unspecified priority"

# Modify message if the task is time-bound
if time_bound == "yes":
    if priority in ["high", "medium"]:
        message += " that requires immediate attention today!"
    else:
        message += ". Consider completing it soon!"
else:
    if priority == "low":
        message += ". Consider completing it when you have free time."
    else:
        message += "."

# Print the final reminder
print(message)
