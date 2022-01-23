from tkinter import *
import tkinter as tk
import guiText
import todoManager
import EmailManager
from tkcalendar import *
from datetime import datetime
import os
import main
import GUI
import guiSelectCat
import categoryManager
import json

class TopicPage:
  
  catList = []

  def AddTopicPage(root):
   
    def getTopic():
      message = topicGet.get()
      return message
 
    def SelectPriority():
      prioritylevel = clicked.get()
      return prioritylevel
  
    def getDescript():
      descript = Des.get()
      return descript

    def selectDate():
      dateget = cal.get_date()
      datenew = datetime.strptime(dateget, "%m/%d/%y").strftime("%d/%m/%Y")      
      return str(datenew)

    def selectTime():
      h = hoursb.get()
      m = minsb.get()
      s = sec.get()
      timeget = f"{h}:{m}:{s}"
      return str(timeget)

    def selectEmail():
      email_s = emailSelect.get()
      return email_s

    def backTomain():
      guiSelectCat.CategoryPage.Catselect = []
      root.destroy()
      
    def lastCur():
      email = selectEmail()
      with open("./Email/"+email+".json") as r:
        data = json.load(r)
        keylist = list(data.keys())
      return keylist[-1]
    
    def SaveTodo():
      topic = getTopic()
      priority = SelectPriority()
      descript = getDescript()
      email = selectEmail()  
      dateget = selectDate() 
      timeget = selectTime()
      Category = TopicPage.catList
      todoManager.todoReminder.addTodoToemail( topic, priority, descript, email, dateget, timeget)
      curtime = lastCur()
      categoryManager.categoryReminder.addTodoCat([email,curtime],Category)
      guiSelectCat.CategoryPage.Catselect = []
      root.destroy()
      
    def setCat():
      GUI.GuiStart.callguiCat()
      
    ########################################################################
    
    tk.Button(root, text= "Back",font=("Arial", 7),fg="white",bg="#1c768f", command = backTomain).pack(anchor = NE)
    
    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
    tk.Label(frame,text="Topic : ",font=("Arial", 7)).pack(anchor = W)
    topicGet = StringVar()    
    tk.Entry(frame,textvariable=topicGet,font=("Arial", 7)).pack(side = LEFT)
    
    level = [0,1,2,3]
    clicked = StringVar()
    clicked.set(0)
    
    tk.Label(frame,text="Priority : ",font=("Arial", 7)).pack(side = LEFT)
    dropPriority = tk.OptionMenu(frame , clicked,*level)
    dropPriority["menu"].config(font=("Arial", 7))
    dropPriority.config(font=("Arial", 7))
    dropPriority.pack(side = LEFT)

    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
    tk.Label(frame,text="Description : ",font=("Arial", 7)).pack(anchor = W)
    Des = StringVar()
    tk.Entry(frame,textvariable= Des,font=("Arial", 7)).pack(fill = "x")
    tk.Label(frame,text="Calendar : ",font=("Arial", 7)).pack(side = LEFT)
    
    now = datetime.now()
    getHour = StringVar()
    getMin = StringVar()
    getSec = StringVar()

    #แสดงdefault
    cal = Calendar(root,font=("Arial", 7), selectmode="day",year= now.year, month=now.month, day=now.day)
    cal.pack(fill = "x")

    tk.Button(root, text= "Set Date",font=("Arial", 7), command = selectDate).pack()

    f1 = Frame(root)
    f2 = Frame(root)

    tk.Label(root,text="Time : ",font=("Arial", 7)).pack()
    f1.pack()
    f2.pack()
    hoursb = Spinbox(f2 , from_= 0 , to = 23 , wrap = True ,textvariable = getHour ,width = 5,state ="readonly", justify = CENTER)
    minsb = Spinbox(f2 ,from_= 0, to = 59, wrap = True, textvariable = getMin , width = 5, state ="readonly",justify=CENTER)
    sec = Spinbox(f2 ,from_= 0, to = 59, wrap = True, textvariable= getSec, width = 5, state ="readonly",justify=CENTER)

    hoursb.pack(side=LEFT, fill=X, expand=True)
    minsb.pack(side=LEFT, fill=X, expand=True)
    sec.pack(side=LEFT, fill=X, expand=True)
    
    tk.Button(f2, text= "Set Time",font=("Arial", 7) ,command= selectTime).pack(side=LEFT)
    
    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
    
    tk.Label(frame,text="Email : ",font=("Arial", 7)).pack(anchor=W)

    syncEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    emailSelect = StringVar()
    emailSelect.set(syncEmail[0])
    dropemail = OptionMenu(frame, emailSelect,*syncEmail)
    dropemail["menu"].config(font=("Arial", 7))
    dropemail.config(font=("Arial", 7))
    dropemail.pack(side = LEFT)
    tk.Button(frame,text="Select Email",font=("Arial", 7),command = selectEmail).pack(side = LEFT)
      
    tk.Button(root, text="Category",font=("Arial", 7),command = setCat).pack()

    fSave = Frame(root)
    fSave.pack()
    bottom = Frame(root)
    bottom.pack()
    tk.Button(fSave,text="Cancle",font=("Arial", 7,'bold'),fg = "white",bg = "#e83845",command = backTomain).pack(side = LEFT)
    tk.Button(fSave,text="Save",font=("Arial", 7,'bold'),command= SaveTodo).pack(side = RIGHT)
  
  def __init__(self,root):
    self.l = []
    TopicPage.AddTopicPage(root)


