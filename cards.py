from db.manage import Database

class CartItem:
    def __init__(self, user_id, product_id, quantity):
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

    def save_to_database(self):
        query = f"""
            INSERT INTO cart_items(user_id, product_id, quantity) 
            VALUES({self.user_id}, {self.product_id}, {self.quantity})
        """
        return Database.connect(query, "insert")


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, user_id, product_id, quantity=1):
        cart_item = CartItem(user_id, product_id, quantity)
        cart_item.save_to_database()  
        self.items.append(cart_item)  
        return "Item added to cart successfully."

if __name__ == "__main__":
    cart = ShoppingCart()
    print(cart.add_item(1, 2, 3))  
