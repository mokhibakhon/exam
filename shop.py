from classes import Category, Product

def category(username, password):
    Category.select()

    back = input("0. Back")
    if back == "0":
        return shop(username, password)


def products(username, password):
    data = Product.select()
    for i in data:
        print(f"""
            ID: {i[0]}
            Name: {i[1]}
            Description: {i[2]}
            Price: {i[3]}
            Count: {i[4]}
            Serial Number: {i[5]}
            Start Date: {i[6]}
            End Date: {i[7]}
            Store Name: {i[8]}
            Category Name: {i[9]}
        """)

    back = input("0. Back")
    if back == "0":
        return shop(username, password)

def shop(username, password):
    service = input(f"""
        s. search
        1. Category
        2. Products
            >>> """)

    if service == "1":
        return category(username, password)

    elif service == "2":
        return products(username, password)

    elif service == "s":
        search = input("Search: ")
        data = Product.search(search)
        for i in data:
            print(f"""
                ID: {i[0]}
                Name: {i[1]}
                Description: {i[2]}
                Price: {i[3]}
                Count: {i[4]}
                Serial Number: {i[5]}
                Start Date: {i[6]}
                End Date: {i[7]}
                Store Name: {i[8]}
                Category Name: {i[9]}
            """)
        return shop(username, password)