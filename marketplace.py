class Marketplace:
    def __init__(self):
        self.items = []

    def add_item(self, item_id, item_name, price, quantity, seller):
        self.items.append({
            'item_id': item_id,
            'item_name': item_name,
            'price': price,
            'quantity': quantity,
            'seller': seller
        })

    def list_items(self):
        if not self.items:
            print("No items available for sale.")
        else:
            for item in self.items:
                print(f"Item ID: {item['item_id']}, Name: {item['item_name']}, Price: {item['price']} PHP, Quantity: {item['quantity']}")

    def buy_item(self, item_id, quantity):
        for item in self.items:
            if item['item_id'] == item_id:
                if item['quantity'] >= quantity:
                    item['quantity'] -= quantity
                    print(f"Bought {quantity} of {item['item_name']}")
                    if item['quantity'] == 0:
                        self.items.remove(item)
                    return True
                else:
                    print("Not enough quantity available.")
                    return False
        print("Item not found.")
        return False