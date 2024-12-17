task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

match priority:
 case "high":
  if time_bound == "yes":
   print (f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
  else :
   print(f"Note: '{task}' is a high priority task. Complete it as soon as possible.")
 case "medium":
  if time_bound == "yes":
   print (f"Reminder: '{task}' is a medium priority task with a deadline. Don't forget to complete it!")
  else:
   print (f"Note: '{task}' is a medium priority task. Complete it when you can.")
 case "low":
  if time_bound == "yes":
   print (f"Reminder: '{task}' is a low priority task but still time-bound. Finish it soon!")
  else:
   print (f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
 case _:
  print ("Invalid priority entered. Please choose high, medium, or low.")
