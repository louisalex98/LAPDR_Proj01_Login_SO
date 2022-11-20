import sys
from tkinter import *
from tkinter import ttk, messagebox
import random

from pymongo import MongoClient


class View():
    
    def __init__(self):
        
        
        global random_states 
        random_states = ["ready", "wait", "running"] 

        self.connect()
        self.container()

    def connect(self):
        client = MongoClient("mongodb://localhost:27017/")
        mydb = client["operationalsystemsdb"]
        self.mydb = mydb
        dblist = client.list_database_names()
        if "operationalsystemsdb" in dblist:
            print("The database exists.")
        else:
            print("Not found")

    def show(self):
        
        mycol = self.mydb["programs"]
        self.list = []
        
        for x in mycol.find({},{ "_id": 0, "pid": 1, "uid": 1, "program":1}):
            y = list(x.values())
            y.append(self.random_state())
            
              
            if y[3] == "running":
                
                y.append(self.random_cpu())
                y.append(self.random_ram())
                
            else:       
                y.append("0%")
                y.append(self.random_ram())
            
            
            self.list.append(y)
            
            
                
        for i, (pid,uid,program,state,cpu,ram) in enumerate(self.list, start=1):
            self.listBox.insert("", "end", values=(program,uid,pid,cpu,ram,state))

        
        
    def random_cpu(self):
        random_cpu1 = random.randrange(1,100)
        cpu = str(random_cpu1) + "%"
        
        return(cpu)
    
    def random_ram(self):
        random_ram1 = random.randrange(100,8000)
        ram = str(random_ram1)
        
        return(ram)
        
    
    def random_state(self):
        
        if len(random_states) == 3:
            state = random_states[random.randrange(0,3)]
            if state == "running":
                random_states.pop(2)
                return(state)
            else:
                
                return(state)
        else:
            state = random_states[random.randrange(0,2)]
            return(state)
             
    def treeview_sort_column(tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        
        
        
        
    def container(self):
        root = Tk()
        root.title("Process Control Block")
        root.geometry("650x650")
        root['bg'] = 'white'
        
        Label(root, text="Task Manager", fg="Black", font=("Helvetica", 20)).place(x=10, y=30)
        
        cols = ('Process Name','ID','PID', '%CPU','RAM','State')
        self.listBox = ttk.Treeview(root, columns=cols, show='headings')

        verscrlbar = ttk.Scrollbar(self.listBox,
                                   orient ="vertical",
                                   command = self.listBox.yview)

        horscrlbar = ttk.Scrollbar(self.listBox,
                                   orient ="horizontal",
                                   command = self.listBox.xview)

        for col in cols:
           self.listBox.heading(col, text=col, command=lambda: \
                            self.treeview_sort_column(self.listBox, col, False))
           self.listBox.place(x=10, y=100, width=600, height=450)

        self.listBox.column('Process Name', anchor=W, stretch=NO, width=130)
        self.listBox.column('ID', anchor=CENTER, stretch=NO, width=80)
        self.listBox.column('PID', anchor=CENTER, stretch=NO, width=180)
        self.listBox.column('%CPU', anchor=CENTER, stretch=NO, width=60)
        self.listBox.column('RAM', anchor=CENTER, stretch=NO, width=60)
        self.listBox.column('State', anchor=CENTER, stretch=NO, width=80)

        horscrlbar.pack(side ='bottom', fill ='x')
        verscrlbar.pack(side ='right', fill ='y')


        self.listBox.configure(xscrollcommand= horscrlbar.set)
        self.listBox.configure(yscrollcommand= verscrlbar.set)

        
        self.show()
        
        
        root.mainloop()

    def close(event=None):
      sys.exit()

v = View()