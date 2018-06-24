import sqlite3

from sqlite3 import Error


class DBManager:
    def __init__(self, dbpath: str):
        self.dbpath = dbpath

    def execute(self, command: str):
        db = None
        try:
            db = sqlite3.connect(self.dbpath)
            cursor = db.cursor()
            cursor.execute(command)
            db.commit()
        except Error as e:
            print(e)
        finally:
            db.close()

    def select_scalar(self, query: str):
        db = None
        result = None
        try:
            db = sqlite3.connect(self.dbpath)
            cursor = db.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            result = rows[0][0]
        except Error as e:
            print(e)
        finally:
            db.close()
        return result

    def recreate_tables(self):
        self.execute('DROP TABLE IF EXISTS badman')
        self.execute('''
            CREATE TABLE badman(
                badman_id INTEGER PRIMARY KEY AUTOINCREMENT,
                lastname TEXT NOT NULL,
                firstname TEXT NOT NULL,
                dob TEXT NOT NULL)
            ''')
        print('recreated badman')

        self.execute('DROP TABLE IF EXISTS goodman')
        self.execute('''
            CREATE TABLE goodman(
                goodman_id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE,
                login TEXT NOT NULL)
            ''')
        print('recreated goodman')

        self.execute('DROP TABLE IF EXISTS appartment')
        self.execute('''
            CREATE TABLE appartment(
                appartment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                city TEXT NOT NULL,
                street TEXT NOT NULL,
                building INTEGER NOT NULL,
                block INTEGER,
                entrance INTEGER,
                floor INTEGER,
                apptnumber INTEGER)            
            ''')
        print('recreated appartment')

        self.execute('DROP TABLE IF EXISTS violation_type')
        self.execute('''
                    CREATE TABLE violation_type(
                        violation_type_id INTEGER PRIMARY KEY,
                        violation_type TEXT NOT NULL)            
                    ''')
        print('recreated violation_type')

        self.execute('DROP TABLE IF EXISTS neigh_to_appt_complaint')
        self.execute('''
            CREATE TABLE neigh_to_appt_complaint(
                neigh_to_appt_complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                goodman_id INTEGER NOT NULL,
                appartment_id INTEGER NOT NULL,
                complaint_date TEXT NOT NULL,
                violation_date TEXT NOT NULL,
                violation_type_id INTEGER NOT NULL,
                violation_text TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY(goodman_id) REFERENCES goodman(goodman_id),
                FOREIGN KEY(appartment_id) REFERENCES appartment(appartment_id),
                FOREIGN KEY(violation_type_id) REFERENCES violation_type(violation_type_id))            
            ''')
        print('recreated neigh_to_appt_complaint')

        self.execute('DROP TABLE IF EXISTS neigh_to_roommate_complaint')
        self.execute('''
            CREATE TABLE neigh_to_roommate_complaint(
                neigh_to_roommate_complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                goodman_id INTEGER NOT NULL,
                badman_id INTEGER NOT NULL,
                complaint_date TEXT NOT NULL,
                violation_date TEXT NOT NULL,
                violation_type_id INTEGER NOT NULL,
                violation_text TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY(goodman_id) REFERENCES goodman(goodman_id),
                FOREIGN KEY(badman_id) REFERENCES badman(badman_id),
                FOREIGN KEY(violation_type_id) REFERENCES violation_type(violation_type_id))            
            ''')
        print('recreated neigh_to_roommate_complaint')

        self.execute('DROP TABLE IF EXISTS landlord_to_tenant_complaint')
        self.execute('''
                    CREATE TABLE landlord_to_tenant_complaint(
                        landlord_to_tenant_complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        goodman_id INTEGER NOT NULL,
                        badman_id INTEGER NOT NULL,
                        complaint_date TEXT NOT NULL,
                        violation_date TEXT NOT NULL,
                        violation_type_id INTEGER NOT NULL,
                        violation_text TEXT NOT NULL,
                        lease_from_date TEXT,
                        lease_to_date TEXT,
                        status TEXT NOT NULL,
                        FOREIGN KEY(goodman_id) REFERENCES goodman(goodman_id),
                        FOREIGN KEY(badman_id) REFERENCES badman(badman_id),
                        FOREIGN KEY(violation_type_id) REFERENCES violation_type(violation_type_id))            
                    ''')
        print('recreated landlord_to_tenant_complaint')


if __name__ == "__main__":
    dbmanager = DBManager(dbpath='data/mycocedi.db')
    dbmanager.recreate_tables()