import tkinter as tk
from tkinter import ttk
from app import App
from wallet import Wallet
from history import History

from db import user
from db import movement

from menu import newWallet

def handleNewWallet(userController):
  confirm, name = newWallet.NewWallet.open()
  if confirm:
    userController.create(1, name)

def main():
  userController = user.UserController()
  movementController = movement.MovementController()

  # userController.createTable()

  app = App("Wallet app")

  menubar = tk.Menu(app)
  app.configure(menu=menubar)
  menuadd = tk.Menu(menubar, tearoff=0)

  menuadd.add_command(label="Add wallet", command=lambda: handleNewWallet(userController))
  menuadd.add_separator()
  menuadd.add_command(label="Exit", command=app.quit)
  menubar.add_cascade(label="File", menu=menuadd)

  container = ttk.Frame(app, padding=5)
  container.pack()

  Wallet(container).grid(column=0, row=0, sticky=tk.W)

  history = History(container)
  history.grid(column=0, row=1, pady=(5, 0))

  # movements = movementController.getAll()
  # history.setData(movements)

  app.mainloop()

if __name__ == "__main__":
  main()