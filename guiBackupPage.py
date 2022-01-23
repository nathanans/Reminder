import GUI
import EmailManager
import tkinter as tk
import BackupManager
from tkinter import *
class BackupPage:
  def Page(root):
    def refreshMain(): 
      root.destroy()
    def refreshBackupPage():
      root.destroy()
      GUI.GuiStart.BackupPage()
    ##1c768f
    def Export():
      if BackupManager.BackupReminder.alreadyExported(PathEx.get(),emailEx.get()):
        def ok(): #back to main
          ComfirmWindow.destroy()
        def overWrite():
          BackupManager.BackupReminder.Export(emailEx.get(),PathEx.get())
          ComfirmWindow.destroy()
          refreshBackupPage()
        ComfirmWindow = Toplevel(root)
        ComfirmWindow.title("Null input")
        ComfirmWindow.geometry("300x100")
        labelBonus = tk.Label(ComfirmWindow, text="\n\n***** There are same Email already EXPORT. *****",font=("Arial", 8),fg="#8B0000")
        labelBonus.pack()
        frame = Frame(root)
        frame.pack()
        bottomframe = Frame(root)
        bottomframe.pack()
        tk.Button(ComfirmWindow,text="OK",font=("Arial", 8),command = ok).pack(side= RIGHT)
        tk.Button(ComfirmWindow,text="Over Write",font=("Arial", 8),command = overWrite).pack(side=RIGHT)
      else:
        BackupManager.BackupReminder.Export(emailEx.get(),PathEx.get())
        refreshBackupPage()
      
    tk.Button(root,text="Back",font=("Arial", 8),fg="white",bg="#1c768f",command = refreshMain).pack(anchor=E)

    tk.Label(root,text ="Export User",font=("Arial", 8,'bold')).pack()
    tk.Label(root,text ="**Export to JSON file**",font=("Arial", 8)).pack()

    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
    
    tk.Label(frame,text="Export to.",font=("Arial", 7)).pack(side=LEFT)
    oldDirec = BackupManager.BackupReminder.getfileDirect()
    PathEx = StringVar()
    PathEx.set(oldDirec[0])
    dropemail = OptionMenu(frame, PathEx,*oldDirec)
    dropemail["menu"].config(font=("Arial", 7))
    dropemail.config(font=("Arial", 7))
    dropemail.pack(side = LEFT)

    def addDirec():
      print("0")
      def ok(): #back to main
        ComfirmWindow.destroy()
      def addDirec():
        BackupManager.BackupReminder.addDirec(newFolder.get())
        ComfirmWindow.destroy()
        refreshBackupPage()
      ComfirmWindow = Toplevel(root)
      ComfirmWindow.title("Null input")
      ComfirmWindow.geometry("300x100")
      tk.Label(ComfirmWindow, text="\nEnter New Folder Name.\n",font=("Arial", 8),fg="#8B0000").pack()
      newFolder = StringVar()
      tk.Entry(ComfirmWindow,textvariable=newFolder,font=("Arial", 7)).pack()

      frame = Frame(ComfirmWindow)
      frame.pack()
      bottomframe = Frame(ComfirmWindow)
      bottomframe.pack()
      tk.Button(frame,text="Cancle",font=("Arial", 8),command = ok).pack(side= RIGHT)
      tk.Button(frame,text="Add",font=("Arial", 8),command = addDirec).pack(side=RIGHT)

    tk.Button(frame,text="Add Folder",font=("Arial", 6,"bold"),command = addDirec).pack(side = RIGHT)
    #tk.Label(frame,text=" Export to.",font=("Arial", 7)).pack(side=LEFT)
    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
  
    tk.Label(frame,text="Email : ",font=("Arial", 7)).pack(side=LEFT)
    syncEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    emailEx = StringVar()
    emailEx.set(syncEmail[0])
    dropemail = OptionMenu(frame, emailEx,*syncEmail)
    dropemail["menu"].config(font=("Arial", 7))
    dropemail.config(font=("Arial", 7))
    dropemail.pack(side = LEFT)
    tk.Button(root,text="EXPORT",font=("Arial", 7, 'bold'),fg = "white",bg="#fa991c",command = Export).pack()

    def Import():
      if BackupManager.BackupReminder.checkForm(importFile.get())==False:
        def ok():
          ComfirmWindow.destroy()
        ComfirmWindow = Toplevel(root)
        ComfirmWindow.title("Error Input")
        ComfirmWindow.geometry("300x100")
        labelBonus = tk.Label(ComfirmWindow, text="\n***** This file is Invalid format *****\n",font=("Arial", 8),fg="#8B0000")
        labelBonus.pack()
        tk.Button(ComfirmWindow,text="OK",font=("Arial", 8),fg="white",bg="#e83845",command = ok).pack()
      if BackupManager.BackupReminder.alreadyImported(importFile.get()):
        def ok():
          ComfirmWindow.destroy()
        def overWrite():
          BackupManager.BackupReminder.Import(importFile.get())
          ComfirmWindow.destroy()
          refreshBackupPage()
        ComfirmWindow = Toplevel(root)
        ComfirmWindow.title("Are you sure?")
        ComfirmWindow.geometry("300x100")
        labelBonus = tk.Label(ComfirmWindow, text="\n\n***** There are same Email already Used in this Device. *****",font=("Arial", 8),fg="#8B0000")
        labelBonus.pack()
        frame = Frame(root)
        frame.pack()
        bottomframe = Frame(root)
        bottomframe.pack()
        tk.Button(ComfirmWindow,text="OK",font=("Arial", 8),command = ok).pack(side= RIGHT)
        tk.Button(ComfirmWindow,text="Over Write",font=("Arial", 8),command = overWrite).pack(side=RIGHT)
      else:
        BackupManager.BackupReminder.Import(importFile.get())
        refreshBackupPage()

    tk.Label(root,text="\nImport User",font=("Arial", 8,'bold')).pack()
    
    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()

    importFileondevice = BackupManager.BackupReminder.getfileDirectForImport()
    
    tk.Label(frame,text="Import Form : ",font=("Arial", 7)).pack(side=LEFT)
    importFile = StringVar()
    importFile.set(importFileondevice[0])
    dropemail = OptionMenu(frame, importFile,*importFileondevice)
    dropemail["menu"].config(font=("Arial", 7))
    dropemail.config(font=("Arial", 7))
    dropemail.pack(side = LEFT)

    tk.Button(root,text="IMPORT",font=("Arial", 6, 'bold'),fg="white",bg="#fa991c",command = Import).pack()


  def __init__(self,root):
    self.l=[]
    BackupPage.Page(root)
    
  