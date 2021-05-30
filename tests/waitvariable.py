import tkinter as tk
from tkinter import ttk


def main():
  app = tk.Tk()
  app.title("Testing")
  app.resizable(False, False)

  result = tk.BooleanVar()
  
  button = ttk.Button(app, text="Ok", command=lambda:result.set(True))
  button.grid(column=0, row=0)

  button.wait_variable(result)

  print(result)

  app.mainloop()

if __name__ == "__main__":
  main()