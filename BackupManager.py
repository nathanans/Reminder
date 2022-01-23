import json
import glob
import EmailManager
import categoryManager
import os
class BackupReminder:
  
  def addDirec(newDir):
    os.mkdir("./"+newDir)

  def getfileDirect():
    direc = []
    n = glob.glob("./*")
    EmailDirec = list(n)
    for i in EmailDirec:
      if i == "./Email" or i == "./Categories":
        continue
      if os.path.isdir(i) :
        direc.append(i)
    return sorted(direc)
  
  def getfileDirectForImport():
    direc = []
    n = glob.glob("./*")
    for i in n:
      if i == "./Email":
        continue
      if os.path.isdir(i) :
        m = glob.glob(i+"/*")
        for j in m:
          k = j.split("/")
          last = k[-1].split(".")
          if last[-1] == "json":
            direc.append(j)
    return sorted(direc)
      
  def checkForm(path):
    trueForm = ['Topic','Priority', 'Description', 'Date&Time', 'Check', 'Category']
    with open(path) as f:
      data = json.load(f)
      sameOwner = list(data.keys())
      if str(sameOwner[0]) != "e-mailSameOwner" :
        return False
      else:
        sameOwner.remove("e-mailSameOwner")
        print(sameOwner)
        for i in sameOwner:
          forCheck = list(data[i].keys())
          return (forCheck.sort()==trueForm.sort())
    
  def Export(email,path):
    with open("./Email/"+email+".json") as f:
      data = json.load(f)
      with open("./"+path+"/"+str(email)+".json", 'w') as t:
        json_string=json.dumps(data)
        t.write(json_string)
  
  def isReallyOnDirec(path):
    fileName = path.split('/')
    tmp = fileName[-1] #email.json
    newPath = path.split(tmp)
    fileInDirec = BackupReminder.fileOnFolder(newPath[0])
    importEmail = tmp.split(".json")
    if importEmail[0] in fileInDirec :
      return True
    else: return False
    

  def getEmailFormPath(path):
    tmp = path.split('\\')
    email = tmp[-1].split('.json')
    return email[0]

  def fileOnFolder(path): #email
    direcList = glob.glob("."+path+"*")
    file = []
    for i in direcList:
      tmp = i.split('/')
      email = tmp[-1].split('.json')
      file.append(email[0])
    return file

  def alreadyExported(path,email):
    direcList = glob.glob("."+path+"*")
    check = "."+path+email+".json"
    if check in list(direcList):
      return True
    else : 
      return False

  def alreadyImported(path):
    importEmail = BackupReminder.getEmailFormPath(path)
    usedEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    if importEmail in usedEmail:
      return True

  def havedJson(path):
    fileName = path.split('/')
    tmp = str(fileName[-1])
    filetype = tmp.split('.')
    if filetype[-1] == "json":
      return True
    else :
      return False

  def Import(path):
    tmp = path.split('\\')
    email = tmp[-1].split('.json')
    newEmail = email[0]
    #newEmail = BackupReminder.getEmailFormPath(path)
    with open(path) as f:
      data = json.load(f)
      with open("./Email/"+newEmail+".json", 'w') as t:
        json_string=json.dumps(data)
        t.write(json_string)
    EmailManager.EmailReminder.toUsedEmail(newEmail)
    BackupReminder.updateCat(path)

  def updateCat(path):
    email = BackupReminder.getEmailFormPath(path) #email String
    with open(path) as f:
      data = json.load(f)
      key = data.keys()
      keyList = list(key)
      keyList.remove("e-mailSameOwner")
      for i in keyList:
        value = data[i]["Category"] #form import
        oldCat = categoryManager.categoryReminder.getCatKey()
        for k in value:
          if k in oldCat:
            continue
          else:
            categoryManager.categoryReminder.addCat(k) # cat[]
            categoryManager.categoryReminder.addTodoCat([email,i],k)
            
