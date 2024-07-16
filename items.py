from datetime import datetime

class Item:
    def __init__(self, item_number, title, description, start_bid, bid_increment, seller):
        self.item_number = item_number
        self.title = title
        self.description = description
        self.start_bid = start_bid
        self.bid_increment = bid_increment
        self.seller = seller
        self.bids = []
        self.bid_start_time = None
        self.bid_end_time = None

    def place_bid(self, buyer, bid_amount):
        if len(self.bids) == 0:
            self.bid_start_time = datetime.now()

        if len(self.bids) < 5:
            min_bid = self.start_bid if not self.bids else self.bids[-1][1] + self.bid_increment
            if bid_amount >= min_bid:
                self.bids.append((buyer, bid_amount, datetime.now()))
                if len(self.bids) == 5:
                    self.bid_end_time = datetime.now()
                return True
        return False

    def is_bidding_open(self):
        return len(self.bids) < 5

    def get_winner(self):
        if self.bids:
            return max(self.bids, key=lambda x: x[1])[0]  # Return buyer with highest bid
        return None

    def format_datetime(self, dt):
        if dt:
            return f"Date: {dt.strftime('%B-%d-%Y')}\nTime: {dt.strftime('%I:%M:%S %p')}"
        return "N/A"

    def get_bid_times(self):
        start_time = self.format_datetime(self.bid_start_time)
        end_time = self.format_datetime(self.bid_end_time)
        return start_time, end_time
