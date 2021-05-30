from db import db

class UserController(db.Db):
  def __init__(self):
    super().__init__()

  def createTable(self):
    sql = """
      CREATE TABLE IF NOT EXISTS user (
        id integer PRIMARY KEY,
        name text NOT NULL,
        lastname text NOT NULL,
        money text NOT NULL
      );
    """
    conn = self.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

  def dropTable(self):
    sql = """
      DROP TABLE user;
    """
    conn = self.connect()
    cursor = cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

  def create(self, name, lastname, money):
    sql = """
      INSERT INTO user(id, name, lastname, money)
      VALUES (?, ?, ?, ?);
    """
    id = self._getNextId()
    conn = self.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id, name, lastname, money))
    conn.commit()
    return cursor.lastrowid

  def updateMoneyById(self, id, money):
    sql = """
      UPDATE user
      SET money = (?)
      WHERE id = (?);
    """
    conn = self.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id, money))
    conn.commit()
    return cursor.lastrowid

  def getMoneyById(self, id):
    sql = """
      SELECT money FROM user
      WHERE id = (?);
    """
    return self.connect().cursor().execute(sql, (id,)).fetchone()[0]

  def getAll(self):
    sql = """
      SELECT * FROM user;
    """
    return self.connect().cursor().execute(sql).fetchall()

  def getById(self, id):
    sql = """
      SELECT * FROM user
      WHERE id == (?);
    """
    return self.connect().cursor().execute(sql, (id,)).fetchone()

  def _getNextId(self):
    sql = """
      SELECT max(id) FROM user;
    """
    lastUserId = self.connect().cursor().execute(sql).fetchone()[0]
    if not lastUserId:
      return 1
    return lastUserId + 1