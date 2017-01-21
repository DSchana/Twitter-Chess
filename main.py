from Game import *
from Player import *
from Input import *
from random import randint

t_input = Input()

games = []

while True:
	moves = t_input.getMoves()
	matches = t_input.getGames()

	for g in matches:
		p1_white = randint(1, 10)
		p1 = Player(g[0], p1_white % 2)
		p2 = Player(g[1], not (p1_white % 2))

		games.append(Game(p1, p2))

	for m in moves:
		for g in range(len(games)):
			p = games[g].getPlayer(m[0])
			if (p != -1):  # Check if either player is one of the tweeters
				if p.isTurn():
					b = games[g].updateBoard(m[1])  # update found game with new move
					#TODO: Make tweet with new board
				else:
					#TODO: Make tweet with "Wait you're turn" content
				break
			elif g == len(games) - 1:  # Found no game with this user
				#TODO: Make tweet with "No game started" content
