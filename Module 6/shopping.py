class ItemToPurchase:
    
    def __init__(self, name = "none", item_price = 0.0, item_quantity = 0, item_description = ""):
        self.item_name = name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description
    
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "${:.2f}".format(self.item_price), "=", "${:.2f}".format(self.item_price*self.item_quantity))
    
class ShoppingCart:
    
    def __init__(self, customer_name = "none", date = "January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = date
        self.cart_items = list()
        
    def add_item(self, itemToPurchase):
        self.cart_items.append(itemToPurchase)
        
    def remove_item(self, item_name):
        item_removed = False
        for each in self.cart_items:
            if each.item_name == item_name:
                self.cart_items.remove(each)
                item_removed = True
        if item_removed is False:
            print("Item not found in cart. Nothing removed.")
            
    def modify_item(self, itemToPurchase):
        item_found = False
        for each in self.cart_items:
            if each.item_name == itemToPurchase.item_name:
                item_found = True
                
                if itemToPurchase.item_description != "" and itemToPurchase.item_price != 0.0 and itemToPurchase.item_quantity != 0:
                    while True:
                        print("Modify {}".format(itemToPurchase.item_name))
                        print("1 - Description")
                        print("2 - Price")
                        print("3 - Quantity")
                        print("4 - Exit")
                        choice = int(input("Enter Option: "))
                        if choice == 1:
                            itemToPurchase.item_description = input("Enter Description: ")
                        elif choice == 2:
                            itemToPurchase.item_price = float(input("Enter item price: "))
                        elif choice == 3:
                            itemToPurchase.item_quantity = int(input("Enter quantity: "))
                        elif choice == 4:
                            break
        if item_found is False:
            print("Item not found in cart. Nothing Modified")
            
    def get_num_items_in_cart(self):
        return sum(item.item_quantity for item in self.cart_items)
    
    def get_cost_of_cart(self):
        return sum(item.item_price * item.item_quantity for item in self.cart_items)
    
    def print_total(self):
        print(self.customer_name+"'s", "Shopping Cart-", self.current_date)
        print("Number of Items:", self.get_num_items_in_cart())
        
        for each in self.cart_items:
            each.print_item_cost()
            
        print("Total:", "${:.2f}".format(self.get_cost_of_cart()))
        
    def print_descriptions(self):
        print(self.customer_name+"'s", "Shopping Cart-", self.current_date)
        print("Item Descriptions")
        for each in self.cart_items:
            print(each.item_name + ":", each.item_description) 

def printMenu(shoppingCart: ShoppingCart):
    while True:
        print("MENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        choice = input("Choose an option: ")
        if choice == "q":
            break
        elif choice == "a":
            itemName = input("Enter Item Name: ")
            itemPrice = float(input("Enter Item Price: "))
            itemQuantity = int(input("Enter Item Quantity: "))
            itemDescription = input("Enter Item Description: ")
            item = ItemToPurchase(itemName, itemPrice, itemQuantity, itemDescription)
            shoppingCart.add_item(item)
        elif choice == "r":
            itemName = input("Enter item name to be removed cart: ")
            shoppingCart.remove_item(itemName)
        elif choice == "c":
            itemName = input("Enter item name to be modified: ")
            item_to_modify = ItemToPurchase()
            for item in shoppingCart.cart_items:
                if item.item_name == itemName:
                    item_to_modify = item
                    break
            shoppingCart.modify_item(item_to_modify)
        elif choice == "i":
            shoppingCart.print_descriptions()
        elif choice == "o":
            print("OUTPUT SHOPPING CART")
            shoppingCart.print_total()
            
if __name__ == "__main__":
    customerName = input("Enter Customer Name: ")
    currentDate = input("Enter Current Date: ")
    
    cart = ShoppingCart(customerName, currentDate)
    printMenu(cart)
            
            
        
