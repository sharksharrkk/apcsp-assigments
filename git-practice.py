toDoList = ["Math Homework", "Cook Dinner", "Fold Laundry"]

def addItem(item):
   toDoList.append(item)
   return toDoList

def deleteItem(item):
   newToDo = []
   toDoDup = []
   for i in toDoList:
      newToDo.append(i)
   else:
      toDoDup.append(i)
      print("we have found duplicates and removed them!", toDoDup)
      toDoList.remove(item)
    
   

userAns = input("Do you want to add to your list ,duplicate check, or quit? A/D/Q")

while userAns == "A":
   item = input("What item do you want to add?")
   addItem(item)
   userAns = input("Do you want to add to your list, duplicate check, or quit? A/D/Q")

   if userAns == "D":
     deleteItem(item)
     userAns = input("Do you want to add to your list, duplicate check, or quit? A/D/Q")
   print(toDoList)



