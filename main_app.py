from auction_system import AuctionSystem

def main():
    auction_system = AuctionSystem()

    while True:
        print("\nONLINE AUCTION APP")
        print("1. Register Member")
        print("2. Display All Members")
        print("3. Add Auction Item")
        print("4. Place Bid")
        print("5. View Current Bidding Activities")
        print("6. View Auction Items")
        print("7. Buy Marketplace Item")
        print("8. Sell Marketplace Item")
        print("9. View Auction Winners")
        print("10. Leave Feedback")
        print("11. View Feedbacks")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            auction_system.register_member()
        elif choice == '2':
            auction_system.display_all_members()
        elif choice == '3':
            auction_system.add_item()
        elif choice == '4':
            auction_system.place_bid()
        elif choice == '5':
            auction_system.display_bidding_activities()
        elif choice == '6':
            auction_system.display_auction_items()
        elif choice == '7':
            auction_system.buy_item()
        elif choice == '8':
            auction_system.sell_item()
        elif choice == '9':
            auction_system.display_auction_winners()
        elif choice == '10':
            auction_system.add_feedback()
        elif choice == '11':
            auction_system.display_feedbacks()
        elif choice == '12':
            print("Thank you for using the Online Auction App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()