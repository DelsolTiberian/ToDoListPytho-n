from customtkinter import *
from tkinter import PhotoImage 
from tkinter import simpledialog
from main import Task





#Creation des taches
def addTask():
    popUp=CTk()
    popUp.title("To Do List")
    popUp.geometry("300x100")
    popUp.minsize(300, 100)
    popUp.maxsize(300, 100)
    #Name Definition
    instruction= CTkLabel(master=popUp, text="Enter your task's name")
    instruction.pack()
    entryName=CTkEntry(master=popUp)
    entryName.pack()
    #Probleme command
    finishButton=CTkButton(master=popUp, text="Create", command= createTask(entryName.get(), popUp)) #Ne Marche pas du tout 
    finishButton.pack()

    popUp.mainloop()

def createTask(name, window):
    Task.tasks.append(Task(name))
    window.destroy()

    



#Creation De la fenêtre

set_appearance_mode("dark")
mainPanel= CTk()
mainPanel.title("To Do List")
mainPanel.geometry("750x500")
mainPanel.minsize(500, 350)


#Widgets

titleFont = CTkFont(family="Helvetica", size=40)

mainFrame= CTkFrame(master=mainPanel, width=600)
mainFrame.pack(padx=30, pady=20, fill="both", expand= True)

title= CTkLabel(master=mainFrame, pady=40, text="To Do List", font=titleFont)
title.pack()

addTaskButton= CTkButton(master= mainFrame, text="New Task", command=addTask)
addTaskButton.pack()





mainPanel.mainloop()

addTask()