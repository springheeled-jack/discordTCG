#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Momentum"
COST = 4
RARITY = 'C'
DESC = "Draw two cards. If you played a Node this turn, draw an additional card."
TARGETS = None
TYPE = "PlyInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	ply.drawCard()
	ply.drawCard()
	if ply.playedNode == True:
		ply.drawCard()
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

