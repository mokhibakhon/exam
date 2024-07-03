from manage import Database

def create_table():
    country = f"""
        CREATE TABLE country(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            create_date TIMESTAMP DEFAULT now());"""

    city = f"""
            CREATE TABLE city(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                county_id INT REFERENCES country(id),
                create_date TIMESTAMP DEFAULT now());"""

    address = f"""
            CREATE TABLE address(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                city_id INT REFERENCES city(id),
                create_date TIMESTAMP DEFAULT now());"""

    customers = f"""
               CREATE TABLE customers(
                   id SERIAL PRIMARY KEY,
                   first_name VARCHAR(50),
                   last_name VARCHAR(50),
                   birth_date DATE,
                   address_id INT REFERENCES address(id),
                   create_date TIMESTAMP DEFAULT now());"""

    payment_status = f"""
                CREATE TABLE payment_status(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    create_date TIMESTAMP DEFAULT now());"""

    category = f"""
            CREATE TABLE category(
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                create_date TIMESTAMP DEFAULT now());"""

    store = f"""
                CREATE TABLE store(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(50),
                    create_date TIMESTAMP DEFAULT now());"""

    product = f"""
                CREATE TABLE product(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100),
                    description TEXT,
                    price NUMERIC,
                    count INTEGER,
                    serial_number INTEGER,
                    start_date DATE,
                    end_date DATE,
                    store_id INT REFERENCES store(id),
                    category_id INT REFERENCES category(id),
                    create_date TIMESTAMP DEFAULT now());"""

    data = {
            "country": country,
            "city": city,
            "address": address,
            "customers": customers,
            "payment_status": payment_status,
            "category": category,
            "store": store,
            "product": product}
    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")

if __name__ == "__main__":
    create_table()