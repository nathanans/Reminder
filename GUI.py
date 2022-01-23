from tkinter import *
import tkinter as tk
import os
import guiwriteTopic
import guiManageEmail
import guiMainPage
import guiEditPage
import guiBackupPage
import guiStatisticsPage
import categoryManager
import guiEditCat
import guiSelectCat
import guiEditCatPage

class GuiStart:
  catChoice = "All"
  
  def callguiTopic():
    addTopicWin = Toplevel(root)
    addTopicWin.title('Add Topic')
    addTopicWin.geometry("250x600")
    guiwriteTopic.TopicPage(addTopicWin)

  def callguiEdit(k):
    EditTopicWin = Toplevel(root)
    EditTopicWin.title('Edit Topic')
    EditTopicWin.geometry("250x600")
    guiEditPage.EditPage(EditTopicWin,k)

  def callguiCat(): 
    Catwin = Toplevel(root)
    Catwin.title('Categories')
    Catwin.geometry("250x600")
    guiSelectCat.CategoryPage.ChooseCat(Catwin)
  
  def callguiEditCat(n):
    editCatwin = Toplevel(root)
    editCatwin.title('Categories')
    editCatwin.geometry("250x600")
    guiEditCat.editCategoryPage.EditCat(editCatwin,n)
  
  
  def StatisticsPage():
    newWindow = Toplevel(root)
    newWindow.title("Statistics Page")
    newWindow.geometry("500x300")
    guiStatisticsPage.StatisticPage(newWindow)
    
  def ManageEmailPage():
    newWindow = Toplevel(root)
    newWindow.title("Manage Email Page")
    newWindow.geometry("250x600")
    guiManageEmail.ManageEmailPage(newWindow)

  def BackupPage():
    newWindow = Toplevel(root)
    newWindow.title("Backup Page")
    newWindow.geometry("250x600")
    guiBackupPage.BackupPage(newWindow)
  
  def EditCatPage():
    newWindow = Toplevel(root)
    newWindow.title("Category Manager Page")
    newWindow.geometry("250x600")
    guiEditCatPage.EditCatReminder(newWindow)

  def MainPage():
    def refreshMain():
      mainWindow.destroy()
      GuiStart.MainPage()
    mainWindow = Toplevel(root)
    mainWindow.title("Reminder")
    mainWindow.geometry("250x600")
    mainWindow.configure(background="white")
    frame = Frame(mainWindow)
    frame.pack(fill = "x")
    frame.config(bg="white")
    bottomframe = Frame(mainWindow)
    bottomframe.pack()
    tk.Button(frame,text="@",font=("Arial", 8,"bold"),fg="white",bg="#1c768f",command = refreshMain).pack(side = RIGHT)
    tk.Button(frame,text="Backup",font=("Arial", 8 ,'bold')
    ,command = GuiStart.BackupPage).pack(side = LEFT)
    tk.Button(frame,text="Statis",font=("Arial", 8 ,'bold')
    ,command = GuiStart.StatisticsPage).pack(side = LEFT)

    guiMainPage.MainPage(mainWindow)

    tk.Button(mainWindow,text="Email",font=("Arial", 8),fg="white",bg="#fa991c",command = GuiStart.ManageEmailPage).pack(anchor=E)
    tk.Button(mainWindow,text="add todo",font=("Arial", 8),fg="white",bg="#1c768f",command = GuiStart.callguiTopic).pack(anchor=E)
  
  def __init__(self):
    #os.system('clear')
    root.wm_state('iconic')
    GuiStart.MainPage()

root = tk.Tk()
app = GuiStart()
root.mainloop()


