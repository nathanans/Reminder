import GUI
import categoryManager
import guiwriteTopic
from tkinter import *
import tkinter as tk
import main
import guiEditPage


class EditCatReminder:
  Catselect = []
  def EditCat(root) :
    def BackToMain(): #back to main
      root.destroy()
    def refresh() :
      root.destroy()
      GUI.GuiStart.EditCatPage() 
    allcat = categoryManager.categoryReminder.getCatKey()
    allcat.remove("All")
    
    def deleteCat(cat):
      categoryManager.categoryReminder.deleteCat([cat])
      refresh()
    def addCat():
      categoryManager.categoryReminder.addCat(newCat.get())
      refresh()
    def showCat():
      n=0
      for i in allcat :
        frame = Frame(root)
        frame.pack()
        frame.config()
        bottomframe = Frame(root)
        bottomframe.pack()
        if i in EditCatReminder.Catselect:
          continue
        tk.Button(frame,text = "X",font=("Arial", 7),fg="white",bg="#e83845",command = lambda m = i : deleteCat(m)).pack(side = RIGHT)
        tk.Button(frame,text = i,font=("Arial", 7)).pack(side = RIGHT)
        n+=1
    ##1c768f
    tk.Button(root,text="Back",font=("Arial", 8),fg="white",bg="#1c768f",command = BackToMain).pack(anchor=E)
    
    tk.Label(root,text = "-----Categories-----",font=("Arial", 8)).pack()
    #tk.Label(root,text ="Add New Category",font=("Arial", 8)).pack()
    newCat = StringVar()
    frame = Frame(root)
    frame.pack()
    bottomframe = Frame(root)
    bottomframe.pack()
    tk.Entry(frame,textvariable=newCat,font=("Arial", 7)).pack(side = LEFT)
    tk.Button(frame,text="Add",font=("Arial", 7, 'bold'),fg="white",bg="#fa991c",command = addCat).pack(side = LEFT)
    showCat()
    #catSelected()

  def __init__(self,root):
    self.l = []
    EditCatReminder.EditCat(root)