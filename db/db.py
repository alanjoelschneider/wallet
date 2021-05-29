import sqlite3

class Db:
  def connect(self):
    connection = None
    try:
      connection = sqlite3.connect("wallet.db")
    except sqlite3.Error as e:
      print(e)
    return connection