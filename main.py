from Game import *
from Player import *
from Input import *
from random import randint
from time import sleep

t_input = Input()

games = []

while True:
	t_input.update()

#moves = t_input.getMoves()
#matches = t_input.getGames()

	for g in range(len(matches)):
		p1_white = randint(1, 10)
		p1 = Player(matches[g][0], p1_white % 2)
		p2 = Player(matches[g][1], not (p1_white % 2))

		games.append(Game(p1, p2))

	for m in moves:
		for g in range(len(games)):
			p = games[g].getPlayer(m.getID())
			if p != -1:  # Check if either player is one of the tweeters
				if p.isTurn():
					b = games[g].updateBoard(m.getMove())  # update found game with new move
					if b == "Invalid move":
						t_input.sendMessage(b, p)
					else:
						t_input.sendMessage(b, games[g].getPlayer(1, True), games[g].getPlayer(2, True))
				else:
					t_input.sendMessage(b, p)
				break
			#elif g == len(games) - 1:  # Found no game with this user
				#TODO: Make tweet with "No game started" content. or maybe do nothing
