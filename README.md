# Online Auction and Marketplace System

This project implements an online auction and marketplace system using Python. It allows users to register as buyers or sellers, add items for auction, place bids, buy and sell items in a marketplace, and leave feedback.

## Files

1. `items.py`: Defines the `Item` class for auction items.
2. `marketplace.py`: Implements the `Marketplace` class for buying and selling items.
3. `members.py`: Contains the abstract `Member` class and concrete `Buyer` and `Seller` classes.
4. `online_auction_app.py`: The main application file with the user interface.
5. `auction_system.py`: Implements the core `AuctionSystem` class that manages the entire system.

## Features

- User registration (buyers and sellers)
- Adding items for auction
- Bidding on auction items
- Viewing current bidding activities
- Buying and selling items in a marketplace
- Leaving and viewing feedback
- Displaying auction winners


## System Structure

- The `AuctionSystem` class in `auction_system.py` is the central component that manages members, items, and the marketplace.
- `Item` class in `items.py` represents auction items and handles bidding logic.
- `Marketplace` class in `marketplace.py` manages buying and selling of non-auction items.
- `Member`, `Buyer`, and `Seller` classes in `members.py` represent users of the system.
- The main loop in `online_auction_app.py` provides a text-based user interface for interacting with the system.
