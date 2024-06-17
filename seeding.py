import sqlite3

shops = [
  ( 'shop-a', 'firstname-a','slogan-a' ),
  ( 'shop-b', 'firstname-b','slogan-b' ),
  ( 'shop-c', 'firstname-c','slogan-c' ),
  ( 'shop-d', 'firstname-d','slogan-d' ),
  ( 'shop-e', 'firstname-e','slogan-e' ),
  ( 'shop-f', 'firstname-f','slogan-f' ),
  ( 'shop-g', 'firstname-g','slogan-g' ),
  ( 'shop-h', 'firstname-h','slogan-h' ),
  ( 'shop-i', 'firstname-i','slogan-i' ),
  ( 'shop-j', 'firstname-j','slogan-j' ),
  ( 'shop-k', 'firstname-k','slogan-k' )
]
treasures_data = [('treasure-a', 'turquoise', 200, '20.00', 2), ('treasure-d', 'azure', 100, '1001.00', 4), ('treasure-b', 'gold', 13, '500.00', 6), ('treasure-f', 'onyx', 56, '0.01', 5), ('treasure-h', 'carmine', 13, '6.90', 8), ('treasure-u', 'khaki', 3, '3.99', 9), ('treasure-e', 'onyx', 10865, '99999.99', 1), ('treasure-n', 'magenta', 13, '6.99', 10), ('treasure-i', 'burgundy', 11, '18.99', 11), ('treasure-c', 'gold', 13, '15.99', 3), ('treasure-r', 'silver', 89, '8.99', 10), ('treasure-j', 'mikado', 504, '2340.99', 2), ('treasure-g', 'carmine', 65, '0.59', 7), ('treasure-l', 'cobalt', 77, '6.99', 4), ('treasure-p', 'turquoise', 13, '987.99', 8), ('treasure-m', 'burgundy', 77, '5.99', 6), ('treasure-o', 'saffron', 13, '78.99', 7), ('treasure-k', 'magenta', 13, '23.99', 9), ('treasure-q', 'magenta', 1, '60.99', 1), ('treasure-s', 'silver', 9, '12.99', 5), ('treasure-t', 'mikado', 13, '41.99', 11), ('treasure-v', 'ivory', 3, '78.99', 3), ('treasure-w', 'silver', 13, '60.99', 2), ('treasure-x', 'cobalt', 234, '7.99', 4), ('treasure-y', 'saffron', 54, '2.99', 5), ('treasure-z', 'ivory', 90, '48.99', 6)]

def create_sqlite_database(filename):
    conn = None
    try:
        conn = sqlite3.connect(filename)
        print(sqlite3.sqlite_version)
    except sqlite3.Error as e:
        print("e in create db connection function", e)
    finally:
        if conn:
            conn.close()

def drop_tables():
    try:
        with sqlite3.connect('treasures.db') as conn:
            c = conn.cursor()
            c.execute('DROP TABLE IF EXISTS shops')
            c.execute('DROP TABLE IF EXISTS treasures')
            print("Table dropped")
            conn.commit()
            conn.close()
    except sqlite3.Error as e:
        print("Drop tables: ", e)

def create_tables():
    sql_statements=[""" 
CREATE TABLE shops(
		shop_id INTEGER PRIMARY KEY,
		shop_name TEXT NOT NULL,
		owner TEXT NOT NULL,
		slogan TEXT
	);
""", """
CREATE TABLE treasures(
		treasure_id INTEGER PRIMARY KEY,
		treasure_name TEXT NOT NULL,
		colour TEXT NOT NULL,
		age INTEGER NOT NULL,
		cost_at_auction INTEGER,
		shop_id INT, 
        FOREIGN KEY (shop_id)
            REFERENCES shops(shop_id)
	);
"""]
    try:
        with sqlite3.connect('treasures.db') as conn:
            c = conn.cursor()
            for statement in sql_statements:
                c.execute(statement)
            conn.commit()
    except sqlite3.Error as e:
        print("Create Tables: ", e)
  
def add_shops(conn, shops):
    sql = """INSERT INTO shops 
    (shop_name, owner, slogan)
   VALUES(?,?,?) """
    c = conn.cursor()
    c.executemany(sql,shops)
    conn.commit()
    return c.lastrowid

def add_treasure(conn, treasure):
    sql="""INSERT INTO treasures
		(treasure_name, colour, age, cost_at_auction, shop_id)
		VALUES(?,?,?,?,?)"""
    c = conn.cursor()
    c.execute(sql,treasure)
    conn.commit()
    return c.lastrowid

def insert_data():
    try:
        with sqlite3.connect('treasures.db') as conn:
            add_shops(conn, shops)
            for treasure in treasures_data:
                add_treasure(conn,treasure)
    except sqlite3.Error as e:
        print("e in insert_data", e)

if __name__ == '__main__':
    create_sqlite_database('treasures.db')
    drop_tables()
    create_tables()
    insert_data()