from db import db

class MovementController(db.Db):
  def __init__(self):
    super().__init__()

  def createTable(self):
    sql = """
      CREATE TABLE IF NOT EXISTS movement (
        id integer PRIMARY KEY,
        from_id integer NOT NULL,
        to_id integer NOT NULL,
        amount integer NOT NULL,
        description text NOT NULL,
        date text NOT NULL,
        FOREIGN KEY (from_id) REFERENCES user (id),
        FOREIGN KEY (to_id) REFERENCES user (id)
      );
    """
    conn = self.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

  def dropTable(self):
    sql = """
      DROP TABLE movement;
    """
    conn = self.connect()
    cursor = cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

  def create(self, id, from_id, to_id, amount, description):
    sql = """
      INSERT INTO movement(id, from_id, to_id, amount, description, date)
      VALUES (?, ?, ?, ?, ?, datetime("now", "localtime"));
    """
    conn = self.connect()
    cursor = conn.cursor()
    cursor.execute(sql, (id, from_id, to_id, amount, description))
    conn.commit()
    return cursor.lastrowid

  def getAll(self):
    sql = """
      SELECT * FROM movement;
    """
    return self.connect().cursor().execute(sql).fetchall()

  def getById(self, id):
    sql = """
      SELECT * FROM movement
      WHERE id == (?);
    """
    return self.connect().cursor().execute(sql, (id,)).fetchone()