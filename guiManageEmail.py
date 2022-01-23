import GUI
import EmailManager
import tkinter as tk
from tkinter import *
class ManageEmailPage:
  def Page(root):
    def BackToMain(): #back to main
      root.destroy()
    def refreshThislPage():
      root.destroy()
      GUI.GuiStart.ManageEmailPage()
    ##1c768f
    tk.Button(root,text="Back",font=("Arial", 8),fg="white",bg="#1c768f",command = BackToMain).pack(anchor=E)
    
    usedEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    syncEmailPage = EmailManager.EmailReminder.getEmail("SynceEmail","Sync")
    CBEmailUnsync = [BooleanVar() for i in usedEmail]
    emailtosync = []
    def unsyncEmail():
      tk.Label(root,text ="Not sync Email",font=("Arial", 8)).pack()
      emailTmp = []
      for i in usedEmail:
        if i in syncEmailPage:
          continue
        emailTmp.append(i)
      n=0
      for i in emailTmp:
        tk.Checkbutton(root, text=i,font=("Arial", 8),anchor='w',fg="black",bg="white",variable=CBEmailUnsync[n],command=syncEmail).pack(fill = "x")
        emailtosync.append(i)
        n+=1
      for i,j in zip(CBEmailSync,emailtounsync):
        if i.get() == True :
          i.set(False)
          EmailManager.EmailReminder.unsyncEmail(j)
          refreshThislPage()
    CBEmailSync = [BooleanVar() for i in usedEmail ]
    emailtounsync = []
    def syncEmail():
      tk.Label(root,text ="Synced Email",font=("Arial", 8)).pack()
      n=0
      for i in usedEmail:
        if i in syncEmailPage:
          emailtounsync.append(i)
          tk.Checkbutton(root, text=i,font=("Arial", 8),anchor='w',fg="black",bg="white",variable=CBEmailSync[n],command=unsyncEmail).pack(fill = "x")
          n+=1
      for i,j in zip(CBEmailUnsync,emailtosync):
        if i.get() == True :
          i.set(False)
          EmailManager.EmailReminder.syncEmail(j)
          refreshThislPage()

    def deletEmail():
      def Comfirm():
        def cancle():
          ComfirmWindow.destroy()
        def deleteEmailCom():
          EmailManager.EmailReminder.deletEmail(emailSelect.get())
          ComfirmWindow.destroy()
          refreshThislPage()
        ComfirmWindow = Toplevel(root)
        ComfirmWindow.title("Are you sure?")
        ComfirmWindow.geometry("300x100")
        labelBonus = tk.Label(ComfirmWindow, text="\n"+str(emailSelect.get())+"\n***** If you delet this Email all data will gone. *****\n",font=("Arial", 8),fg="#8B0000")
        labelBonus.pack()
        tk.Button(ComfirmWindow,text="DELETE",font=("Arial", 8),fg="white",bg="#e83845",command = deleteEmailCom).pack()
        tk.Button(ComfirmWindow,text="CANCLE",font=("Arial", 8),fg="white",bg="gray",command = cancle).pack()
      tk.Label(root,text ="Delete Email",font=("Arial", 8)).pack(anchor=W)
      Email = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
      Email.remove("Anonymous")
      emailSelect = StringVar()
      emailSelect.set(Email[0])
      frame = Frame(root)
      frame.pack()
      bottomframe = Frame(root)
      bottomframe.pack()
      dropemail = OptionMenu(frame, emailSelect,*Email)
      dropemail.config(font=("Arial", 7),bg = "white")
      dropemail["menu"].config(font=("Arial", 7),bg = "white")
      dropemail.pack(side = LEFT)
      tk.Button(frame,text="DELETE",font=("Arial", 7, 'bold'),fg="white",bg="#e83845",command = Comfirm).pack(side = RIGHT)

    def addEmail():
      def Comfirm():
        def OK():
          ComfirmWindow.destroy()
        ComfirmWindow = Toplevel(root)
        ComfirmWindow.title("Email Manager")
        ComfirmWindow.geometry("200x100")
        labelBonus = tk.Label(ComfirmWindow, text=str(newEmail.get())+"\n***** This Email is already used *****\n",font=("Arial", 8),fg="black").pack()
        tk.Button(ComfirmWindow,text="CANCLE",font=("Arial", 8),fg="white",bg="gray",command = OK).pack()
      def checkEmail():
        usedEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
        if newEmail.get() in usedEmail:
          Comfirm()
        else : 
          EmailManager.EmailReminder.addEmail(newEmail.get())
          refreshThislPage()
      tk.Label(root,text ="Add New Email",font=("Arial", 8)).pack(anchor=W)
      newEmail = StringVar()
      frame = Frame(root)
      frame.pack(fill = "x")
      bottomframe = Frame(root)
      bottomframe.pack(fill = "x")
      tk.Entry(frame,textvariable=newEmail,font=("Arial", 7)).pack(fill = "x")
      tk.Button(frame,text="Add Email",font=("Arial", 7, 'bold'),fg="white",bg="#fa991c",command = checkEmail).pack(side = RIGHT)
      
    syncEmail()
    unsyncEmail()
    addEmail()
    deletEmail()

  def __init__(self,root):
    self.l=[]
    ManageEmailPage.Page(root)
    
  