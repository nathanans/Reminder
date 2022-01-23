import GUI
import categoryManager
import guiwriteTopic
from tkinter import *
import tkinter as tk
import main
import guiEditPage

class editCategoryPage:
    
  def EditCat(root,n):
    address = n
    Catselect = categoryManager.categoryReminder.catvalue(n) 
    
    allcat = categoryManager.categoryReminder.getCatKey()
    allcat.remove("All")
    
    def refresh(n):
      root.destroy()
      GUI.GuiStart.callguiEditCat(n)
      
    def showText(d): #d = Topic
        if d in catchoose:
          catchoose.remove(d)
          categoryManager.categoryReminder.deleteCatFormTodo(address,[d])
        else:
          catchoose.append(d) 
          categoryManager.categoryReminder.addTodoCat(address,[d])
        refresh(address)
    
    catNotchoose = []
    catchoose = [] 
    def catNotselected():
      tk.Label(root,text ="Not Selected",font=("Arial", 8)).pack()
      catOld =[]
      for i in allcat:
        if i in catchoose:
          continue
        catOld.append(i)
      n=0 
      for i in catOld :
        tk.Button(root,text = i,font=("Arial", 8),command = lambda m = i : showText(m)).pack()
        catNotchoose.append(i)
        n+=1

    def catSelected():
      tk.Label(root,text ="Selected",font=("Arial", 8)).pack()
      n=0
      for i in Catselect:
        catchoose.append(i)
        if i in catNotchoose:
          continue
        tk.Button(root,text = i,font=("Arial", 8),command = lambda m = i : showText(m)).pack()
        n+=1
        
        
    tk.Label(root,text = "-----Categories-----",font=("Arial", 8)).pack()
    def getCatselect():
      guiEditPage.EditPage.catList = catchoose
      root.destroy()
      
    catSelected()
    catNotselected()
    tk.Button(root,text = "Save",font=("Arial", 8),fg = "white",bg = "#fa991c",command =getCatselect).pack()
    

  def __init__(self,root,n):
    self.l = []
    self.n = n
    editCategoryPage.EditCat(root,n)