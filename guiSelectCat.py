import GUI
import categoryManager
import guiwriteTopic
from tkinter import *
import tkinter as tk

class CategoryPage:
  
  Catselect = []
  
  def ChooseCat(root) :
    
    def BackToMain() :
      root.destroy()
    
    def refresh() :
      root.destroy()
      GUI.GuiStart.callguiCat()
    
    allcat = categoryManager.categoryReminder.getCatKey() 
    allcat.remove("All")
    
    def showText(d):
      if d in CategoryPage.Catselect:
        CategoryPage.Catselect.remove(d) 
      else:
        CategoryPage.Catselect.append(d)
      refresh()
    
    def catNotselected():
      tk.Label(root,text ="Not Selected",font=("Arial", 8)).pack()
      n=0
      for i in allcat :
        if i in CategoryPage.Catselect:
          continue
        tk.Button(root,text = i,font=("Arial", 8),command = lambda m = i : showText(m)).pack()
        n+=1
    def catSelected():
      tk.Label(root,text ="Selected",font=("Arial", 8)).pack()
      n=0
      for i in CategoryPage.Catselect :
        tk.Button(root,text = i,font=("Arial", 8),command = lambda m = i : showText(m)).pack()
        n+=1
    tk.Button(root,text="Back",font=("Arial", 8),fg="white",bg="#1c768f",command = BackToMain).pack(anchor=E)
       
    tk.Label(root,text = "-----Categories-----",font=("Arial", 8)).pack()
    def getCatselect():
      guiwriteTopic.TopicPage.catList = CategoryPage.Catselect
      root.destroy()
    
    catNotselected()
    catSelected()
    
    tk.Button(root,text = "Save",font=("Arial", 8),fg = "white",bg = "#fa991c",command =getCatselect).pack()
    

  def __init__(self,root):
    self.l = []
    CategoryPage.ChooseCat(root)
    