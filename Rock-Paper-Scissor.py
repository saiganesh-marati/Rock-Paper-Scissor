#!/usr/bin/env python
# coding: utf-8

# In[132]:


from random import randint
i=0
ps=0
cs=0

print("---------WELCOME TO ROCK PAPER SCISSOR GAME---------")
while(True):
    choice=['rock','paper','scissor']
    player=input((f"choose from {choice}")).lower()
    comp=choice[randint(0,2)]
    print("computer chooses:",comp)
    if player==comp:
        print("DRAW MATCH")
    elif player =="paper" and comp=="rock":
        print("player 1 wins")
        ps+=1
    elif player =="rock" and comp=="scissor":
        print("player 1 wins") 
        ps+=1
    elif player =="scissor" and comp=="paper":
        print("player 1 wins")
        ps+=1
    else:
        print("Computer Wins")
        cs+=1
    if(cs==5 or ps==5):
        break
    
    
if(ps>cs):
    print("Player 1 wins Whole Game with score:",ps)
else:
    print("Computer Wins the Whole Game with score",cs)


# In[ ]:




