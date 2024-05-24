class ItemToPurchase:
    item_name = ""
    item_price = 0.0
    item_quantity = 0
    
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
    
    def print_item_cost(self):
        print(self.item_name, self.item_quantity, "@", "$"+str(self.item_price), "=", self.item_price*self.item_quantity)
        
        
if __name__ == "__main__":
    print("Item 1")
    item1 = ItemToPurchase()
    item1.item_name = input("Enter the item name:\n")
    item1.item_price = float(input("Enter the item price:\n"))
    item1.item_quantity = int(input("Enter the item quantity:\n"))
    print("Item 2")
    item2 = ItemToPurchase()
    item2.item_name = input("Enter the item name:\n")
    item2.item_price = float(input("Enter the item price:\n"))
    item2.item_quantity = int(input("Enter the item quantity:\n"))
    print("TOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()
    total_cost = (item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)
    print("Total: $"+str(total_cost))
