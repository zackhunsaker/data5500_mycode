'''
This is an example of how to create a DeckOfCards object, shuffle it, and deal cards to play a game
'''

from DeckOfCards import *  # this brings in the card and deck of card classes. The * means bring in all data

def get_score(hand):
    total = 0
    num_aces = 0

    for card in hand: #this sums the values and counts aces
        total += card.val
        if card.face == "Ace": #if the face card is an ace we will add +1 to the total
            num_aces += 1
    while total > 21 and num_aces > 0: #this logic is saying that if the score is over 21 and the number of aces is greater than 0 we will lower the score by 10 for each ace until the score is under 21
        total -= 10
        num_aces -= 1
    return total

while True:
    deck = DeckOfCards() #this makes the new deck of 52 cards

    deck.print_deck() #this prints the deck in order
    deck.shuffle_deck() #this shuffles the deck
    deck.print_deck() #this will print the new shuffled deck


# deal two cards to the user
    card = deck.get_card() 
    card2 = deck.get_card()

    card1 = card


    user_hand = [card1,card2] # storing the users cards in a list

    score = get_score(user_hand) #this calls the list of card objects and gets the score for the user through the calculation. It gets card value and accounts for the aces rule

    print("Your score is:",score)

# ask user if they would like a "hit" (another card)
    hit = input("would you like a hit? (y or n) ") #asks if the user wants a hit and gives them the option of yes or no

    if hit == 'y':
        card3 = deck.get_card()
        user_hand.append(card3) #this will add it to the hand
        score = get_score(user_hand)
        print("new score: ", score)

        if score > 21:
            print("You broke 21, you lose")
            break
       

        hit = input("would you like a hit? (y or n) ")

    if score <= 21:  #if the user busts this will skip the dealer
    
        dealer_card1 = deck.get_card()
        dealer_card2 = deck.get_card()
        dealer_hand = [dealer_card1, dealer_card2] #dealing two cards to the dealer

        print("Dealers card number 1 is:",dealer_hand[0])
        print("Dealers card number 2 is:",dealer_hand[1])

        dealer_score = get_score(dealer_hand)
        dealer_count = 2 #we have two cards in the hand already

        while dealer_score < 17: #while the dealer is under 17 we hit and add a new card and then add it to the score. 
            next_card = deck.get_card()
            dealer_hand.append(next_card)
            dealer_count += 1
            print("Dealer hits, card number " + str(dealer_count) + " is:", next_card)
            dealer_score = get_score(dealer_hand) 

        print("Dealer score is:",dealer_score)
#below are the if statements for winning or losing
        if dealer_score > 21:
            print("Dealer broke 21, you win!")
        else:
            if score > dealer_score:
               print("Your score is higher, you win!")
            elif score == dealer_score:
                print("You and the dealer tied, you lose")
            else:
                print("Dealer score is higher, you lose :(")
    #here is the play again logic
    play_again = input("Would you like to play again? (y or n) ")
    if play_again.lower() != 'y':
        print("Thanks for playing!")
        break