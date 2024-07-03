from classes import Country, City, Customers
from db.manage import Check
import account
import shop

def website(username, password):
    web = input("""
        Website
            1. Shop
            2. Cards
            3. Account
                >>> """)

    if web == "1":
        return shop.shop(username, password)

    elif web == "2":
        pass

    elif web == "3":
        return account.account(username, password)

    else:
        print("Error")
        return website(username, password)


def login():
    username = input("Username: ")
    password = input("Password: ")
    if Check.login_check(username, password):
        return website(username, password)

    else:
        print("Username yoki Password noto'g'ri")
        return login()

def register():
    print("Register Page")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    username = input("Username: ")
    password_1 = input("Password: ")
    password_2 = input("Reply Password: ")
    while password_1 != password_2:
        print("Passwordlar mos kelmadi!")
        password_1 = input("Password: ")
        password_2 = input("Reply Password: ")

    new_customer = Customers(first_name, last_name, username, password_1)
    print(new_customer.insert())

    return login()

def intro():
    user = input("""
        1. Login
        2. Register
            >>> """)

    if user == "1":
        return login()

    elif user == "2":
        return register()

    else:
        print("Error")
        return intro()

if __name__ == "__main__":
    intro()