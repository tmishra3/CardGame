# -*- coding: utf-8 -*-
"""
Created by Tanmay Mishra

"""
import random
import sys
from termcolor import colored, cprints

class card: #Card object. Contains a suit, a color and a value.
    
     specialCards = ["J","Q","K"] #Local variable to card that denotes the special kinds of cards representing
#11 to 13.
    
     def __init__(self, color="Red", suit="♦", number=2): #Default values of the card if nothing is inputted.
          self.suit = suit
          self.color = color
          self.number = str((number<2)*"A" or ((number>10)*(self.specialCards[(number>10)*(number<=13)*(number-11)])) or (number>1)*(number<=10)*number)
#The constructor takes in a value of 1 to 13 for the number. The line above turns cards of value 1 to "A" and cards of value 11, 12 or 13 to values 
#represented by the specialCards list. All values are converted to string through casting.

     def printCard(self): #method to print the card value. Notice that it calls retPrint method.
          print(self.retPrint())
         
     def __str__(self): #Overloaded method of passing the output of the card value as a string. It also calls retPrint.
          return (self.retPrint())


     def __repr__(self): #Overloaded method of passing the print representation of a card object. It also calls retPrint.
          return (self.retPrint())


     def retPrint(self): #The main method for returning a string statement that the above 3 functions use. Prints the text in either
#red or black depending on the color of the card.

         if self.color=="Red":
             return (colored(str(self.number) + '' + str(self.suit), 'red', attrs=['bold']))
         else:
             return (str(self.number) + "" + self.suit)
         
     def returnColor(self): #Method to return the current card object's color.        
         return self.color            

     def returnSuit(self): #Method to return the current card object's suit.        
         return self.suit

     def returnNumber(self): #Method to return the current card object's numeric value. As you can see, despite the card object
#operating within the constraints of A,2,3,4,5,6,7,8,9,10,J,K,Q, this method is returning the equivalent numeric value as an int.
         if (self.number=="A"):
             return 1
         elif (self.number=="J"):
             return 11
         elif (self.number=="K"):
             return 13
         elif (self.number=="Q"):
             return 12
         else:         
             return int(self.number)                      


class deck: #The deck class is an object that is comprised of card objects. The cards are stored as a list.

    mySuits = ["♠","♣","♥","♦"] #Local variable for deck class. Any deck object we create will have these in common so it creates
#consistency between the objects themselves.
    myColors = ["Black","Red"] #Local variable for deck class. Same comment as for mySuits.    

    def __init__(self, name = "THIS DECK", FullDeck = True): #Constructor for deck object. As you can see,
#the default name for a deck is "THIS DECK" and the boolean value of FullDeck is set to True. FullDeck tells
#the constructor whether to create a default, full deck of 52 cards. If it's False, it'll create an "empty"
#deck. This is useful if you write main code where you need to draw cards and move them to a new location.
#The location is simply an empty deck into which you put the cards you removed from your full deck (in example).
        self.numCards = 0 #By default, create no cards in the deck.
        self.stack = [] #By default, create no cards in the list.
        self.shuffledDeck = [] #This stores the number of shuffled cards. Will be explained later.
        self.name = name #Stores the name passed by the parameter.

        if (FullDeck==True): #If value of FullDeck is True (which it is by default), we create
#a deck of 52 cards.
            self.numCards = 52
            for y in range(0,4): #For the 4 suits designated by mySuits.
                for x in range(0,13): #For the 13 different cards per suit.
                    self.stack.append(card(self.myColors[(y>1)],self.mySuits[y],x+1)) #If y>1, this means that we're looking
#at index 2,3 of mySuits (the last 2 card shapes). If this is true, y>1 calculates to a boolean value of 1 which when 
#passed into myColors will pick Red as the color for the last 2 cards of mySuit and will pick Black as the color for the first
#2 cards in mySuit. The suit is simply represented by y. The value of the card is x+1 since our index goes from 0 to 12 and we
#want it to go from 1 to 13. We pass these parameters into the card object (which will card the constructor for card as explained
#above in the card class). The card is then "appended" (literally pushed in) to the deck from the right.

    def emptyDeck(self, printOutput = None): #This method will remove all cards in a deck. This is useful if you don't want to
#initialize your deck object as an empty deck but want to empty it later. 

#NOTE: PrintOutput is simply a "devmode" sort of parameter that you'll see in several methods below. Basically, it'll print out
#a statement explaining what it is doing if you pass anything as a parameter in the function. So, for example, if you say
#myDeck.emptyDeck(1), it will actually print that it emptied the deck but myDeck.emptyDeck() will empty the deck but will not
#actually print anything. This is useful when writing the main code and wanting to see what is actually going on but should be
#removed in the final build of the game.

        self.numCards = 0
        self.stack = []
        self.shuffleDeck = []
        if (printOutput!=None):
            print ("***************\nYOUR DECK IS NOW EMPTY\n***************\n")        

    def printDeck(self): #Prints out the list of cards in the deck. Notice that when I say print(self.stack), technically
#i am printing out a list of card objects. Since we created the _repr_ functon in card, we can actually use print because
#print now knows that when it's printing out a list of cards, it has to print out each card individually and knows how to 
#print it due to the _repr_ function which explains to Python how a custom object (in this case card) is being printed out.
        print ("***************\n" + str(self.name) +" HAS THESE CARDS:\n***************\n")
        print (self.stack)
        print("\n")
            

    def shuffleDeck(self, printOutput = None): #With a deck of n cards, this function will shuffle its contents. It works
#by first picking a random index between 0 and (n-1) (so with 52 cards in the deck, a random number between 0 and 51). Once
#a random index has been picked, the card at that location is removed and stored into shuffleDeck. Now, we have 1 less card in
#our deck. The process is repeated with a random number generated between 0 and (n-2) (representing the removal of the first
#randomly picked card. This process repeats until all cards are removed. Then, we assign stack as shuffleDeck.
        
        r = 0
        drawCard = card()
        
        for j in range(0,(self.numCards)):
            r = random.randint(0,(self.numCards)-1-j)
            drawCard = self.stack[r] #Temporary card storing the random card we removed.
            
            self.shuffledDeck.append(drawCard) #Push the random card into shuffleDeck.
            self.stack.remove(drawCard) #Remove the card with value "drawCard" from the stack. Since we have no duplicate cards,
#it's ok to use remove rather than pop.
        
        self.stack = self.shuffledDeck
        self.shuffledDeck = [] #Notice that we then assign shuffleDeck as empty again.
        if (printOutput!=None):
            print ("***************\nYOUR DECK HAS BEEN SHUFFLED.\n***************\n")

    def returnCardN(self, cardNumber): #Returns the card at location cardNumber. However, it DOES NOT delete the card.
        if ((cardNumber>0) and (cardNumber<53)):
            return self.stack[cardNumber-1]
        else:
            print ("***************\nINVALID CARD.\n***************\n")

    def reverseDeck(self, printOutput = None): #Reverses the deck in opposite order.
        self.stack.reverse()
        if (printOutput!=None):
            print("***************\nYOUR DECK HAS BEEN REVERSED.\n***************\n")

    def removeCardN(self,index, printOutput = None): #Removes a card at location index and returns it. Notice that despite me using the term
#index, it represents locations 1 to n not 0 to n-1.
        if ((index-1)>=0) and ((index-1)<=self.numCards): #If number of cards are between 1 and n.
            cardtoRemove = self.stack[index-1] #Set a temporary card equal to card at that location.
            self.stack.remove(cardtoRemove) #Remove the card from stack.
            self.numCards += -1 #Reduce the number of cards by 1.
            if (printOutput!=None):
                print("***************\nREMOVED CARD #" + str(index))
                print(cardtoRemove)
                print("***************\n")
            return cardtoRemove #Return the card object that we removed.
        else:
            print ("***************\nYOUR DECK HAS NO CARDS TO REMOVE.\n***************\n")

    def removeRandCard(self, printOutput = None): #Does the same thing as the above function but for a random index.
        if (self.numCards>=0): #As long as we have more than 0 cards.
            indexofRemove = random.randint(0,(self.numCards)-1) #Store index of location of card to be removed.
            cardtoRemove = self.stack[indexofRemove] #Store card at that index into a temporary card object.
            if (printOutput!=None):
                print("***************\nREMOVED CARD #" + str(indexofRemove+1))
                print(cardtoRemove)
                print("***************\n")
            self.stack.remove(cardtoRemove)
            self.numCards += -1 #Reduce the number of cards by 1.
            return cardtoRemove #Return the card object that we removed.
        else:
            print ("***************\nYOUR DECK HAS NO CARDS TO REMOVE.\n***************\n")           

    def returnNumCards(self, printOutput = None): #Returns the number of cards.
        if (printOutput!=None):
            print ("***************\nYOUR DECK CONTAINS " + str(self.numCards) + " CARDS:\n***************\n")        
        return self.numCards

    def addCard(self,newCard,printOutput=None): #Pushes a card into the deck from the right with value newCard as long
#as we have less than 52 cards (can't add a card into a full deck)
        if (self.numCards<52):
            self.stack.append(newCard)
            self.numCards += 1 #increase number of cards by 1
            if (printOutput!=None):
                print("***************\nADDED CARD TO DECK")
                print(newCard)
                print("***************\n") 
        else:
            print ("***************\nYOUR DECK ALREADY HAS 52 CARDS.\n***************\n")                       

    def resizeRandDeck(self,numberCards): #Resizes a deck of n cards to a deck of numberCards by randomly 
#picking cards to make a new deck. So for example, if you had 52 cards, you can create a deck of 30 by randomly picking
#30 cards to put into a new deck. This method does modify the current deck.
        if ((self.numCards-numberCards)>=0): #Cards to create in resized deck has to be less or equal to number of 
#cards in the original deck.
            print ("***************\nPICKING " + str(numberCards) + " RANDOM CARDS.\n***************\n")            
            for j in range (0,numberCards):
                indexofRemove = random.randint(0,(self.numCards)-1)
                cardtoRemove = self.stack[indexofRemove]
                self.stack.remove(cardtoRemove)
                self.shuffledDeck.append(cardtoRemove)
                self.numCards += -1
            self.stack = self.shuffledDeck
            self.shuffledDeck = []
            self.numCards = numberCards
            print ("***************\nYOUR DECK HAS " + str(self.numCards) + " CARDS NOW.\n***************\n")            
        else:
            print ("***************\nYOUR DECK HAS NO CARDS TO RESIZE.\n***************\n")        

#====================================================
###################MAIN CODE BLOCK###################       

