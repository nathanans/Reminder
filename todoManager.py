import json
import os
from datetime import datetime
from datetime import date
import dateutil
from dateutil.parser import parse
from collections import OrderedDict
import EmailManager
import guiText
import time
import categoryManager

class todoReminder:
  def __init__(self):
    self.l = []
  #def checkInput(start,limit):
  def editTodoGui(self,curTime, topic,Priority, description, toEmail, DateSet,TimeSet,oldEmail):
    if oldEmail != toEmail:
      todoReminder.addTodoToemail(topic,Priority, description,toEmail,DateSet,TimeSet)
      todoReminder.deleteByAddress("Email",[oldEmail,curTime])
    else : todoReminder.updateTodoToemail(self,curTime, topic,Priority, description,toEmail,DateSet,TimeSet,oldEmail)

  def addTodo(self,status):
    topic = EmailManager.EmailReminder.checkInputNull()  
    Priority = todoReminder.prioritylevel(self)#0-3
    P = ["","!","!!","!!!"]
    topic += P[Priority]
    description = input(str("Description :"))

    toEmail = EmailManager.EmailReminder.chooseEmail(self)
    DateSet = todoReminder.setDate(self)
    TimeSet = todoReminder.setTime(self)
    if todoReminder.isSave():
      if status[0] == "add":
        todoReminder.addTodoToemail(topic,Priority, description,toEmail,DateSet,TimeSet)
      if status[0] == "edit":
        if status[1][0] != toEmail:
          todoReminder.addTodoToemail(topic,Priority, description,toEmail,DateSet,TimeSet)
          todoReminder.deleteByAddress("Email",[status[1][0],status[1][1]])
        else : todoReminder.updateTodoToemail(self,status[1][1], topic,Priority, description,toEmail,DateSet,TimeSet,status[1][0])
    else : guiText.showReminder.showMainPage(self)


  def updateTodoToemail(self,curTime, topic,Priority, description, toEmail, DateSet,TimeSet,oldEmail):
    with open("./Email/"+str(toEmail) + ".json") as f:
        data = json.load(f)
    #databuf.append(self.user)
    print(str(curTime))
    data[str(curTime)].update({
        "Topic": topic,
        "Priority" : Priority,
        "Description": description,
        "Date&Time" : DateSet+" "+TimeSet,
        "Category" : []
    })
    with open("./Email/"+toEmail + ".json", 'w') as f:
      json.dump(data,f)

  def addTodoToemail(topic,Priority, description, toEmail, DateSet, TimeSet):
    now = datetime.now()
    #current_time = now.strftime("%H:%M:%S")
    with open("./Email/"+str(toEmail) + ".json") as f:
        data = json.load(f)
    #databuf.append(self.user)
    databuf = {
        "Topic": topic,
        "Priority" : Priority,
        "Description": description,
        "Date&Time" : DateSet+" "+TimeSet,
        "Check" : "uncheck",
        "Category" : []
    } 
    data[str(now)] = databuf
    with open("./Email/"+toEmail + ".json", 'w') as f:
        json.dump(data,f)
  
  '''def setDate(self):
    day = int(input("Enter a day : "))
    month = int(input("Enter a month : "))
    year = int(input("Enter a year : "))
    DateToDo = str(day)+ "/" + str(month) +"/"+str(year)

    return DateToDo
     
  def setTime(self):
    hour = int(input("Enter hour : "))
    minute = int(input("Enter minute : "))
    sec = int(input("Enter sec : "))
    TimeToDo = str(hour)+ ":" + str(minute) +":"+str(sec)
    return TimeToDo'''

  def prioritylevel(self):
    Priority = ""
    Priority = input("Priority level (1) -Low- (2) -Medium- (3) -High- : ")
    if Priority == "":
      Priority = 0
    Priority = int(Priority)
    if Priority == 0 or Priority == 1 or Priority == 2 or Priority == 3 :
      return Priority
    else: 
      print("Please choose level 1-3 !" + "\n")
      todoReminder.prioritylevel(self)

  def isSave():
    choice = input("(1) Save (2) cancle :")
    choice = int(choice)
    if choice == 1:
        return True
    elif choice == 2:
        return False
    else:
        print("You need to choose 1 or 2 !")
        todoReminder.isSave()

  def sortDateTime(status):
    data = todoReminder.showCheckList(status)
    #print(data)
    TopicnDate = []
    tmp = {}
    for i in data:
      n=[]
      #print(i)
      with open("./Email/"+i[0]+".json") as f:
        databuf = json.load(f)
      tdKey = list(tmp.keys()) 
      #print(tdKey)
      if databuf[i[1]]["Date&Time"] in tdKey:
        topicbuf = tmp[databuf[i[1]]["Date&Time"]]
        #print(topicbuf)
        topicbuf.append(databuf[i[1]]["Topic"])
      else : tmp[databuf[i[1]]["Date&Time"]] = [databuf[i[1]]["Topic"]]
    #print(tmp)
    new_d = OrderedDict(sorted(tmp.items(), key=lambda x: parse(x[0])))
    late = []
    TopicnDate = []
    for i in reversed(list(new_d)):#time
      if todoReminder.isLate(i):
        late.append([new_d[i],i])
        #print(new_d[i])
        #print(late)
      else:
        TopicnDate.append([new_d[i],i])
    #print(TopicnDate,"\n",late)
    return [TopicnDate,late] #[[topic,time]]

  def isLate(uncheckTime):
    now = datetime.now()
    #2022-01-16 15:53:39.610064
    #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    newuncheckTime = datetime.strptime(uncheckTime,"%d/%m/%Y %H:%M:%S")
    #print(dt_string >= uncheckTime,dt_string,uncheckTime)
    return now > newuncheckTime #new > old

  def updateCheckList(email,key,s1tatus):
    with open("./Email/"+email+".json") as f:
      data = json.load(f)
    if data[key]["Check"] == "checked":
      data[key]["Check"] = "uncheck"
    else:
      data[key]["Check"] = "checked"
    with open("./Email/"+email+".json", 'w') as f:
      json.dump(data, f)
  
  def getTodoDetail(key):
    with open("./Email/"+key[0]+".json") as f:
      data = json.load(f)
    dataList = list(data[key[1]].values())
    return dataList
      
  def showAllCheckList():
    syncEmail = EmailManager.EmailReminder.getEmail("SynceEmail","Sync")
    returnList = []
    n = 1
    for k in syncEmail:
      with open("./Email/"+k+".json") as f:
            data = json.load(f)
      for i in data:
        if i == "e-mailSameOwner":
          continue
        print("("+str(n)+") "+data[i]["Topic"])
        n+=1
        returnList.append([k,i])
        todoReminder.getTodoDetail([k,i])
    return returnList

  def showCheckList(status):
    syncEmail = EmailManager.EmailReminder.getEmail("SynceEmail","Sync")
    returnList = []
    #n = 1
    for k in syncEmail:
      with open("./Email/"+k+".json") as f:
        data = json.load(f)
      for i in data:
        if i == "e-mailSameOwner":
          continue
        if data[i]["Check"] == status :
          #print("("+str(n)+") "+data[i]["Topic"])
          #n+=1
          returnList.append([k,i])#[[email,current_time],[],[]]
    return returnList

  def deleteByAddress(folder,key):
    with open("./"+folder+"/"+key[0]+".json") as f:
      data = json.load(f)
    data.pop(key[1][0])
    with open("./"+folder+"/"+key[0]+".json", 'w') as f:
      json.dump(data, f)

  def getFromAddress(folder,address):#["Email",[email,curtim]]
    with open("./"+folder+"/"+address[0]+".json")  as f:
      data = json.load(f) 
    return data[address[1][0]] #Dict

  '''def readFormTwoKey(status):
    todoList = []
    keyList= todoReminder.showCheckList(status)
    for i in keyList:
      with open("./Email/"+i[0]+".json")  as f:
        data = json.load(f)
      todoList.append(data[i[1]]["Topic"])
    return todoList'''

  def getTodoByStatus(status,islate):
    todoListBuf = todoReminder.sortDateTimewithcur(status)
    #todoListBuf = todoManager.todoReminder.sortDateTime(status)
    topicList = [] #[   [[topic,email,curtime],date]   ,   [[topic,email,curtime],date]   ]
    #print(todoListBuf)
    if islate == "onTime":
      todoList = todoListBuf[0] #topic date 
      il = 0
      #print(todoList)
    if islate == "late" : 
      todoList = todoListBuf[1] #topic date
      il = 1
      #print(todoList)
    for i in todoList:
      for j in i[0]:
        topicList.append(j[0]) #[topic,email,curtime]
    return [todoList,topicList]

  def sortDateTimewithcur(status):
    data = todoReminder.showCheckList(status) #email,Cur
    #print(data)
    TopicnDate = []
    tmp = {}
    for i in data:
      n=[]
      #print(i)
      with open("./Email/"+i[0]+".json") as f:
        databuf = json.load(f)
      tdKey = list(tmp.keys()) 
      #print(tdKey)
      if databuf[i[1]]["Date&Time"] in tdKey :
        #print(tmp[databuf[i[1]]["Date&Time"]])
        tmp[databuf[i[1]]["Date&Time"]].append([   databuf[i[1]]["Topic"] , i[0] , i[1]   ])
        #print(tmp)
      else : tmp[databuf[i[1]]["Date&Time"]] = [[ databuf[i[1]]["Topic"],i[0],i[1] ]]
    #print(tmp)
   # print(topicbuf)
    #print(tmp)
    new_d = OrderedDict(sorted(tmp.items(), key=lambda x: parse(x[0]))) # dict
    #print(new_d,"\n",list(new_d),"\n")
    late = []
    TopicnDate = []
    for i in reversed(list(new_d)):#time
      if todoReminder.isLate(i):
        late.append([new_d[i],i])
        #print(new_d[i])
        #print(late)
      else:
        TopicnDate.append([new_d[i],i])
    #print(TopicnDate,"\n",late)
    #print([TopicnDate,late])
    return [TopicnDate,late] #[[[topic,email,curtime],remindTime],[[topic,email,curtime],remindTime]]