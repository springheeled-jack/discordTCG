#!/user/bin/env python

from cardList import addCard
import tcgpowers, mechanics

#Simple variables
NAME = "Snipe"
COST = 5
RARITY = 'C'
DESC = "Destroys an enemy Node (they still gain life)."
TARGETS = "ENEMY_NODE"
TYPE = "NodeInteraction"

#What happens when you play it
def playFunc(ply, enemy, target):
	mechanics.sacNode(enemy,ply,target)
	
addCard( NAME, COST, RARITY, DESC, TARGETS, TYPE, playFunc )

