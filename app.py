import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
  def __init__(self, title):
    super().__init__()
    self.title(title)
    self.resizable(False, False)

  def quit(self):
    self.destroy()
