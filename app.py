import tkinter as tk
from tkinter import ttk
from window import Window
from wallet import Wallet
from history import History

from db import user
from db import movement

from menu import newWallet

class App:
  def __init__(self):
    self.userController = user.UserController()
    self.movementController = movement.MovementController()

    # self.userController.createTable()
    # self.userController.dropTable()

    self.window = Window("Wallet")
    self.menubar = tk.Menu(self.window)
    self.window.configure(menu=self.menubar)
    self.menuadd = tk.Menu(self.menubar, tearoff=0)

    self.menuadd.add_command(label="Add wallet", command=self._addWallet)
    self.menuadd.add_separator()
    self.menuadd.add_command(label="Exit", command=self.window.quit)
    self.menubar.add_cascade(label="File", menu=self.menuadd)

    self.container = ttk.Frame(self.window, padding=5)
    self.container.pack()

    self.wallet = Wallet(self.container)
    self.wallet.grid(column=0, row=0, sticky=tk.W)
    self.wallet.setMoney(self.userController.getMoneyById(1))

    self.userController.getMoneyById(1)

    history = History(self.container)
    history.grid(column=0, row=1, pady=(5, 0))

    # movements = movementController.getAll()
    # history.setData(movements)

    self.window.mainloop()

  def _addWallet(self):
    confirm, name, lastname, initialMoney = newWallet.NewWallet.open()
    if confirm:
      self.userController.create(name, lastname, initialMoney)