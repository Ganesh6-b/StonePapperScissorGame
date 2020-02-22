# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 16:30:10 2019

@author: Ganesh
"""
name1 = str(input("Enter player 1 name :"))
name2 = str(input("Enter player 2 name :"))
Player1 = str(input("Play %s" %name1))
Player2 = str(input("Play %s" %name2))
if Player1==Player2:
    print("Play Again")
elif Player1=="stone" and Player2=="scissor" or Player1=="paper" and Player2=="stone" or Player1=="scissor" and Player2 == "paper" :
    print("Player1 win")
elif Player2=="stone" and Player1=="scissor" or Player2=="paper" and Player1=="stone" or Player2=="scissor" and Player1 == "paper" :
    print("Player2 win")
else:
    print("unknown command")

    