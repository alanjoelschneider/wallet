import tkinter as tk
from tkinter import ttk

class BooleanButtons(ttk.Frame):
  def __init__(self, master, command, padding=(0, 20, 0, 0), truebuttontext="Ok", falsebuttontext="Cancel"):
    super().__init__(master, padding=padding)
    self.command = command
    self._initWidgets(truebuttontext, falsebuttontext)

  def _initWidgets(self, truebuttontext, falsebuttontext):
    self.yesButton = ttk.Button(self, text=truebuttontext, command=lambda:self._handle(True))
    self.yesButton.grid(column=0, row=0, sticky=tk.W)
    self.yesButton.focus()
    
    self.noButton = ttk.Button(self, text=falsebuttontext, command=lambda:self._handle(False))
    self.noButton.grid(column=1, row=0, sticky=tk.W, padx=(5, 0))

  def _handle(self, boolean):
    self.command(boolean)