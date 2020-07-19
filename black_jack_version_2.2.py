#When game launches, player will see green canvas, New Game Hit, Stand and End Game buttons
#When New Game button is clicked, player will be asked how many chips they would like to bet
#When number of chips are entered, and Submit Chips button is clicked, the cards should then display on the screen
#Player should then be asked if they'd like to hit or stand, and How many chips question should be removedf from screen
#When Hit button is clicked, another card is dealt to dealer and player and their values are calculated
#The calculated values are then displayed on the screen.
#When Stand button is clicked, a message is displayed that the Dealer is now playing
#At End of game, chip totals need to be updated
#All dealer cards need to be displayed on screen for all needed indexes


from tkinter import *
from winsound import *
import random
import os
from PIL import ImageTk,Image
from collections import OrderedDict
from functools import partial
import os  #it will be used to restart the game
from tkinter import messagebox

#INPUT FIELD FOR CHIPS
global chipsInput 
global chipsButton,chipsLabel
global bet_chips

global hitButton,standButton
global total_chips
global player_chips
global player_hand
global hitLabel
global playing
global new_game_message
global dealerHitLabel,dhl_flag
global dxpos,dypos #dealer x and y positions
global pxpos,pypos #player x and y positions

#These two variable are created to controll the display of cards
global dCard,pCard
pCard=0
dCard=0
dxpos=50
dypos=110
pxpos=50 
pypos=410

global window
#TRY PLAYER.CARDS[0] AND [1]
window = Tk()
window.title("Jaron's Python Blackjack")
window.configure(background="dark green")

#MAKE SCREEN FIT ANY MONITOR SIZE/NOT RESIZABLE BY USER
width_value=window.winfo_screenwidth()
height_value=window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (width_value, height_value))
window.resizable(width=False, height=False)

'''Frames go into Windows'''
#RIGHT FRAME
rightFrame = Frame(window, width=200, height=1000,bg="black")
rightFrame.place(x=1095,y=340,anchor=W)

'''CREATING GAME IMAGE LOGO'''
#SETTING IMAGE DIMENSIONS
width = 100
height = 150


#OPENING,RESIZING AND LOADING JACK ICON IMAGE
load = Image.open(r'C:\Users\I860605\OneDrive - SAP SE\Desktop\THONNY\Black_Jack_Game\blackjackicon3.png')
load = load.resize((width,height), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

#DISPLAYING AND PLACING JACK ICON IMAGE ON SCREEN
img = Label(window,image=render)
img.image=render
img.place(x=1111,y=200,anchor=W)


'''CREATE DEALER DECK IMAGE '''
#OPENING,RESIZING AND LOADING IMAGE
load = Image.open(r'C:\Users\I860605\OneDrive - SAP SE\Desktop\THONNY\Black_Jack_Game\Card-Back-01.png')
load = load.resize((width,height), Image.ANTIALIAS)   
render = ImageTk.PhotoImage(load)

#DISPLAYING AND PLACING IMAGE ON SCREEN
img = Label(window,image=render)
img.image=render
img.place(x=925,y=60)

'''Deck Label '''
deckLabel = Label(window,text="DECK",font=20)
deckLabel.place(x=946,y=25)


#OPENING,RESIZING AND LOADING ACE IMAGE#2
load = Image.open(r'C:\Users\I860605\OneDrive - SAP SE\Desktop\THONNY\Black_Jack_Game\black_ace_icon.png')
load = load.resize((width,height), Image.ANTIALIAS)
render = ImageTk.PhotoImage(load)

#DISPLAYING AND PLACING ACE IMAGE#2 ON SCREEN
img = Label(window,image=render)
img.image=render
img.place(x=1161,y=230,anchor=W)

#TITLE OF GAME
gameTitle = Label(window, font=('notmarykate',28),text="Blackjack", bg="black", fg="white")
gameTitle.place(x=1101,y=40,anchor=W)

#VERSION TITLE
versionTitle = Label(window, font=('notmarykate',10),text="Version 2.0", bg="black", fg="white")
versionTitle.place(x=1121,y=80,anchor=W)


#AUTHOR'S TITLE
authorTitle = Label(window, font=('notmarykate',8),text="by Jaron Manyama", bg="black", fg="white")
authorTitle.place(x=1121,y=100,anchor=W)

#DEALER LABEL
dealerLabel = Label(window, text= "DEALER:", font=20,borderwidth=5,relief="groove")
dealerLabel.place(x=50,y=50)



'''Used to identify the attributes of each card, and print out a string representation of each card'''

suits = ('Spades','Diamonds','Hearts','Club') #('Hearts','Diamonds','Spades','Clubs')   


rankes = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

cardImages = ['c02.png','c03.png','c04.png','c05.png','c06.png','c07.png','c08.png','c09.png','c10.png','c11.png','c12.png','c13.png','c01.png','d02.png','d03.png','d04.png','d05.png','d06.png','d07.png','d08.png','d09.png','d10.png','d11.png','d12.png','d13.png','d01.png','h02.png','h03.png','h04.png','h05.png','h06.png','h07.png','h08.png','h09.png','h10.png','h11.png','h12.png','h13.png','h01.png','s02.png','s03.png','s04.png','s05.png','s06.png','s07.png','s08.png','s09.png','s10.png','s11.png','s12.png','s13.png','s01.png']


cardImages2 = [('c02.png',2),('c03.png',3),('c04.png',4),('c05.png',5),('c06.png',6),('c07.png',7),('c08.png',8),('c09.png',9),('c10.png',10,),('c11.png',10,),('c12.png',10),('c13.png',10,),('c01.png',11,),('d02.png',2),('d03.png',3),('d04.png',4),('d05.png',5),('d06.png',6),('d07.png',7),('d08.png',8),('d09.png',9),('d10.png',10,),('d11.png',10,),('d12.png',10),('d13.png',10,),('d01.png',11,),('h02.png',2),('h03.png',3),('h04.png',4),('h05.png',5),('h06.png',6),('h07.png',7),('h08.png',8),('h09.png',9),('h10.png',10,),('h11.png',10,),('h12.png',10),('h13.png',10,),('h01.png',11,),('s02.png',2),('s03.png',3),('s04.png',4),('s05.png',5),('s06.png',6),('s07.png',7),('s08.png',8),('s09.png',9),('s10.png',10,),('s11.png',10,),('s12.png',10),('s13.png',10,),('s01.png',11,)]

cardImagesOrdered = OrderedDict(cardImages2)

#COMMAND LINE CLASSES AND FUNCTIONS

''' Breaking up components needed for Black Jack Game using Global Variables'''

playing = True

class Card:
    
    def __init__(self,suit,rank,card_image):
        self.suit = suit
        self.rank = rank
        self.card_image = card_image
        
        
    def __str__(self):
        return self.rank + ' ' + "of " + self.suit
    


'''Store 52 cards into the Deck that can later be shuffled (refilling the deck)'''
class Deck:  
    
    def __init__(self):
        self.deck = [] # start with an empty list
        img_index=0
        for suit in suits:
            for rank in rankes:
                card_image=cardImages[img_index]
                self.deck.append(Card(suit,rank,card_image)) # add every suit of every rank into the Deck.
                img_index+=1
                
                                        
    '''Used to display what's currently in the deck'''         
            
    def __str__(self): 
        deck_comp = '' # starting with an empty deck
        for card in self.deck:
            deck_comp += '\n' + card.__str__() # add string representation (from Card class) of each individual card to the deck.
        return "The deck has: " + deck_comp
    

    '''Used to shuffle the deck'''
    
    def shuffle(self):
        random.shuffle(self.deck) # apply random function on shuffle function with self.deck parameter
        
    '''Used to deal a card from the deck'''
    
    def deal(self):
        single_card = self.deck.pop() # grab a deck attribute from self.deck. Pop off a card item from that list. Set that card value equal to single-card
        return single_card
    
    
    ''' Used to calculate the values of the cards that are actually in the player's hand. '''  
class Hand:
    def __init__(self):
        self.cards = [] # start with an emply list
        self.image = 0
        self.value = 0 # start with a zero value
        self.aces = 0 # add an attribute to keep track of the aces
        
        
    def add_card(self,card):
        # card passed in from Deck.deal() single Card(suit,rank,image)
        self.cards.append(card)
        self.value += values[card.rank]

        self.image += cardImagesOrdered[card.card_image]
                
        #track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        #IF TOTAL VALUE > 21 AND I STILL HAVE AN ACE
        #THEN CHANGE MY ACE TO BE A 1 INSTEAD OF AN 11
        while self.value > 21 and self.aces:
            self.value -= 10  # Subtract 10 from the value of the Ace (currently 11)
            self.aces -= 1    # Take away one of my aces



'''Used to keep track of the starting and remaining chips that are bet'''
class Chips:
    def __init__(self):
        self.total = 100 #Default starting value in chips
        self.bet = 0 #Default starting bet value is 0
        
    def win_bet(self,total,bet):
        total += bet
        return total
    
    def lose_bet(self,total,bet):
        total -= bet
        return total


#INDEPENDENT FUNCTIONS NOT TIED TO ANY CLASS

def take_bet_question():
    #CHIPS QUESTION LABEL
    global chipsQuestion
    chipsQuestion = Label(window, text="How many chips would you like to bet?",bg="dark green",fg='white', font=20)
    chipsQuestion.place(x=640,y=450)
    

def hit(deck,hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()
            

def hit_or_stand(deck,hand):
    global hitLabel
    global playing #to control upcoming while loop
    
    hitLabel = Label(window, text= "Hit or Stand? >>>",bg="dark green",fg='white', font=20)
    hitLabel.place(x=920,y=420)
    
       
def show_some(player,dealer):
        global pxpos,pypos,dxpos,dypos
        global dCard,pCard

        print("\n DEALER'S HAND: ")
        print("One card hidden!")
        print("",dealer.cards[1])   
        
        '''Dealer Label Hidden Card Label'''
        dealerCardHidden = dealer.cards[0]
        
        '''Dealer Label Revealed Card 2'''
        dealerCard_2 = dealer.cards[1]
        
        '''Hidden Dealer Card Image'''
            
        #OPENING,RESIZING AND LOADING IMAGE
        load = Image.open('Card-Back-01.png')
        load = load.resize((width,height), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        #DISPLAYING AND PLACING IMAGE ON SCREEN
        img = Label(window,image=render)
        img.image=render
        img.place(x=dxpos,y=dypos)
        dxpos+=width+30
        dCard+=1
        i=0
        '''Revealed Dealer Card Image at Index 1'''
        for card in dealer.cards:
            if(i==dCard):
                dCard=dCard+1

                             
                #OPENING,RESIZING AND LOADING IMAGE
                if (i==1):
                    load = Image.open(card.card_image)
                else:
                    load = Image.open('Card-Back-01.png')
                
                load = load.resize((width,height), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)

                #DISPLAYING AND PLACING IMAGE ON SCREEN
                img = Label(window,image=render)
                img.image=render
                img.place(x=dxpos,y=110)
                dxpos+=width+30
                '''Player's starting cards at indexes 0 and 1'''
            
            i+=1
        
        #print("PLAYER'S HAND: ", sep= '\n')
        playerCardsLabel = player.cards
        i=0
        
        '''Player Label Revealed Card'''
        for card in player.cards:
            if(pCard==i):
                pCard+=1

                image=card.card_image

                print(card)
        
                #OPENING,RESIZING AND LOADING IMAGE for Player Card indexes 0 and 1
                load = Image.open(image)
                load = load.resize((width,height), Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
               
                
                #DISPLAYING AND PLACING IMAGE ON SCREEN
                img = Label(window,image=render)
                img.image=render
                img.place(x=pxpos,y=pypos)
                pxpos+=width+30
            
            i+=1
        


def show_another(player):
    global pCard,pxpos,pypos
    i=0
    
    for card in player.cards:
        playerCardsLabel_2 = card
        if(i==pCard):
            pCard+=1
            print(card)
        
                
            '''Player card position #3 '''
            #OPENING,RESIZING AND LOADING IMAGE
            load1 = Image.open(card.card_image)
            load1 = load1.resize((width,height), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load1)

            #DISPLAYING AND PLACING IMAGE ON SCREEN
            img1 = Label(window,image=render)
            img1.image=render
            img1.place(x=pxpos,y=pypos)
            pxpos+=width+30
        i+=1
               
def show_all(dealer):
    #if u want to show one hidden card of dealer then uncommit this below code
    
    global dCard
    global dxpos,dypos
    
    dCard=0
    dxpos=50
    dypos=110


    print('-----------------------------------')
    print('Showing All Cards in Dealer Hand=',len(dealer.cards))
    print("DEALER'S HAND: ")
    i=0
    for card in dealer.cards:
        if(i==dCard):
            dCard+=1        
            #OPENING,RESIZING AND LOADING IMAGE
            load = Image.open(card.card_image)
            load = load.resize((width,height), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)

            #DISPLAYING AND PLACING IMAGE ON SCREEN
            img = Label(window,image=render)
            img.image=render
            img.place(x=dxpos,y=dypos)
            dxpos+=width+30
        i+=1
         
                    
def dshow_another(dealer):
    global dCard,dxpos,dypos
    print('In Show Another Function and dealer card already shown is=',dCard)
    
    i=0
    
    for card in dealer.cards:
        dealerCardsLabel_2 = card
        if(i==dCard):
            dCard+=1
            print(card)
        
                                
            '''Player card position #3 '''
            #OPENING,RESIZING AND LOADING IMAGE
            #load1 = Image.open(card.card_image)
            load1 = Image.open('Card-Back-01.png')
            load1 = load1.resize((width,height), Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load1)

            #DISPLAYING AND PLACING IMAGE ON SCREEN
            img1 = Label(window,image=render)
            img1.image=render
            img1.place(x=dxpos,y=dypos)
            dxpos+=width+30
        i+=1      

#to enable and disable buttons

def disable(x):
    x.config(state=DISABLED)
def enable(x):
    x.config(state=NORMAL)   

def all_children (window) :
    _list = window.winfo_children()

    for item in _list :
        if item.winfo_children() :
            _list.extend(item.winfo_children())

    return _list  

def clearFrame():
    widget_list = all_children(window)
    print('Widget Lsit:',len(widget_list))
        
    for item in widget_list:
        xp=item.winfo_rootx()
        yp=item.winfo_rooty()
               
        if(xp<900 and yp>=100  ):    
            item.destroy()
        if(xp==58 and yp==51  ):    #it will destroy dealer hit label 
            item.destroy()
   
          
#BUTTON FUNCTIONS
def newGameButton(bt):
    global window
    global pCard,dCard,pxpos,pypos,dxpos,dypos
    global hitButton,standButton
    global new_game_message
    global chipsInput,chipsButton,chipsLabel
    disable(standButton)
    disable(hitButton)
        
  
    if(bt=='new'):
        if(pCard>0):
            clearFrame()
            dCard=pCard=0
            dxpos=50
            dypos=110
            pxpos=50
            pypos=410
            
        instructions.destroy()
        new_game_message.destroy()
        dealerWinsLabel.destroy()
        dealerBustLabel.destroy()
        playerWinsLabel.destroy()
        playerBustLabel.destroy()
        playerChipsLabel.destroy()
        playerChipsTotalLabel.destroy()
        disable(dealButton)
        PlaySound("79616__tymaue__card-shuffle-2.wav", SND_FILENAME)
    
        
        
        #CHIPS LABEL    
        chipsLabel = Label(window, text="Chips:",bg="dark green", fg='white',font='Times 20')
        chipsLabel.place(x=640,y=500)
        
        #INPUT FIELD FOR CHIPS
        chipsInput = Entry(window, width=5,text=chipData, borderwidth=5, bg="lightgray")
        chipsInput.place(x=717,y=505)
                
        #CHIPS SUBMIT BUTTON
        chipsButton = Button(window,text="Submit Chips",command=submitChips,fg="white", bg="dark orange",borderwidth=5,font='Times 11')
        chipsButton.place(x=770, y=505)
            
        chipsInput.delete(0,END)
        
        #PLAYER LABEL
        playerLabel = Label(window, text= "PLAYER:", font=20,borderwidth=5,relief="groove")
        playerLabel.place(x=50,y=350)
  
    
    global deck
    deck = Deck()
    
    deck.shuffle()
                  
    global player_hand
    player_hand = Hand()

    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

                    
    global dealer_hand                
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    

    #Set up the player's chips
    player_chips =Chips() #Default value of 100
              
    #Prompt the player for their bet
    take_bet_question()
    

def submitChips():
    
    global playing,chipsInput,chipsButton,chipsLabel,chipsQuestion
    global bet_chips
    enable(standButton)
    enable(hitButton)
    #Set up the player's chips
    player_chips =Chips() #Default value of 100
    player_chips= take_bet(player_chips) 
    chipsQuestion.destroy()
    
    if(player_chips.bet<=0):
        messagebox.showerror("Error", "Chips are more than you have or Invalid!\nPlease Enter Valid Bet (Max 100)")
        chipsInput.destroy()
        chipsButton.destroy()
        chipsLabel.destroy()
        newGameButton('new')
    else:
        bet_chips=player_chips

        chipsInput.destroy()
        chipsButton.destroy()
        chipsLabel.destroy()

        #Show cards(but keep one dealer card hidden)
        show_some(player_hand,dealer_hand) #SHOW THE DEALER'S HAND AND PLAYER'S HAND
            
        #Remove chips question from screen
        chipsQuestion.destroy()
                
        #Paste rest of code here and see if we can simulate the rest of the gam eon the GUI
        hit_or_stand(deck,player_hand)  #Ask Player if they'd like to Hit or Stand

    
    
#HAD TO RE-DEFINE THESE AGAIN HERE FOR DESTROY FUNCTION ON NEW GAME
player_chips =Chips()        
playerChipsTotal = player_chips.total


#global usernameData
usernameData = StringVar()

#USERNAME LABEL
usernameLabel = Label(window, text="Username:",bg="dark green",fg='white',font=20)
usernameLabel.place(x=450,y=140)

#USERNAME INPUT
usernameInput = Entry(window,text=usernameData)
usernameInput.place(x=550,y=150)


def submitUsername():
    get_username = usernameData.get()                                                                         
    usernameLabel.destroy()
    usernameInput.destroy()
    usernameButton.destroy()
    return get_username


#USERNAME SUBMIT BUTTON
global usernameButton
usernameButton = Button(window,text="Submit",fg="white", bg="dark orange",borderwidth=5,font='Times 9',command=submitUsername)
usernameButton.place(x=690,y=145)

def take_bet(chips):    
    global bet_chips
    bet_chips=chipData.get()
    chips.bet= bet_chips  #GRAB THE INPUT CHIP VALUE

    if chips.bet.isdigit(): 
        chips.bet = int(chips.bet)
    if chips.bet > chips.total:
        chips.bet=-1
    return chips  
            
            
def hitButtonFunc(bt):
    global bet_chips
    global dhl_flag
    dhl_flag=False
    
    global hitButton,standButton
    result=False
    
    print('Button '+ bt + ' Clicked')
    if(bt=='hit'):
       hand = Hand()
       
       
    player_chips = bet_chips
    
    
    hitLabel.destroy()
    
    if(bt=='hit'):
        hit(deck,player_hand)
        print('Total Card After Dealt in Player HAnd is=',len(player_hand.cards))
        show_another(player_hand)  #PLAYER SELECTS 'HIT', SO AN ADDITIONAL CARD IS SHOWN ON THE SCREEN FOR THE PLAYER'S HAND
          
   
    if player_hand.value > 21:    #21
        player_busts(player_hand,dealer_hand,player_chips)
        result=True
        
      
    if player_hand.value <= 21 :     #21
        while dealer_hand.value < 17:   #17
            print('Dealer get a new Card')
            hit(deck,dealer_hand)
            dshow_another(dealer_hand)   ##this function will print new inserted card
            dealerHitLabel = Label(window, text="Dealer chooses to Hit",font=15,fg='white',bg='dark green')    
            dealerHitLabel.place(x=50,y=20)          
           
            
    # Show all cards
    print('Total Cards In Dealer Hand:=',len(dealer_hand.cards))
    print('Total Cards In Player Hand:=',len(player_hand.cards))
    
    print('Dealer Value:',dealer_hand.value)
    print('Player VAlue:',player_hand.value)
    if(bt=='stand' and result==False):
        # Test different winning scenarios
        if dealer_hand.value > 21:      #21
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand)
        result=True
        
    print('Checking if result is True or Not Final ')
    if (result==True): 
        
        show_all(dealer_hand)
        disable(hitButton)
        disable(standButton)
        #this will show the hidden dealer card first
        image=dealer_hand.cards[0].card_image
        #OPENING,RESIZING AND LOADING IMAGE
        load = Image.open(image)
        load = load.resize((width,height), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)

        #DISPLAYING AND PLACING IMAGE ON SCREEN
        img = Label(window,image=render)
        img.image=render
        img.place(x=50 ,y=110)   
        
        # Inform Player of their chips total
        global playerChipsLabel
        playerChipsTotal = player_chips.total
        playerChipsLabel = Label(window, text="Player's winnings stand at:",font=15,borderwidth=5,relief="groove")
        playerChipsLabel.place(x=650,y=540)
        
        global playerChipsTotalLabel
        playerChipsTotalLabel = Label(window, text=playerChipsTotal,font=15,borderwidth=5,relief="groove")
        playerChipsTotalLabel.place(x=900,y=540)
        
        print("\nPlayer's winnings stand at",player_chips.total)
        
        # Ask to play again
        global new_game_message
        new_game_message = Label(window,text="Click New Game to play again! >>>",font=15,bg='dark green',fg='white')
        new_game_message.place(x=770,y=350)
        enable(dealButton)
    
#BUTTONS USED FOR CONTROLLING THE GAME

dealButton = Button(window, text="NEW GAME", font=7, padx=7,pady=2,fg="white", bg="red", activebackground="yellow", borderwidth=7,command=partial(newGameButton,'new'))
dealButton.place(x=1114,y=360,anchor=W)


hitButton = Button(window, text="  HIT  ",font=7, padx=5,pady=2,fg="white", bg="orange", activebackground="yellow", borderwidth=7, command=partial(hitButtonFunc,'hit'))
hitButton.place(x=1141,y=420,anchor=W)


standButton = Button(window, text="STAND",font=7, padx=0,pady=2,fg="white", bg="gray", activebackground="yellow", borderwidth=7, command=partial(hitButtonFunc,'stand'))
standButton.place(x=1141,y=480,anchor=W)

exitButton = Button(window, text="END GAME",font=7, padx=7,pady=2,fg="white", bg="black", activebackground="yellow", borderwidth=7, command=window.destroy)
exitButton.place(x=1114,y=560,anchor=W)
               
     
def player_busts(player,dealer,chips):
    playerBustLabel = Label(window, text="Player Busts!",font=15,fg='white',bg='dark green')
    playerBustLabel.place(x=150,y=350)
    print("PLAYER BUSTS!")
    chips.total=chips.lose_bet(chips.total,chips.bet)
    PlaySound("124996__phmiller42__aww.wav", SND_FILENAME)
    loss = True
    return loss
    
    
def player_wins(player,dealer,chips):
    playerWinsLabel = Label(window, text="Player Wins!",font=15,fg='white',bg='dark green')
    playerWinsLabel.place(x=150,y=350)
    print("PLAYER WINS!")
    chips.total=chips.win_bet(chips.total,chips.bet)
    PlaySound("209792__alterr__applause-mono-24bit-48khz.wav", SND_FILENAME)
    win = True
    return win
        

def dealer_busts(player,dealer,chips):
    global dealerBustLabel
    dealerBustLabel = Label(window, text="Player Wins! Dealer Busts!",font=15,fg='white',bg='dark green')
    dealerBustLabel.place(x=150,y=50)
    print("PLAYER WINS! DEALER BUSTS!")
    chips.total=chips.win_bet(chips.total,chips.bet)
    PlaySound("209792__alterr__applause-mono-24bit-48khz.wav", SND_FILENAME)
    win = True
    return win
    
    

def dealer_wins(player,dealer,chips):
    global dealerWinsLabel
    dealerWinsLabel = Label(window, text="Dealer Wins!",font=15,fg='white',bg='dark green')
    dealerWinsLabel.place(x=150,y=50)
    print("DEALER WINS!")
    chips.total=chips.lose_bet(chips.total,chips.bet)
    PlaySound("124996__phmiller42__aww.wav", SND_FILENAME)
    loss = True
    return loss
    
  
def push(player,dealer):
    pushLabel = Label(window, text="Dealer and player tie! It's a push. ",font=15,fg='white',bg='dark green')
    pushLabel.place(x=150,y=350)
    print("Dealer and player tie! It's a push. ")
    PlaySound("209792__alterr__applause-mono-24bit-48khz.wav", SND_FILENAME)
     

'''Defining Labels here for acknowledgement at newGameButton function '''

welcomeMessage = Label(window, text="BLACKJACK BUDDY",bg="dark green",fg='white',font='Times 30',borderwidth=10,relief="groove")#What Start Button does
welcomeMessage.place(x=405,y=15)
        
instructions = Label(window, text="Enter Username and Click 'New Game' To Begin!",bg="dark green",fg='white',font=20)
instructions.place(x=400,y=100)

new_game_message = Label(window,text="Click New Game to play again!",font=15)

dealerWinsLabel = Label(window, text="Dealer Wins",font=15)

dealerBustLabel = Label(window, text="Player Wins! Dealer Busts!",font=15)

playerWinsLabel = Label(window, text="Player Wins",font=15)

playerBustLabel = Label(window, text="Player Busts",font=15)

playerChipsLabel = Label(window, text="Player's winnings stand at",font=15)

playerChipsTotalLabel = Label(window, text=playerChipsTotal,font=15)
   

global chipData
chipData = StringVar()

window.mainloop()







