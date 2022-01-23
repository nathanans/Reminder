import json
import os
from datetime import datetime
import EmailManager
import todoManager
class showReminder:
  def __init__(self):
    self.l = []
    #Reminder = EmailManager.Reminder()
  def showAllUser():
    allUser = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    allUser.remove("Anonymous")
    n=1
    for i in allUser:
        print(str(n)+"."+i)
        n+=1

  def deleteEmailPage(self):
    #os.system('clear')
    print("\n-----Delete Email-----")
    showReminder.showAllUser()
    allUser = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    allUser.remove("Anonymous")
    syncUser = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    press = EmailManager.EmailReminder.checkInput(1,len(allUser))
    print("\n***** If you delet this Email all data will gone. *****\n")
    print("(1) Yes,Delete it. (2) No,Don't Delete it.")
    press2 = EmailManager.EmailReminder.checkInput(1,2)
    if press2 == 1 :
      EmailManager.EmailReminder.deletEmail(allUser[press-1])
    showReminder.manageEmailPage(self)
    
  def addEmailPage(self):
    #os.system('clear')
    print("\n-----Add New Email-----")
    ("-----Email already used-----")
    showReminder.showAllUser()
    newEmail = input("New Email : ")
    EmailManager.EmailReminder.addEmail(newEmail)
    showReminder.manageEmailPage(self)

  def addTodoPage(self):
    #os.system('clear')
    print("-----Add New Reminder-----")
    #Gui
    # 5-6
    todoManager.todoReminder.addTodo(self,["add"])
  
  def syncEmailPage(self):
    #os.system('clear')
    print("-----Sync Email-----")
    press = ""
    unsync = []
    Email = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    syncEmailPage = EmailManager.EmailReminder.getEmail("SynceEmail","Sync")
    n = 1
    for i in Email:
      if i in syncEmailPage:
        continue
      unsync.append(i)
      print(str(n)+"."+i)
      n+=1
    if len(unsync)==0:
      print("No Email to Sync... Press any to go back...")
      press = input()
      showReminder.manageEmailPage(self)
    else :
      press = EmailManager.EmailReminder.checkInput(1,len(unsync))
      syncEmailPage.append(unsync[press-1])
    EmailManager.EmailReminder.syncEmail(syncEmailPage)
    showReminder.manageEmailPage(self)

  def unsyncEmailPage(self):
    #os.system('clear')
    print("-----Unsync Email-----")
    usedEmail = EmailManager.EmailReminder.getEmail("SynceEmail","Sync")
    if len(usedEmail)==0:
      print("No Unsync Email... Press any to go back...")
      press = input()
      showReminder.manageEmailPage(self)
    else :
      n=1
      for i in usedEmail:
          print(str(n)+"."+i)
          n+=1
      press = EmailManager.EmailReminder.checkInput(1,len(usedEmail))
      email = usedEmail[press-1]
    EmailManager.EmailReminder.unsyncEmail(email)  
    showReminder.manageEmailPage(self)  
  
  def checkPage(self):
    #os.system('clear')
    print("-----Check Todo-----")
    print("(0) <--- Back to main")
    count = todoManager.todoReminder.showCheckList("uncheck") #[email,Cur]
    print(count)
    n = 1
    for k in count:
      with open("./Email/"+k[0]+".json") as f:
        data = json.load(f)
      print("("+str(n)+") "+data[k[1]]["Topic"])
      n+=1
    print("-----Finished-----")
    uncheck = todoManager.todoReminder.showCheckList("checked")
    n = 1
    for k in uncheck:
      with open("./Email/"+k[0]+".json") as f:
        data = json.load(f)
      print("X "+data[k[1]]["Topic"])
      n+=1
    press = EmailManager.EmailReminder.checkInput(0,len(count))
    if press == 0 :
      showReminder.showMainPage(self)
    todoManager.todoReminder.updateCheckList(count[press-1][0],count[press-1][1],"checked")
    showReminder.checkPage(self)

  def UncheckPage(self):
    #os.system('clear')
    print("-----Uncheck Todo-----")
    count = todoManager.todoReminder.showCheckList("uncheck")
    for k in count:
      with open("./Email/"+k[0]+".json") as f:
        data = json.load(f)
      print("O "+data[k[1]]["Topic"])
    print("-----Finished-----")
    print("(0) <--- Back to main")
    uncheck = todoManager.todoReminder.showCheckList("checked")
    n = 1
    for k in uncheck:
      with open("./Email/"+k[0]+".json") as f:
        data = json.load(f)
      print("("+str(n)+") "+data[k[1]]["Topic"])
      n+=1
    press = EmailManager.EmailReminder.checkInput(0,len(uncheck))
    if press == 0 :
      showReminder.showMainPage(self)
    todoManager.todoReminder.updateCheckList(uncheck[press-1][0],uncheck[press-1][1],"uncheck")
    showReminder.UncheckPage(self)
    

  def manageEmailPage(self):
    #os.system('clear')
    press = ""
    print("-----Manage Email-----")
    usedEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    syncEmailPage = EmailManager.EmailReminder.getEmail("SynceEmail","Sync")
    for i in usedEmail:
      if i in syncEmailPage:
        print("+ "+i)
      else:
        print("- "+i)
    print("\n(0) Back to Main")
    print("(1) Sync Email")
    print("(2) Unsync Email")
    print("(3) Add New Email")
    print("(4) Delete Email")
    press = EmailManager.EmailReminder.checkInput(0,4)
    if press == 0 :
      showReminder.showMainPage(self)
    elif press == 1 :
      showReminder.syncEmailPage(self)
    elif press == 2 :
      showReminder.unsyncEmailPage(self)
    elif press == 3 :
      showReminder.addEmailPage(self)
    elif press == 4 :
      showReminder.deleteEmailPage(self)

  def seeDetail(self):
    #os.system('clear')
    print("-----All Check List-----")
    allCheckList = todoManager.todoReminder.showAllCheckList()
    print("-------Choose todo List to Edit or Delet-------")
    print("(0) <--- Back to main")
    press = EmailManager.EmailReminder.checkInput(0,len(allCheckList))
    if press == 0 :
      showReminder.showMainPage(self)
    showReminder.editDetailPage(self,allCheckList[press-1])

  def editDetailPage(self,key):
    #os.system('clear')
    print("-------Edit or Delete-------")
    todoManager.todoReminder.getTodoDetail(key)
    print("(0) <--- Back to main")
    print("(1) -Edit- \n(2) -Delete-")
    press = EmailManager.EmailReminder.checkInput(0,2)
    if press == 0 :
      showReminder.showMainPage(self)
    if press == 1:
      print("-------Edit-------")
      todoManager.todoReminder.addTodo(self,["edit",key])
      #todoManager.todoReminder.todoUpdate(self)
    if press == 2:
      print("\n***** Are you sure to DELETE?. *****\n")
      print("(1) -Yes- \n(2) -No-")
      press = EmailManager.EmailReminder.checkInput(1,2)
      if press == 1:
        todoManager.todoReminder.deleteByAddress("Email",key)
        showReminder.seeDetail(self)
      else : showReminder.editDetailPage(self,key)

  def showTodoInMain():
    show = todoManager.todoReminder.getDataFromSyncedEmail("Topic")
    todoList =[]
    for i in show:
      todoList.append(i)
      print("O "+i)
    return todoList
  
  def showMainPage(self):
    #os.system('clear')
    print("-----Main-----\n")
    uncheck = todoManager.todoReminder.sortDateTime("uncheck")
    #print(uncheck[0])
    for i in uncheck[0]:
      print(i[1])
      for j in i[0]:
        print("\tO "+j)
    #count = todoManager.todoReminder.showCheckList("uncheck")
    print("\n-----Overdue-----\n")
    late = todoManager.todoReminder.sortDateTime("uncheck")
    #print(late)
    for i in late[1]:
      print(i[1])
      for j in i[0]:
        print("\tO "+j)
    print("\n-----Finished-----\n")
    checked = todoManager.todoReminder.sortDateTime("checked")
    #print(checked)
    for i in checked[0]:
      for j in i[0]:
        print("\tX "+j)
    for i in checked[1]:
      for j in i[0]:
        print("\tX "+j)
    print("\n--------------\n(1) -Add Todo- \n(2) -Check Todo-\n(3) -Uncheck Todo-\n(4) -Manage Email-\n(5) -See Detail-")
    press = EmailManager.EmailReminder.checkInput(1,5)
    if press == 1:
      showReminder.addTodoPage(self)
    if press == 2 :
      showReminder.checkPage(self)
    if press == 3 :
      showReminder.UncheckPage(self)
    if press == 4 :
      showReminder.manageEmailPage(self)
    if press == 5 :
      showReminder.seeDetail(self)
    showReminder.showMainPage(self)


