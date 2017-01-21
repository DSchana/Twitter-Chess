# Title:	 game.py
# Author:     	 Dilpreet S. Chana
# Description: 	 A clean chess wrapper for Python-Chess
# Last Modified: 21 Jan, 2017

import chess
import datetime
import random
import string

from Player import *

class Game:
	def __init__(self, p1, p2):
		self.board = chess.Board()
		self.p1 = p1
		self.p2 = p2
		self.key = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(4)) + str(datetime.datetime.now().time().hour) + str(datetime.datetime.now().time().minute)

	def updateBoard(self, m):
		if not self.isValidMove(m):
			return "Invalid move";

		self.board.push(chess.Move.from_uci(m))
		self.p1.toggleTurn()
		self.p2.toggleTurn()

		return self.getBoard()

	def isValidMove(self, m):
		try:
			return chess.Move.from_uci(m) in self.board.legal_moves
		except:
			return False

	def getPlayer(self, p_id, num = False):
		if num:
			if p_id == 1:
				return self.p1
			elif p_id == 2:
				return self.p2
			else:
				return -1

		if self.p1.getName() == p_id:
			return self.p1
		elif self.p2.getName() == p_id:
			return self.p2
		else:
			return -1

	def getBoard(self):
		out = str(self.board)

		chess_replace = {u'P':u'♙',
				 u'R':u'♖',
                                 u'N':u'♘',
                                 u'B':u'♗',
                                 u'Q':u'♕',
                                 u'K':u'♔',
                                 u'p':u'♟',
                                 u'r':u'♜',
                                 u'n':u'♞',
                                 u'b':u'♝',
                                 u'q':u'♝',
                                 u'k':u'♝',
				 u'.':u'…' }

		for key, value in chess_replace.iteritems():
			out = out.replace(key, value)

		return out

	def getKey(self):
		return self.key
