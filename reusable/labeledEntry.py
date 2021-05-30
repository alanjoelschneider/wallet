import tkinter as tk
from tkinter import ttk

class LabeledEntry(ttk.Frame):
  def __init__(self, master, labelText, padding=0):
    super().__init__(master, padding=padding)
    self._initWidgets(labelText)

  def _initWidgets(self, labelText):
    self.label = ttk.Label(self, text=labelText)
    self.label.grid(column=0, row=0, sticky=tk.W)

    self.entry = ttk.Entry(self, text=labelText)
    self.entry.grid(column=1, row=0, padx=(5, 0))

  def get(self):
    return self.entry.get()