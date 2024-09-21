# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = ""

# Process the Task Based on Priority and Time Sensitivity
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task."
        if time_bound == "yes":
            reminder += " It would be good to address it soon."
        else:
            reminder += " Consider scheduling it for later."
    case "low":
        reminder = f"Reminder: '{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " However, it requires immediate attention today!"
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level."

# Print the Reminder
print(reminder)

