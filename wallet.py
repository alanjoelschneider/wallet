import tkinter as tk
from tkinter import ttk
from formatters import Formatters
from tkinter.messagebox import askyesno
from texts import Texts

class Wallet(tk.Frame):
  def __init__(self, master):
    super().__init__(master)
    self._initVars()
    self._initWidgets()
    self.moneyEntryVar.trace_add("write", self.format)

  def _initVars(self):
    self.totalMoneyVar = tk.StringVar(value="0.00")
    self.moneyEntryVar = tk.StringVar(value="")

  def _initWidgets(self):
    self.totalMoneyTitleLabel = ttk.Label(self, text="Available money (USD)")
    self.totalMoneyTitleLabel.grid(column=0, row=0, sticky=tk.W)

    self.totalMoneyLabel = ttk.Label(self, textvariable=self.totalMoneyVar)
    self.totalMoneyLabel.grid(column=0, row=1, sticky=tk.W)

    self.moneyEntry = ttk.Entry(self, textvariable=self.moneyEntryVar)
    self.moneyEntry.grid(column=0, row=2)

    self.depositMoneyButton = ttk.Button(self, text="Deposit", command=self.deposit)
    self.depositMoneyButton.grid(column=1, row=2, padx=(5,0))
    
    self.moneyButton = ttk.Button(self, text="Withdraw", command=self.withdraw)
    self.moneyButton.grid(column=2, row=2, padx=(5,0))

    self.moneyButton = ttk.Button(self, text="Send", command=self.send)
    self.moneyButton.grid(column=3, row=2, padx=(5,0))

  def deposit(self):
    message = Texts.walletDepositAskMessage.format(self.moneyEntryVar.get())
    answer = askyesno(
      title='Deposit money',
      message=message)
    if answer:
      toDeposit = Formatters.usdToFloat(self.moneyEntryVar.get())
      totalMoney = Formatters.usdToFloat(self.totalMoneyVar.get())
      self.totalMoneyVar.set(Formatters.floatToUsd(totalMoney + toDeposit))
      self.moneyEntryVar.set("")
      print("deposited")

  def send(self):
    top= tk.Toplevel(self)
    top.title("Send Money")
    self.totalMoneyVar.set(self.moneyEntryVar.get())
    self.moneyEntryVar.set("")

  def withdraw(self):
    message = Texts.walletWithdrawAskMessage.format(self.moneyEntryVar.get())
    answer = askyesno(
      title='Withdraw money',
      message=message)
    if answer:
      toWithdraw = Formatters.usdToFloat(self.moneyEntryVar.get())
      totalMoney = Formatters.usdToFloat(self.totalMoneyVar.get())
      self.totalMoneyVar.set(Formatters.floatToUsd(totalMoney - toWithdraw))
      self.moneyEntryVar.set("")

  def format(self, *args):
    formatted = Formatters.usd(self.moneyEntryVar.get())
    self.moneyEntryVar.set(formatted)
    self.moneyEntry.delete(0, tk.END)
    self.moneyEntry.insert(0, formatted)

  def setMoney(self, money):
    self.totalMoneyVar.set(money)
