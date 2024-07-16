from datetime import datetime
from marketplace import Marketplace
from items import Item
from members import Buyer, Seller

class AuctionSystem:
    def __init__(self):
        self.members = {}  # Key: member_id (string), Value: Member object
        self.items = {}
        self.feedbacks = []
        self.marketplace = Marketplace()
        self.next_member_id = 1  # To generate unique member IDs
        self.next_item_id = 1  # To generate unique item IDs

    def register_member(self):
        member_type = input("Enter member type (buyer/seller): ").lower()
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        home_address = input("Enter home address: ")
        phone = input("Enter phone number: ")

        member_id = f"M{self.next_member_id:03d}"  # Generate member ID like M001, M002, etc.
        self.next_member_id += 1

        if member_type == 'buyer':
            shipping_address = input("Enter shipping address: ")
            member = Buyer(member_id, name, email, password, home_address, phone, shipping_address)
        elif member_type == 'seller':
            bank_account = input("Enter bank account number: ")
            routing_number = input("Enter routing number: ")
            member = Seller(member_id, name, email, password, home_address, phone, bank_account, routing_number)
        else:
            print("Invalid member type.")
            return

        self.members[member_id] = member
        print(f"{member_type.capitalize()} registered successfully. Member ID: {member_id}")

    def display_all_members(self):
        print("Members:")
        for member_id, member in self.members.items():
            member_type = 'Buyer' if isinstance(member, Buyer) else 'Seller'
            print(f"[{member_id}] {member.name} - {member_type}")

    def display_auction_items(self):
        print("Auction Items:")
        for item_id, item in self.items.items():
            print(f"Item ID: {item_id}, Title: {item.title}, Starting Bid: {item.start_bid}")

    def add_item(self):
        seller_id = input("Enter seller ID: ")
        if seller_id not in self.members or not isinstance(self.members[seller_id], Seller):
            print("Invalid seller ID.")
            return

        title = input("Enter item title: ")
        description = input("Enter item description: ")
        start_bid = float(input("Enter starting bid price: "))
        bid_increment = float(input("Enter bid increment: "))

        item_id = f"I{self.next_item_id:03d}"  # Generate item ID like I001, I002, etc.
        self.next_item_id += 1

        item = Item(item_id, title, description, start_bid, bid_increment, self.members[seller_id])
        self.items[item_id] = item
        print(f"Item added successfully with item ID: {item_id}")

    def place_bid(self):
        buyer_id = input("Enter your buyer ID: ")
        if buyer_id not in self.members or not isinstance(self.members[buyer_id], Buyer):
            print("Invalid buyer ID.")
            return

        item_id = input("Enter the item ID you want to bid on: ")
        if item_id not in self.items:
            print("Invalid item ID.")
            return

        item = self.items[item_id]
        if not item.is_bidding_open():
            print("Bidding for this item has closed.")
            return

        bid_amount = float(input("Enter your bid amount: "))
        if item.place_bid(self.members[buyer_id], bid_amount):
            print("Bid placed successfully.")
            if not item.is_bidding_open():
                print("This was the final bid. Bidding for this item has now closed.")
            self.display_bidding_activities()
        else:
            print("Bid not accepted. Please ensure your bid is higher than the current highest bid.")

    def get_auction_winners(self):
        winners = []
        for item_id, item in self.items.items():
            if not item.is_bidding_open():
                winner = item.get_winner()
                if winner:
                    start_time, end_time = item.get_bid_times()
                    winners.append({
                        'item_id': item_id,
                        'item_title': item.title,
                        'winner': winner.name,
                        'winning_bid': item.bids[-1][1],
                        'bid_start': start_time,
                        'bid_end': end_time
                    })
        return winners

    def display_auction_winners(self):
        winners = self.get_auction_winners()
        if not winners:
            print("No auctions have completed yet.")
        else:
            for winner in winners:
                print(f"\nItem ID: {winner['item_id']}")
                print(f"Item Title: {winner['item_title']}")
                print(f"Winner: {winner['winner']}")
                print(f"Winning Bid: ${winner['winning_bid']:.2f}")
                print(f"Bidding Started:\n{winner['bid_start']}")
                print(f"Bidding Ended:\n{winner['bid_end']}")
                print("-" * 40)

    def display_bidding_activities(self):
        print("\nCurrent Bidding Activities:")
        print(f"{'Bidded':<15}{'Bidders':<30}{'Bidder ID':<15}")
        print("-" * 60)

        active_items = [item for item in self.items.values() if item.is_bidding_open()]
        
        if not active_items:
            print("No active bidding at the moment.")
            return

        for item in active_items:
            print(f"[{len(item.bids)}] {item.title:<10}", end="")
            
            if not item.bids:
                print("No bids yet")
                continue
            
            for i, (bidder, amount, _) in enumerate(item.bids):
                if i > 0:
                    print(" " * 15, end="")
                print(f"{bidder.name:<30}{bidder.member_id:<15}")
            
            print()  # Empty line for readability between items

    def buy_item(self):
        self.marketplace.list_items()
        item_id = input("Enter the item ID to buy: ")
        quantity = int(input("Enter the quantity to buy: "))
        return self.marketplace.buy_item(item_id, quantity)

    def sell_item(self):
        seller_id = input("Enter your seller ID: ")
        if seller_id not in self.members or not isinstance(self.members[seller_id], Seller):
            print("Invalid seller ID.")
            return

        item_name = input("Enter item name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        
        item_id = f"M{self.next_item_id:03d}"  # Generate marketplace item ID like M001, M002, etc.
        self.next_item_id += 1

        self.marketplace.add_item(item_id, item_name, price, quantity, self.members[seller_id])
        print(f"Item {item_name} added successfully to the marketplace with item ID: {item_id}")

    def add_feedback(self):
        giver_id = input("Enter your member ID: ")
        receiver_id = input("Enter the receiver's member ID: ")
        
        if giver_id not in self.members or receiver_id not in self.members:
            print("Invalid member ID.")
            return

        rating = int(input("Enter rating (1-10): "))
        if rating < 1 or rating > 10:
            print("Invalid rating. Please enter a number between 1 and 10.")
            return

        comment = input("Enter comment: ")

        giver = self.members[giver_id]
        receiver = self.members[receiver_id]
        feedback = Feedback(rating, comment, giver, receiver)
        self.feedbacks.append(feedback)
        print("Feedback added successfully.")

    def display_feedbacks(self):
        if not self.feedbacks:
            print("No feedbacks available.")
        else:
            for feedback in self.feedbacks:
                print(f"From: {feedback.giver.name}, To: {feedback.receiver.name}")
                print(f"Rating: {feedback.rating}, Comment: {feedback.comment}")
                print("-" * 30)

class Feedback:
    def __init__(self, rating, comment, giver, receiver):
        self.rating = rating
        self.comment = comment
        self.giver = giver
        self.receiver = receiver