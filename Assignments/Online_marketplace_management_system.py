class OutOfStockError(Exception):
    def __init__(self, message="Requested quantity is not available or product is out of stock."):
        super().__init__(message)


class User:
    def __init__(self, name, email, user_id):
        self.set_name(name)
        self.set_email(email)
        self.set_user_id(user_id)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_email(self):
        return self.__email

    def set_email(self, email):
        if "@" not in email or not email.endswith(".com"):
            raise ValueError("Invalid email address")
        self.__email = email

    def get_user_id(self):
        return self.__user_id

    def set_user_id(self, user_id):
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("User ID must be a positive integer")
        self.__user_id = user_id


class Buyer(User):
    def __init__(self, name, email, user_id):
        super().__init__(name, email, user_id)
        self.__cart = []
        self.__purchase_history = {}
        self.__total_spent = 0.0

    def add_to_cart(self, product_name, quantity, seller):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        inventory = seller.get_inventory()
        if product_name not in inventory:
            raise OutOfStockError(f"{product_name} is not available in the seller's inventory.")
        price, stock = inventory[product_name]
        if quantity > stock:
            raise OutOfStockError(f"Only {stock} units of {product_name} available.")
        self.__cart.append((product_name, quantity))
        print(f"Added {quantity} x {product_name} to cart.")

    def checkout(self, seller):
        total = 0
        for product_name, quantity in self.__cart:
            if product_name not in seller.get_inventory():
                raise OutOfStockError(f"{product_name} not found in seller inventory")
            price, stock = seller.get_inventory()[product_name]
            if quantity > stock:
                raise OutOfStockError(f"Not enough stock for {product_name}")
            total += price * quantity
            seller.get_inventory()[product_name] = (price, stock - quantity)
            self._purchase_history[product_name] = self._purchase_history.get(product_name, 0) + quantity
        self.__cart = []
        self.__total_spent += total
        print(f"Checkout successful. Total spent: {total}")
        return total

    def view_cart(self):
        if not self.__cart:
            print("Cart is empty.")
        else:
            print("\n--- Cart Items ---")
            for product, qty in self.__cart:
                print(f"{product}: {qty}")

    def generate_invoice(self):
        print(f"\n--- Invoice for {self.get_name()} ---")
        print("Purchase History:")
        for product, qty in self.__purchase_history.items():
            print(f"{product}: {qty} pcs")
        print(f"Total Spent: {self.__total_spent}")
        if self.__total_spent > 10000:
            print("You are now a Premium Member!")

    def get_purchase_history(self):
        return self.__purchase_history


class Seller(User):
    def __init__(self, name, email, user_id, store_name):
        super().__init__(name, email, user_id)
        self.__store_name = store_name
        self.__inventory = {}

    def add_product(self, product_name, price, stock):
        if price < 0 or stock < 0:
            raise ValueError("Invalid product details")
        self.__inventory[product_name] = (price, stock)

    def update_stock(self, product_name, quantity_to_add):
        if quantity_to_add < 0:
            raise ValueError("Quantity to add must be positive")
        if product_name in self.__inventory:
            price, stock = self.__inventory[product_name]
            self.__inventory[product_name] = (price, stock + quantity_to_add)
        else:
            raise ValueError("Product not found in inventory")

    def get_inventory(self):
        return self.__inventory

    def get_store_name(self):
        return self.__store_name


# Menu logic
buyers = []
sellers = []


def buyer_menu(buyer):
    while True:
        print(f"\n--- Buyer Menu ({buyer.get_name()}) ---")
        print("1. Add product to cart")
        print("2. View cart")
        print("3. Checkout")
        print("4. View purchase history")
        print("5. Generate invoice")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                store_id = int(input("Enter seller ID: "))
                seller = next((s for s in sellers if s.get_user_id() == store_id), None)
                if not seller:
                    print("Seller not found.")
                    continue
                product = input("Enter product name: ")
                try:
                    quantity = int(input("Enter quantity: "))
                    buyer.add_to_cart(product, quantity, seller)
                except ValueError:
                    print("Invalid quantity.")
            elif choice == '2':
                buyer.view_cart()
            elif choice == '3':
                store_id = int(input("Enter seller ID: "))
                seller = next((s for s in sellers if s.get_user_id() == store_id), None)
                if seller:
                    buyer.checkout(seller)
                else:
                    print("Seller not found.")
            elif choice == '4':
                print(buyer.get_purchase_history())
            elif choice == '5':
                buyer.generate_invoice()
            elif choice == '6':
                break
            else:
                print("Invalid choice.")
        except OutOfStockError as oe:
            print("Out of Stock:", oe)
        except Exception as e:
            print("Error:", e)


def seller_menu(seller):
    while True:
        print(f"\n--- Seller Menu ({seller.get_store_name()}) ---")
        print("1. Add product")
        print("2. Update stock")
        print("3. View inventory")
        print("4. Exit")
        choice = input("Enter your choice: ")
        try:
            if choice == '1':
                product = input("Enter product name: ")
                try:
                    price = float(input("Enter price: "))
                    stock = int(input("Enter stock: "))
                    seller.add_product(product, price, stock)
                    print(f"Product '{product}' added.")
                except ValueError:
                    print("Invalid price or stock value.")
            elif choice == '2':
                product = input("Enter product name to update: ")
                try:
                    quantity = int(input("Enter quantity to add: "))
                    seller.update_stock(product, quantity)
                    print(f"Stock for '{product}' updated.")
                except ValueError:
                    print("Invalid quantity.")
            elif choice == '3':
                print(seller.get_inventory())
            elif choice == '4':
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)


def main():
    print("Welcome to the Online Marketplace System")
    while True:
        print("\nMain Menu:")
        print("1. Register Seller")
        print("2. Register Buyer")
        print("3. Seller Login")
        print("4. Buyer Login")
        print("5. Exit")
        main_choice = input("Enter your choice: ")
        try:
            if main_choice == '1':
                name = input("Seller Name: ")
                email = input("Seller Email: ")
                user_id = int(input("Seller ID: "))
                store_name = input("Seller Store name: ")
                seller = Seller(name, email, user_id, store_name)
                sellers.append(seller)
                print("Seller registered successfully.")
            elif main_choice == '2':
                name = input("Buyer Name: ")
                email = input("Buyer Email: ")
                user_id = int(input("Buyer ID: "))
                buyer = Buyer(name, email, user_id)
                buyers.append(buyer)
                print("Buyer registered successfully.")
            elif main_choice == '3':
                try:
                    user_id = int(input("Enter your user ID: "))
                    seller = next((s for s in sellers if s.get_user_id() == user_id), None)
                    if seller:
                        seller_menu(seller)
                    else:
                        print("Seller not found.")
                except ValueError:
                    print("Invalid ID.")
            elif main_choice == '4':
                try:
                    user_id = int(input("Enter your user ID: "))
                    buyer = next((b for b in buyers if b.get_user_id() == user_id), None)
                    if buyer:
                        buyer_menu(buyer)
                    else:
                        print("Buyer not found.")
                except ValueError:
                    print("Invalid ID.")
            elif main_choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":
    main()