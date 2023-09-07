toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

def deleteItem(item):
   newToDo = []
   toDoDup = []
   for i in toDoList:
      newToDo.append(i)
      print("There's no duplicates!")
   else:
      toDoDup.append(i)
      print("we have found duplicates!" + toDoDup)
   
   toDoList.remove(item)
   

userAns = input("Do you want to add to your list ,delete an item, or quit? A/D/Q")

while userAns == "A":
   item = input("What item do you want to add?")
   addItem(item)
   userAns = input("Do you want to add to your list, delete an item, or quit? A/D/Q")
   print(toDoList)
   if userAns == "D":
     item = input("What would you like to delete?")
     deleteItem(item)
     userAns = input("Do you want to add to your list, delete an item, or quit? A/D/Q")
   print(toDoList)



