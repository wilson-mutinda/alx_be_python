Task = input("Enter your task: ")
Priority = input("Priority (high/medium/low): ")
Time_Bound = input("Is it time bound? (yes/no): ")

match Priority:
 case "high":
  if Time_Bound == "yes":
   print (f"Reminder: '{Task}' is a high priority task that requires immediate attention today!")
  else :
   print(f"Note: '{Task}' is a high priority task. Complete it as soon as possible.")
 case "medium":
  if Time_Bound == "yes":
   print (f"Reminder: '{Task}' is a medium priority task with a deadline. Don't forget to complete it!")
  else:
   print (f"Note: '{Task}' is a medium priority task. Complete it when you can.")
 case "low":
  if Time_Bound == "yes":
   print (f"Reminder: '{Task}' is a low priority task but still time-bound. Finish it soon!")
  else:
   print (f"Note: '{Task}' is a low priority task. Consider completing it when you have free time.")
 case _:
  print ("Invalid priority entered. Please choose high, medium, or low.")
