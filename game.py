# Title:	 game.py
# Author:     	 Dilpreet S. Chana
# Description: 	 A clean chess wrapper for Python-Chess
# Last Modified: 20 Jan, 2017

import chess
from Plyaer import *

class Game:
	def __init__(self, p1, p2):
		self.board = chess.Board()
		self.p1 = p1
		self.p2 = p2

	def updateBoard(self)

	def isValidMove(self, m):
		return chess.Move.from_uci(m) in self.board.legal_moves

	def getBoard(self):
		return self.board
