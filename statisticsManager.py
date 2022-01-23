import EmailManager
import todoManager
import json
import categoryManager
class statisticsReminder:
  plotEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
  typeStat = "USER"
  choiceData = "All"
  #dataValue = []
  def getStatisByStatus(): #list [email]
    checked = 0
    overdue = 0
    onTime = 0
    print(statisticsReminder.plotEmail)
    for i in statisticsReminder.plotEmail:
      #print(statisticsReminder.plotEmail)
      #if i == "All":
      #  continue
      with open("./Email/"+i+".json") as f:
        data = json.load(f)
        dataKey = list(data.keys())
        for j in dataKey :
          if j == "e-mailSameOwner":
            continue
          tmp = data[j]
          if tmp["Check"] == "checked" :
            checked+=1
          else :
            if todoManager.todoReminder.isLate(data[j]["Date&Time"]) :
              overdue += 1
            else : onTime +=1
    statData = [onTime ,overdue ,checked]
    #print(statData)
    #statisticsReminder.dataValue = statData 
    return statData
    
  def getStatisByCat(): #list [email]
    checked = 0
    overdue = 0
    onTime = 0
    emailForStat = []
    email = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    #print("Cat in ",statisticsReminder.choiceData )
    if statisticsReminder.choiceData == "All" :
      for i in email :
        with open("./Email/"+i+".json") as f:
          data = json.load(f)
          dataKey = list(data.keys())
          for j in dataKey :
            if j == "e-mailSameOwner":
              continue
            else :
              #print(data[j])
              if len(data[j]["Category"]) > 0 :
              #if data[j]["Category"] == statisticsReminder.choiceData :
                if data[j]["Check"] == "checked" :
                  checked+=1
                else :
                  if todoManager.todoReminder.isLate(data[j]["Date&Time"]) :
                    overdue += 1
                  else : onTime +=1
    else :
      #print(statisticsReminder.choiceData)
      for i in email :
        with open("./Email/"+i+".json") as f:
          data = json.load(f)
          dataKey = list(data.keys())
          for j in dataKey :
            if j == "e-mailSameOwner":
              continue
            else :
              if statisticsReminder.choiceData in data[j]["Category"] :
                #print("\n",data[j])
                if data[j]["Check"] == "checked" :
                  checked+=1
                else :
                  if todoManager.todoReminder.isLate(data[j]["Date&Time"]) :
                    overdue += 1
                  else : onTime +=1
                #print(onTime ,overdue ,checked)
    statData = [onTime ,overdue ,checked]
    #print(statData)
    #statisticsReminder.dataValue = statData 
    return statData

  def getDataAllUser():
    #print("choice : ",statisticsReminder.typeStat)
    #print("choice2 : ",statisticsReminder.choiceData)
    #All
    if statisticsReminder.typeStat == "USER":
      if statisticsReminder.choiceData == "All":
        statisticsReminder.plotEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
      else : 
        statisticsReminder.plotEmail = [statisticsReminder.choiceData]
      allUserData = statisticsReminder.getStatisByStatus()
    else :
      #print(statisticsReminder.choiceData)
      allUserData = statisticsReminder.getStatisByCat()
    #print(allUserData)
    return allUserData

