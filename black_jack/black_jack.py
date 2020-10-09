import time
import random
try:
    import tkinter
except:
    import Tkinter as tkinter #python 2

def load_card(card_images):
    suits = ["heart", "club", "diamond", "spade"]
    face_cards = ["jack", "queen", "king"]

    if tkinter.TkVersion >= 8.6:
        extension = "png"
    else:
        extension = "ppm"

    #for each suits retreive the image for the cards
    for suit in suits:
        for card in range(1, 11):
            name = 'tkinter/black_jack/cards/{}_{}.{}'.format(str(card), suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((card, image))
        
        #dealing with face cards    
        for face in face_cards:
            name = 'tkinter/black_jack/cards/{}_{}.{}'.format(face, suit, extension)
            image = tkinter.PhotoImage(file=name)
            card_images.append((10, image))


def deal_card(frame):
    next_card = deck.pop(0)
    tkinter.Label(frame, image=next_card[1], relief="raised").pack(side='left')
    return next_card


def score_hand(hand):
    #Calculate hand score
    score = 0
    ace = False
    for card in hand:
        card_value = card[0]
        if card_value == 1 and not ace:
            if score < 11:
                card_value = 11
                ace = True
        score += card_value
    return score

def deal_dealer():
    dealer_score = score_hand(dealer_hand)
    while 0 < dealer_score < 17:
        dealer_hand.append(deal_card(dealer_card_frame))
        dealer_score = score_hand(dealer_hand)
        dealer_score_label.set(dealer_score)

    player_score = score_hand(player_hand)

    if player_score > 21:
        result_text.set("Dealer wins!")
    elif dealer_score > 21 or player_score > dealer_score:
        result_text.set("Player Wins!")
    elif dealer_score > player_score:
        result_text.set("Dealer wins!")
    elif dealer_score == player_score:
        result_text.set("Tie Game!")
        
    if player_score == 21 or dealer_score ==21:
        time.sleep(2)
        resulet_text.set("Black Jack!")
    
    
def deal_player():
    player_hand.append(deal_card(player_card_frame))
    player_score = score_hand(player_hand)
    player_score_label.set(player_score)
    if player_score > 21:
        result_text.set("Dealer Wins!")
    if player_score == 21:
        result_text.set("Black Jack!")
    # global player_score
    # global player_ace
    # card_value = deal_card(player_card_frame)[0]
    # if card_value == 1:
    #     if player_score < 11:
    #         card_value = 11
    #         player_ace = True
    # player_score += card_value
    # if player_score > 21 and player_ace:
    #     player_score -= 10
    #     player_ace = False
    # player_score_label.set(player_score)
    # if player_score > 21:
    #     result_text.set("Dealer wins!")


def new_game():
    global player_hand
    player_hand.clear()
    global dealer_hand
    dealer_hand.clear()
    global player_card_frame
    global dealer_card_frame
    player_card_frame.destroy()
    dealer_card_frame.destroy()

    dealer_card_frame = tkinter.Frame(card_frame, background="green")
    dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="ew")

    player_card_frame = tkinter.Frame(card_frame, background="green")
    player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)
    result_text.set("who will win is still a mystery..")
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()
   

def play():
    #main    
    deal_player()
    dealer_hand.append(deal_card(dealer_card_frame))
    dealer_score_label.set(score_hand(dealer_hand))
    deal_player()

    mainwindow.mainloop()


mainwindow = tkinter.Tk()

#set up screen and frames for dealer and player
mainwindow.title("Black Jack")
mainwindow.geometry("640x480")
mainwindow.configure(background="purple")

result_text = tkinter.StringVar()
result = tkinter.Label(mainwindow, textvariable=result_text)
result.grid(row=0, column=0, columnspan=3)

#card frame
card_frame = tkinter.Frame(mainwindow, relief = "sunken", borderwidth = 2, background = "green")
card_frame.grid(row=1, column=0, sticky="ew", rowspan=2, columnspan=3)

dealer_score_label = tkinter.IntVar()
tkinter.Label(card_frame, text="Dealer", background="green", fg="white").grid(row=0, column=0)
tkinter.Label(card_frame, textvariable=dealer_score_label, background="green", fg="white").grid(row=1, column=0)
#embedded frame to hold card images
dealer_card_frame = tkinter.Frame(card_frame, background="green")
dealer_card_frame.grid(row=0, column=1, rowspan=2, sticky="ew")

player_score_label = tkinter.IntVar()

tkinter.Label(card_frame, text="Player", background="green", fg="white").grid(row=2, column=0)
tkinter.Label(card_frame, textvariable=player_score_label, background="green", fg="white").grid(row=3, column=0)
#embedded frame to hold card images
player_card_frame = tkinter.Frame(card_frame, background="green")
player_card_frame.grid(row=2, column=1, sticky="ew", rowspan=2)

#button frame
button_frame = tkinter.Frame(mainwindow)
button_frame.grid(row=3, column=0, columnspan=3, sticky="w")
dealer_button = tkinter.Button(button_frame, text="Dealer", command=deal_dealer)
dealer_button.grid(row=0, column=0)

player_button = tkinter.Button(button_frame, text="Player", command=deal_player)
player_button.grid(row=0, column=1)

new_game_button = tkinter.Button(button_frame, text='New Game', command=new_game)
new_game_button.grid(row=1, column=0)

cards = []
load_card(cards)
#create a new deck of cards and shuffle
deck = list(cards)
random.shuffle(deck)

#create list to create hands
dealer_hand = []
player_hand = []


# if __name__ == "__main__":
#     play()
