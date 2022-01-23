import tkinter as tk
from tkinter import *
import EmailManager
import todoManager
import guiManageEmail
import GUI
import guiEditPage
from tkinter.scrolledtext import ScrolledText
import categoryManager 
import statisticsManager
import GUI
import guiEditCatPage

class MainPage:
  def Page(root):
    def BackToMain():
        root.destroy()
        GUI.GuiStart.MainPage()
    
    def chooseHightlight(setData):#[topic,email,curtime]
      #print(setData[0])
      priorityBuf = EmailManager.EmailReminder.getEmail(setData[0][1],setData[0][2])
      colorHL = ["white","#cce2cb","#f6eac2","#ffb3c6"]
      return colorHL[int(priorityBuf["Priority"])]
    
    def buildCheckbox(status,islate,textColor):
      def getResult():
        for i,j in zip(checkboxData,tp):# tp [[topic,email,cur],[]]
          if i.get() == "checked":
            todoManager.todoReminder.updateCheckList(j[1],j[2],"uncheck")
            BackToMain()
      def editResult(k): # [email,curtime]
        GUI.GuiStart.callguiEdit(k)
      
      tmp = todoManager.todoReminder.getTodoByStatus(status,islate)
      todoList = tmp[0]
      topicList = tmp[1]
      if len(todoList)!=0:
        checkboxData = [StringVar() for i in topicList ]
        EditData = [StringVar() for i in topicList]
        for i in checkboxData:
          i.set("uncheck")
        tp = []
        n=0
        #text = ScrolledText(root, width=10, height=3)
        #text.pack()
        frame = Frame(root)
        frame.pack(fill = "x")
        frame.config(bg="white")
        bottomframe = Frame(root)
        bottomframe.pack()
        
        for i in todoList:# i = [[topic,email,curtime],date]
          highlight = chooseHightlight(i[0])
          #print(i[0])
          if GUI.GuiStart.catChoice == "All" :
            if status == "uncheck": 
              #frame.config(bg="white")
              tk.Label(frame, text=i[1],font=("Arial", 7),fg=textColor, bg="white").pack(anchor=W)
              #frame.config(bg="white")
              for j in i[0]:
                #frame.config(bg=highlight)
                frame2 = Frame(frame)
                frame2.pack(anchor = W,fill = "x")
                bottomframe = Frame(frame)
                bottomframe.pack(side = LEFT)
                tk.Checkbutton(frame2, text=j[0],font=("Arial", 8), anchor='w',fg=textColor,bg=highlight,variable=checkboxData[n],onvalue = "checked",offvalue="uncheck",command=getResult).pack(side = LEFT,fill="both", expand=True)
                tk.Button(frame2, text="Edit",font=("Arial", 8),command = lambda m=[j[1],j[2]]: editResult(m)).pack(side = RIGHT)
                tp.append(j)
                n+=1
            else :
              for j in i[0]: #[topic,email,curtime]
                #frame.config(bg=highlight)
                frame2 = Frame(frame)
                frame2.pack(anchor = W,fill = "x")
                bottomframe = Frame(frame)
                bottomframe.pack(side = LEFT)
                tk.Checkbutton(frame2, text=j[0],font=("Arial", 8), anchor='w',fg=textColor,bg=highlight,variable=checkboxData[n],onvalue = "uncheck",offvalue="checked",command=getResult).pack(side = LEFT,fill="both", expand=True)
                tk.Button(frame2, text="Edit",font=("Arial", 7),command = lambda m=[j[1],j[2]]: editResult(m)).pack(side = RIGHT)
                tp.append(j)
                n+=1
          else:
            #catEmail = categoryManager.categoryReminder.getCatValue(GUI.GuiStart.catChoice)
            #print(catEmail)
            #email = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
            if status == "uncheck" :
              frame.config(bg="white")
              if categoryManager.categoryReminder.isCatInAdress([i[0][0][1],i[0][0][2]],GUI.GuiStart.catChoice ) :
                tk.Label(frame, text=i[1],font=("Arial", 7),fg=textColor, bg="white").pack(anchor=W)
              for j in i[0]:
                print(j)
                if categoryManager.categoryReminder.isCatInAdress([i[0][0][1],i[0][0][2]],GUI.GuiStart.catChoice ):
                  #frame.config(bg=highlight)
                  frame2 = Frame(frame)
                  frame2.pack(anchor = W,fill = "x")
                  bottomframe = Frame(frame)
                  bottomframe.pack(side = LEFT)
                  tk.Checkbutton(frame2, text=j[0],font=("Arial", 8), anchor='w',fg=textColor,bg=highlight,variable=checkboxData[n],onvalue = "checked",offvalue="uncheck",command=getResult).pack(side = LEFT,fill="both", expand=True)
                  tk.Button(frame2, text="Edit",font=("Arial", 8),command = lambda m=[j[1],j[2]]: editResult(m)).pack(side = RIGHT)
                  tp.append(j)
                  n+=1
            else :
              for j in i[0]: #[topic,email,curtime]
                if categoryManager.categoryReminder.isCatInAdress([i[0][0][1],i[0][0][2]],GUI.GuiStart.catChoice ):
                  #frame.config(bg=highlight)
                  frame2 = Frame(frame)
                  frame2.pack(anchor = W,fill = "x")
                  bottomframe = Frame(frame)
                  bottomframe.pack(side = LEFT)
                  tk.Checkbutton(frame2, text=j[0],font=("Arial", 8), anchor='w',fg=textColor,bg=highlight,variable=checkboxData[n],onvalue = "uncheck",offvalue="checked",command=getResult).pack(side = LEFT,fill="both", expand=True)
                  tk.Button(frame2, text="Edit",font=("Arial", 7),command = lambda m=[j[1],j[2]]: editResult(m)).pack(side = RIGHT)
                  tp.append(j)
                  n+=1
    
    def setTodoByCat(self):
      GUI.GuiStart.catChoice = chooseTitle.get()
      BackToMain()

    frame = Frame(root)
    frame.pack(fill = "x")
    frame.config(bg="white")
    bottomframe = Frame(root)
    bottomframe.pack()
    userChoice = categoryManager.categoryReminder.getCatKey()
    chooseTitle = StringVar()
    chooseTitle.set(GUI.GuiStart.catChoice)
    dropemail = OptionMenu(frame, chooseTitle,*userChoice,command = setTodoByCat)
    dropemail["menu"].config(font=("Arial", 8))
    dropemail.config(font=("Arial", 8))
    dropemail.pack(side = LEFT)
    tk.Button(frame,text="+",font=("Arial", 8),command = GUI.GuiStart.EditCatPage).pack(side = LEFT)

    fgColr = "black"
    tk.Label(root, text="-----Todo List-----",font=("Arial", 9),fg="black", bg="white").pack(anchor=W)
    buildCheckbox("uncheck","onTime",fgColr)
    fgColr = "#8B0000"
    tk.Label(root, text="-----Overdue-----",font=("Arial", 9),fg="black", bg="white").pack(anchor=W)
    buildCheckbox("uncheck","late",fgColr)
    fgColr = "gray"
    tk.Label(root, text="-----Finished-----",font=("Arial", 9),fg="black", bg="white").pack(anchor=W)
    buildCheckbox("checked","onTime",fgColr)
    buildCheckbox("checked","late",fgColr)

  def __init__(self,root):
    self.l=[]
    MainPage.Page(root)