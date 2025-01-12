def display_menu():
 print("Shopping List Manager")
 print("1. Add Item")
 print("2. Remove Item")
 print("3. View List")
 print("4. Exit")

def main():
 shopping_list = []
 while True:
  display_menu()
  choice = input("Enter your choice: ")

  if choice == '1':
   item = input("Enter an item: ")
   shopping_list.append(item)
   print(f"{item} added to the list.")
  elif choice == '2':
   item_to_remove = input("Enter item to remove: ")
   if item_to_remove in shopping_list:
    shopping_list.remove(item_to_remove)
    print(f"{item_to_remove} removed from the list.")
   else:
    print("Item not in the list.")
  elif choice == '3':
   print("\nCurrent Shopping List")
   if shopping_list:
    for item in shopping_list:
     print(item)
   else:
    print("Shopping list is empty")
  elif choice == '4':
   print('Goodbye')
   break
  else:
   print("Invalid choice")

if __name__ == "__main__":
 main()
