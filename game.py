# Title:	 game.py
# Author:     	 Dilpreet S. Chana
# Description: 	 A clean chess wrapper for Python-Chess
# Last Modified: 21 Jan, 2017

import chess
from Player import *

class Game:
	def __init__(self, p1, p2):
		self.board = chess.Board()
		self.p1 = p1
		self.p2 = p2

	def updateBoard(self, m):
		if not self.isValidMove(m):
			return "Invalid move";

		self.board.push(chess.Move.from_uci(m))
		self.p1.toggleTurn()
		self.p2.toggleTurn()

		return self.board

	def isValidMove(self, m):
		try:
			return chess.Move.from_uci(m) in self.board.legal_moves
		except:
			return False

	def getPlayer(self, p_id):
		if self.p1.getName() == p_id:
			return self.p1
		elif self.p2.getName() == p_id:
			return self.p2
		else:
			return -1

	def getBoard(self):
		return self.board
