import tkinter as tk
from tkinter import ttk

from reusable import booleanButtons

class NewWallet(tk.Toplevel):
  def __init__(self):
    super().__init__()
    self.title("New wallet")
    self.resizable(False, False)
    self.resultVar = tk.BooleanVar()
    self._initWidgets()

  def _initWidgets(self):
    self.container = ttk.Frame(self, padding=10)
    self.container.pack()

    self.nameLabel = ttk.Label(self.container, text="Name:")
    self.nameLabel.grid(column=0, row=0, sticky=tk.W)
    
    self.lastnameLabel = ttk.Label(self.container, text="Lastname:")
    self.lastnameLabel.grid(column=0, row=1, sticky=tk.W)
    
    self.initialMoneyLabel = ttk.Label(self.container, text="Initial money:")
    self.initialMoneyLabel.grid(column=0, row=2, sticky=tk.W)

    self.nameEntry = ttk.Entry(self.container)
    self.nameEntry.grid(column=1, row=0, padx=(5, 0), pady=(10, 0))

    self.lastnameEntry = ttk.Entry(self.container)
    self.lastnameEntry.grid(column=1, row=1, padx=(5, 0), pady=(10, 0))

    self.initialMoneyEntry = ttk.Entry(self.container)
    self.initialMoneyEntry.grid(column=1, row=2, padx=(5, 0), pady=(10, 0))
    
    self.yesnoButtons = booleanButtons.BooleanButtons(self.container, self._handleBooleanButtons)
    self.yesnoButtons.grid(column=1, row=3)

  def _handleBooleanButtons(self, boolean):
    self.resultVar.set(boolean)

  def getResult(self):
    self.wait_variable(self.resultVar)
    result = self.resultVar.get()
    name = self.nameEntry.get()
    self.destroy()
    return (result, name)

  @staticmethod
  def open():
    return NewWallet().getResult()
