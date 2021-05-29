from db import db

class UserController(db.Db):
  def __init__(self):
    super().__init__()

  def createTable(self):
    sql = """
      CREATE TABLE IF NOT EXISTS user (
        id integer PRIMARY KEY,
        name text NOT NULL
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

  def create(self, id, name):
    sql = """
      INSERT INTO user(id, name)
      VALUES (?, ?);
    """
    conn = self.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id, name))
    conn.commit()
    return cursor.lastrowid

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