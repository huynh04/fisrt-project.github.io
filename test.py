from numpy import random as rd
class Games:
    def __init__(self,player,):
        self.p=player
        
    def player(x):
        x=x.p
        a=rd.choice(['keo','bua','bao'])
        if x=='keo':
            if a=="keo":
                print("Hoa")
            if a=="bua":
                print("bot won")
            if a=="bao":
                print("player won")
        if x=='bua':
            if a=="keo":
                print("player won")
            if a=="bua":
                print("Hoa")
            if a=="bao":
                print("bot won")
        if x=='bao':
            if a=="keo":
                print("bot won")
            if a=="bua":
                print("player won")
            if a=="bao":
                print("Hoa")

p1=Games(str(input()))
p1.player()
        

            

