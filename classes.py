from db.manage import Database

class Country:
    table_name = "country"
    def __init__(self, name):
        self.name = name

    @staticmethod
    def select():
        query = f"SELECT * FROM {Country.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO country(name) VALUES('{self.name}')
        """
        return Database.connect(query, "insert")

    @staticmethod
    def update(column, new_data, old_data, table) -> str:
        if column == "id":
            query = f"UPDATE {table} SET {column} = {new_data} WHERE {column} = {old_data}"

        else:
            query = f"UPDATE {table} SET {column} = '{new_data}' WHERE {column} = '{old_data}'"

        return Database.connect(query, "update")

    @staticmethod
    def delete(column, data, table):
        if column == "id":
            query = f"DELETE FROM {table} WHERE {column} = {data}"

        else:
            query = f"DELETE FROM {table} WHERE {column} = '{data}'"
        return Database.connect(query, "delete")


class City(Country):
    table_name = "city"
    def __init__(self, name, county_id):
        Country.__init__(self, name)
        self.county_id = county_id

    @staticmethod
    def select():
        query = f"SELECT * FROM {City.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
            INSERT INTO city(name, county_id) VALUES('{self.name}', {self.county_id})
        """
        return Database.connect(query, "insert")


class Address(Country):
    pass

class Customers(Country):
    table_name = "customers"
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.username = username
        # self.birth_date = birth_date

    @staticmethod
    def select():
        query = f"SELECT * FROM {Customers.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
                INSERT INTO customers(first_name, last_name, username, password) 
                VALUES('{self.first_name}', '{self.last_name}', '{self.username}', '{self.password}')
            """
        return Database.connect(query, "insert")

    @staticmethod
    def personal_data(username, password):
        query = f"SELECT * FROM {Customers.table_name} WHERE username = '{username}' and password = '{password}'"
        return Database.connect(query, "select")

class PaymentStatus:
    pass

class Category(Country):
    table_name = "category"

    def __init__(self, name):
        Country.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Category.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
                    INSERT INTO category(name) 
                    VALUES('{self.name}')
                """
        return Database.connect(query, "insert")

class Store(Country):
    table_name = "store"

    def __init(self, name):
        Country.__init__(self, name)

    @staticmethod
    def select():
        query = f"SELECT * FROM {Store.table_name} ORDER BY id"
        data = Database.connect(query, "select")
        for i in data:
            print(i)

    def insert(self):
        query = f"""
               INSERT INTO store(name) VALUES('{self.name}')
           """
        return Database.connect(query, "insert")

class Product(Country):
    table_name = "product"

    def __init__(self, name, description, price, count, serial_number, start_date, end_date, store_id, category_id):
        Country.__init__(self, name)
        self.description = description
        self.price = price
        self.count = count
        self.serial_number = serial_number
        self.start_date = start_date
        self.end_date = end_date
        self.store_id = store_id
        self.category_id = category_id

    @staticmethod
    def select():
        query = f"""
        SELECT p.id, p.name, p.description, p.price, p.count, p.serial_number, p.start_date, p.end_date, s.name as "Store Name", c.name as "Category Name" FROM product p
                INNER JOIN category c ON p.category_id = c.id
                INNER JOIN store s ON p.store_id = s.id ORDER BY p.id"""

        return Database.connect(query, "select")

    def insert(self):
        query = f"""
                        INSERT INTO product(name, description, price, count, serial_number, start_date, end_date, store_id, category_id) 
                        VALUES('{self.name}', '{self.description}', {self.price}, {self.count}, {self.serial_number}, '{self.start_date}', '{self.end_date}', {self.store_id}, {self.category_id})
                    """
        return Database.connect(query, "insert")

    @staticmethod
    def search(name):
        query = f"SELECT * FROM product WHERE name LIKE '%{name}%'"
        return Database.connect(query, "select")

