import tkinter as tk
from tkinter import ttk

class History(ttk.Treeview):
  def __init__(self, master):
    columns = ("#1", "#2", "#3", "#4", "#5", "#6")
    super().__init__(master, columns=columns, show="headings", height=15)
    self.heading("#1", text="Id")
    self.heading("#2", text="From")
    self.heading("#3", text="To")
    self.heading("#4", text="Mount")
    self.heading("#5", text="Description")
    self.heading("#6", text="Date")
    self.column("#1", minwidth=50, width=50, stretch=False) 
    self.column("#2", minwidth=50, width=50, stretch=False) 
    self.column("#3", minwidth=50, width=50, stretch=False) 
    self.column("#4", minwidth=50, width=50, stretch=False) 
    self.column("#5", minwidth=50, width=150, stretch=False) 
    self.column("#6", minwidth=50, width=150, stretch=False) 

  def _mock(self):
    # generate sample data
    contacts = []
    for n in range(1, 100):
      contacts.append((f'from {n}', f'to {n}', f'email{n}@example.com'))

    for contact in contacts:
      self.insert('', tk.END, values=contact)

  def setData(self, data):
    for values in data:
      self.insert('', tk.END, values=values)