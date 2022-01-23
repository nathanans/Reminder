from tkinter import *
import tkinter as tk
import todoManager
import EmailManager
from tkcalendar import *
from datetime import datetime
import GUI
import categoryManager
import guiEditCat


class EditPage:
  catList = []
 
  def Start(self,root):

    ################################
    def getTopic():
      message = topicGet.get()
      return message

    ####################################
    def SelectPriority():
      prioritylevel = clicked.get()
      return prioritylevel
    
    ########################################
    def getDescript():
      descript = Des.get()
      return descript

    #########################################

    def selectDate():
      dateget = cal.get_date()
      datenew = datetime.strptime(dateget, "%m/%d/%y").strftime("%d/%m/%Y")
      
      return str(datenew)
    
    #######################################

    def selectTime():
      h = hoursb.get()
      m = minsb.get()
      s = sec.get()
      timeget = f"{h}:{m}:{s}"
      return str(timeget)
        
    #########################################
    def selectEmail():
      email_s = emailSelect.get()
      return email_s
    
    ###################################################

    def delbackTomain():
      popask = Toplevel(root)
      popask.title("Delete topic")
      popask.geometry("200x100")
      poplabel = Label(popask, text="Are you sure?",font=("Arial", 5))
      poplabel.pack()
      def deletethis():
        categoryManager.categoryReminder.deleteCatWhenDeleteEmail(detail)
        todoManager.todoReminder.deleteByAddress("Email",detail)
        popask.destroy()
        root.destroy()
      def BackToEditPage():
        popask.destroy()
      frame = Frame(popask)
      frame.pack()
      bottomframe = Frame(popask)
      bottomframe.pack()
      btnY = Button(frame,text="Yes",font=("Arial", 5),command = deletethis)
      btnY.pack(side = LEFT)
      btnN = Button(frame,text="No",font=("Arial", 5),command = BackToEditPage)
      btnN.pack(side = LEFT)

    def SaveTodo():
        topic = getTopic()
        priority = SelectPriority()
        descript = getDescript()
        email = selectEmail()  
        dateget = selectDate() 
        timeget = selectTime()
        Category = EditPage.catList
        todoManager.todoReminder.editTodoGui(self,detail[1],topic, priority, descript, email, dateget, timeget,detail[0])
        
        #(self,curTime, topic,Priority, description, toEmail, DateSet,TimeSet,oldEmail)
        categoryManager.categoryReminder.addTodoCat([email,detail[1]],Category)
        root.destroy()
        
    def Back():
      root.destroy()

    def editcat(): 
      editCatwin = Toplevel(root)
      editCatwin.title('Categories')
      editCatwin.geometry("250x600")
      n=[detail[0],detail[1]]
      guiEditCat.editCategoryPage.EditCat(editCatwin,n)
    
    
    detail = self.k #address = [email,cur]
    detailList = todoManager.todoReminder.getTodoDetail(detail)
    
    emailclicked = detail[0]
    curtime = detail[1]
    topicGet = StringVar()    
    
    backbt = Button(root, text= "Back",font=("Arial", 5),fg="white",bg="#1c768f", command = Back)
    backbt.pack(anchor=NE)

    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
    label_tp = Label(frame,text="Topic : ",font=("Arial", 7))
    label_tp.pack(anchor = W)
    topicGet = StringVar()    
    Topic = Entry(frame,textvariable=topicGet,font=("Arial", 7))
    Topic.pack(side = LEFT)
    
    oldTopic = detailList[0]
    Topic.insert(0,oldTopic)
    Topic.pack()
    
    level = [0,1,2,3]
    clicked = StringVar()
    clicked.set(detailList[1])
    
    label_pr = Label(frame,text="Priority : ",font=("Arial", 7)).pack(side = LEFT)
    dropPriority = tk.OptionMenu(frame , clicked,*level)
    dropPriority["menu"].config(font=("Arial", 7))
    dropPriority.config(font=("Arial", 7))
    dropPriority.pack(side = LEFT)
    
    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
    label_de = Label(frame,text="Description : ",font=("Arial", 7)).pack(anchor = W)
    Des = StringVar()
    Description = Entry(frame,textvariable= Des,font=("Arial", 7))
    oldDescrpit = detailList[2]
    Description.insert(0,oldDescrpit)
    Description.pack(fill = "x")
    label_pr = Label(frame,text="Calendar : ",font=("Arial", 7)).pack(side = LEFT)

    oldDateSet = detailList[3]
    oldDateTime = oldDateSet.split(" ")
    tmp = oldDateTime[0]+" "+oldDateTime[1]
    getDateOld = datetime.strptime(tmp,"%d/%m/%Y %H:%M:%S")
    oldTime = oldDateTime[1].split(":")

    getHour = StringVar()
    getMin = StringVar()
    getSec = StringVar()

    getHour.set(oldTime[0])       
    getMin.set(oldTime[1])
    getSec.set(oldTime[2])

    #แสดงdefault
    cal= Calendar(root,font=("Arial", 7), selectmode="day",year= getDateOld.year, month=getDateOld.month, day=getDateOld.day)
    cal.pack(fill = "x")

    datebutton= Button(root, text= "Set Date",font=("Arial", 7), command = selectDate)
    datebutton.pack()

    f1 = Frame(root)
    f2 = Frame(root)
    label_time = Label(f2,text="Time : ",font=("Arial", 5)).pack()
    f1.pack()
    f2.pack()
    hoursb = Spinbox(f2 , from_= 0 , to = 23 , wrap = True ,textvariable = getHour ,width = 5,state ="readonly", justify = CENTER)
    minsb = Spinbox(f2 ,from_= 0, to = 59, wrap = True, textvariable = getMin , width = 5, state ="readonly",justify=CENTER)
    sec = Spinbox(f2 ,from_= 0, to = 59, wrap = True, textvariable= getSec, width = 5, state ="readonly",justify=CENTER)

    hoursb.pack(side=LEFT, fill=X, expand=True)
    minsb.pack(side=LEFT, fill=X, expand=True)
    sec.pack(side=LEFT, fill=X, expand=True)


    timebutton= Button(f2, text= "Set Time",font=("Arial", 7) ,command= selectTime)
    timebutton.pack(side=LEFT)
    
    frame = Frame(root)
    frame.pack(anchor = W,fill = "x")
    bottomframe = Frame(root)
    bottomframe.pack()
    
    label_email = Label(frame,text="Email : ",font=("Arial", 7)).pack(anchor=W)

    syncEmail = EmailManager.EmailReminder.getEmail("User","e-mailUsed")
    emailSelect = StringVar()
    emailSelect.set(emailclicked)
    dropemail = OptionMenu(frame, emailSelect,*syncEmail)
    dropemail["menu"].config(font=("Arial", 7))
    dropemail.config(font=("Arial", 7))
    dropemail.pack(side = LEFT)
    tk.Button(frame,text="Select Email",font=("Arial", 7),command = selectEmail).pack(side = LEFT)

    tk.Button(root, text="Category",font=("Arial", 7),command = editcat).pack()

    fDelEdit = Frame(root)
    fDelEdit.pack()
    bottom = Frame(root)
    bottom.pack()
    Deletebt = Button(fDelEdit,text="Delete",font=("Arial", 7,'bold'),fg="white",bg="#e83845",command = delbackTomain).pack(side = LEFT)
    editbt = Button(fDelEdit,text="Edit",font=("Arial", 7,'bold'),command= SaveTodo).pack(side = RIGHT)

  def __init__(self,root,k):
    self.l = root
    self.k = k
    EditPage.Start(self,root)
    ####################--------------------------------####################