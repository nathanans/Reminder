from tkinter import *
import numpy as np
import tkinter as tk
import EmailManager
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import statisticsManager
import categoryManager
import GUI
class StatisticPage:
  #plotEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")

  def Page(root):
    def refreshMain(): 
      root.destroy()
    def refreshStatisticsPage():
      root.destroy()
      GUI.GuiStart.StatisticsPage()
    frame = Frame(root)
    frame.pack(fill = "x")
    frame.config()
    bottomframe = Frame(root)
    bottomframe.pack()

    def printchooseType(self):
      statisticsManager.statisticsReminder.choiceData = "All"
      statisticsManager.statisticsReminder.typeStat = chooseType.get()
      #print(statisticsManager.statisticsReminder.typeStat)
      refreshStatisticsPage()

    choose = ["USER","Category"]
    chooseType = StringVar()
    chooseType.set(statisticsManager.statisticsReminder.typeStat)
    dropType = OptionMenu(frame,chooseType,*choose,command=printchooseType)
    dropType["menu"].config(font=("Arial", 7))
    dropType.config(font=("Arial", 7))
    dropType.pack(side = LEFT)
    
    #tk.Button(frame,text="@",font=("Arial", 8),command = refreshStatisticsPage).pack(side = RIGHT)
    tk.Button(frame,text="Back",font=("Arial", 8),fg="white",bg="#1c768f",command = refreshMain).pack(side = RIGHT)
    #tk.Button(frame,text="Plot",font=("Arial", 8),fg="white",bg="#fa991c",command = choosePlot).pack(side = RIGHT)
    #print("\nPass DataType")

    if statisticsManager.statisticsReminder.typeStat == "USER":
      userChoice = ["All"]
      usedEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
      for i in sorted(usedEmail):
        userChoice.append(i)
    else:
      userChoice = categoryManager.categoryReminder.getCatKey() #list
      #print(userChoice)
    
    def printChooseTitle(self):
      statisticsManager.statisticsReminder.choiceData = chooseTitle.get()
      #print(statisticsManager.statisticsReminder.choiceData)
      refreshStatisticsPage()

    chooseTitle = StringVar()
    choiceChoosed = statisticsManager.statisticsReminder.choiceData
    #print(type(choiceChoosed))
    chooseTitle.set(choiceChoosed[0])
    dropemail = OptionMenu(frame, chooseTitle,*userChoice,command = printChooseTitle)
    dropemail["menu"].config(font=("Arial", 7))
    dropemail.config(font=("Arial", 7))
    dropemail.pack(side = LEFT)

    #plotData()
    #def plotData():
    dataValue = statisticsManager.statisticsReminder.getDataAllUser()
    #dataValue = statisticsManager.statisticsReminder.dataValue
    #print(type(statisticsManager.statisticsReminder.dataValue))

    x1 = dataValue[0]
    x2 = dataValue[2]
    x3 = dataValue[1]

    figure2 = Figure(figsize=(4,1), dpi=90) 
    subplot2 = figure2.add_subplot(111) 
    labels2 = 'Uncheck', 'Complete', 'Overdue' 
    pieSizes = [float(x1),float(x2),float(x3)]
    my_colors2 = 'lightsteelblue','lightblue','silver'
    explode2 = (0, 0.1, 0)  
    subplot2.pie(pieSizes, colors=my_colors2, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
    
    #subplot2.axis('equal')  
    pie2 = FigureCanvasTkAgg(figure2, root)
    pie2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=0)

    label1 = tk.Label(root, text='\nUncheck :'+str(dataValue[0])+" \nOverdue : "+str(dataValue[1])+" \nComplete : "+str(dataValue[2])+" " )
    label1.config(font=('Arial', 10))
    label1.pack(anchor = SE)

  def __init__(self,root):
    self.l=[]
    StatisticPage.Page(root)