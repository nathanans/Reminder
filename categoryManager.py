import todoManager
import json
class categoryReminder:
  
  def addCat(cat): #add cat key=[]
    with open("./Categories/categories.json") as r:
      catkey = json.load(r)
      catkeylist = list(catkey.keys())
      for i in catkeylist:
        if str(cat) in catkeylist:
          continue
        else: 
          catkey[str(cat)] = []       
      with open("./Categories/categories.json",'w') as k:
        json.dump(catkey, k)

  #address,cat = (['email','cur']),cat  
  def setCat(address,cat): #add address in category
    with open("./Categories/categories.json") as r:
      catused = json.load(r)    
      catkeyAll = list(catused["All"])
      for i in cat:
        if address in catused[i]:
          continue
        catlist = catused[i]
        catlist.append(address)
        catused[i] = catlist
      if address not in catkeyAll:
        catlist = catused["All"]
        catlist.append(address)
        catused["All"] = catlist
      with open("./Categories/categories.json",'w') as k:
        json.dump(catused, k)
      
  #(['email','cur'],cat)
  def addTodoCat(address,cat): #add cat in email
    categoryReminder.setCat(address,cat)
    with open("./Email/"+address[0]+".json") as r:
      addcat = json.load(r)
      catkeyAll = list(addcat[address[1]]["Category"])
      setcat = set(cat)
      if len(setcat) == 1:
        if cat not in catkeyAll:
          catkeyAll.append(cat[0])
      else:
        for i in cat:
          if i not in catkeyAll:
            catkeyAll.append(i)
      addcat[address[1]]["Category"] = catkeyAll
      with open("./Email/"+address[0]+".json",'w') as w:
        json.dump(addcat,w)
        
  def deleteCat(cat):
    categoryReminder.deleteCatFormAllTodo(cat)
    todoManager.todoReminder.deleteByAddress("Categories",["categories",cat])
    
  def deleteAdressformCat(address,cat):
    with open("./Categories/categories.json") as w2:
      allcat2 = json.load(w2)
      setcat = set(cat)
      if setcat == 1:
        if address in allcat2[cat[0]]:
          allcat2[cat[0]].remove(address)
      else:  
        for j in cat:
          if j == "All":
            continue
          for i in allcat2[j]:
            if i[0] == address[0] and i[1] == address[1] :
              allcat2[j].remove(i)
      with open("./Categories/categories.json", 'w') as f:
        json.dump(allcat2, f)
        
  def deleteCatWhenDeleteEmail(address):
    with open("./Email/"+address[0]+".json") as w:
      data = json.load(w)
      datakey = list(data.keys())
      for i in datakey:
        if i == "e-mailSameOwner":
          continue
        if len(data[i]["Category"]) == 0:
          continue
        for j in data[i]["Category"]:
          categoryReminder.deleteAdressformCat([address[0],i],[j])
          categoryReminder.deleteAdressformCat([address[0],i],["All"])
        
  def deleteCatFormAllTodo(cat):
    catValue = categoryReminder.getCatValue(cat)
    for i in catValue :
      with open("./Email/"+i[0]+".json") as w:
        allcat = json.load(w)
        setcat = set(cat)
        if setcat == 0:
          continue
        else:
          for k in cat:
            allcatList = list(allcat[i[1]]["Category"])
            if len(set(allcatList)) == 0:
              continue
            allcatList.remove(k)
            allcat[i[1]]["Category"] = allcatList
        if len(allcatList) == 0:
          categoryReminder.deleteAdressformCat([i[0],i[1]],["All"]) # no cat on todo anymore
          
        with open("./Email/"+i[0]+".json", 'w') as f:
          json.dump(allcat, f)
      
  def deleteCatFormTodo(address,cat): #[[email,cur],cat]
    with open("./Email/"+address[0]+".json") as w:
      allcat = json.load(w)
      allcatList = list(allcat[address[1]]["Category"])
      allcatList.remove(cat[0])
      allcat[address[1]]["Category"] = allcatList
      if len(allcat[address[1]]["Category"]) == 0:
        categoryReminder.deleteAdressformCat(address,["All"])
      with open("./Email/"+address[0]+".json", 'w') as f:
        json.dump(allcat, f)
    categoryReminder.deleteAdressformCat(address,cat)
  
  def getCat():
    catKeyNValue = []
    with open("./Categories") as f:
      data = json.load(f)
      key = data.keys()
      for i in key:
        catValue = []
        catValue.append(i)
        catValue.append(data[i])
        catKeyNValue.append(catValue)
    return catKeyNValue

  def getCatKey():
    with open("./Categories/categories.json") as f:
      data = json.load(f)
      key = list(data.keys())
    return key

  def getCatValue(cat):
    catValue = todoManager.todoReminder.getFromAddress("Categories",["categories",cat])
    return catValue #[[email,cur],[email,cur]]
  
  def catvalue(address): #address = [email,cur]
    with open("./Email/"+address[0]+".json") as r:
      addcat = json.load(r)
      catkeyAll = list(addcat[address[1]]["Category"])
      return catkeyAll

  def isCatInAdress(address,cat):
    #print(address)
    with open("./Email/"+address[0]+".json") as r:
      addcat = json.load(r)
      catkeyAll = list(addcat[address[1]]["Category"])
      if cat in catkeyAll:
        return True
      else:
        return False
