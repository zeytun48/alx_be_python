# daily_reminder.py

# Prompt for a Single Task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity
if time_bound == "yes":
    # Reminder with immediate attention
    print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
else:
    # Note without time sensitivity
    print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")

