import numpy as np

def Deck():
    deck=[0]
    for i in range(1,13):
        for j in range(i):
            deck.append(i)
    actions=["Freeze","Flip Three","Second Chance"]
    deck+=actions*3 # append 3 of each special action
    modifiers=["x2", "+2", "+4", "+6", "+8", "+10"]
    deck+=modifiers # Unique Modifiers for game
    return np.array(deck)


def Draw(deck):
    """
    Function to draw without replacements from deck.
    Returns new deck and value drawn
    """
    drawn=np.random.choice(len(deck))
    val=deck[drawn]
    deck=np.delete(deck,drawn)
    return deck,val


class Player:
    def __init__(self,name):
        self.name=name
        self.cards=[]
        self.score=0
        self.bused=False
    def __deal__(self,dealt_card):
        if dealt_card in self.cards:
            self.busted=True
        else:
            self.cards.append(dealt_card)
        if len(self.cards)==7:
            self.score+=sum(self.cards)+15


def NumericDeck(d,mods=False):
    numericdata=np.vectorize(lambda x: x.isnumeric())
    df=np.unique_counts(np.int_(d[numericdata(d)]))
    if mods is True:
        df[1][[2,4,6,8,10]]+=1
    return df