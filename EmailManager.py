import json
import os
from datetime import datetime
import guiText

class EmailReminder:
  
  def checkInput(start,limit):
    choice = input("choice : ")
    if choice.isdigit():
      choice = int(choice)
      while choice < start or choice > limit:
        print("Error!!! Please input Only "+str(start)+"-"+str(limit))
        choice = int(input("choice : "))
      return choice
    else: 
      print("Error!! You need to input Number!!!")
      EmailReminder.checkInput(start,limit)
  
  def checkInputNull():
    topic = ""
    while topic == "":
        topic = input(str("Topic :"))
        if topic == "":
            print("You need to name Topic!")
    return topic
    
  def getEmail(file,key):
    with open("./Email/"+file+".json") as f:
        data = json.load(f)
        dataBuf = data[key]
    return dataBuf

  def setEmail(file,key,data):
    databuf = {}
    databuf[str(key)]= data
    with open("./Email/"+file+".json", 'w') as f:
      json.dump(databuf, f)

  def UpdateEmail(newEmail, location, key):
    databuf = []
    with open("./Email/"+str(location) + ".json") as f:
        data = json.load(f)
    for i in data[str(key)]:
        databuf.append(i)
    databuf.append(newEmail)
    data[str(key)] = databuf
    with open("./Email/"+location + ".json", 'w+') as f:
        json.dump(data, f)
        f.close()

  def toUsedEmail(newEmail):
    EmailReminder.UpdateEmail(newEmail, "User", "e-mailUsed")

  def isEmailUsed(self, email):
    with open("./Email/"+"User.json") as f:
        data = json.load(f)
        #print(len(data['e-mailSameOwner']))
    for i in data["e-mailUsed"]:
        if i == email:
            print("this E-mail been used. " + email)
            return True
    print("Welcome! New User!!! " + email)
    return False

  def addEmailPage(newEmail):
    databuf = []
    databuf.append(newEmail)
    data = {"e-mailSameOwner": databuf}
    inputData = json.dumps(data)
    with open("./Email/"+newEmail + ".json", 'w+') as f:
        f.write(inputData)
    EmailReminder.toUsedEmail(newEmail)

  def chooseEmail(self):
      databuf = EmailReminder.getEmail("User","e-mailUsed")
      n = 1
      email_n = []
      for i in databuf:
        print(str(n) + ". " + i)
        email_n.append(i)
        n += 1
      press = EmailReminder.checkInput(1,len(databuf))
      return str(email_n[press-1])

  def isUsed(newEmail):
    allUser = EmailReminder.getEmail("User","e-mailUsed")
    for i in allUser:
      if i == newEmail:
        return True
    return False

  def deletEmail(email):
    allUser = EmailReminder.getEmail("User","e-mailUsed")
    allUser.remove("Anonymous")
    syncUser = EmailReminder.getEmail("User","e-mailUsed")
    os.remove("./Email/"+email+'.json')
    syncUser.remove(email)
    allUser.append("Anonymous")
    allUser.remove(email)
    EmailReminder.setEmail("SynceEmail","Sync",syncUser)
    EmailReminder.setEmail("User","e-mailUsed",allUser)

  def addEmail(newEmail):
    allUser = EmailReminder.getEmail("User","e-mailUsed")
    allUser.remove("Anonymous")
    if EmailReminder.isUsed(newEmail):
      print("This Email is used...")
      EmailReminder.addEmailPage()
    else:
      EmailReminder.setEmail(str(newEmail),"e-mailSameOwner",newEmail)
      databuf = []
      databuf.append(newEmail)
      data = {"e-mailSameOwner": databuf}
      inputData = json.dumps(data)
      with open("./Email/"+str(newEmail) + ".json", 'w+') as f:
          f.write(inputData)
      allUser.append(newEmail)
      allUser.append("Anonymous")
      EmailReminder.setEmail("User","e-mailUsed",allUser)
  
  def syncEmail(syncEmail):
    syncEmailPage = EmailReminder.getEmail("SynceEmail","Sync")
    if len(syncEmailPage) == 0:
      buf = []
      buf.append(syncEmail)
    else : 
      buf = syncEmailPage
      buf.append(syncEmail)
    EmailReminder.setEmail("SynceEmail","Sync",buf)
  
  def unsyncEmail(email):
    data = EmailReminder.getEmail("SynceEmail","Sync")
    print(data,email)
    data.remove(email)
    EmailReminder.setEmail("SynceEmail","Sync",data)


