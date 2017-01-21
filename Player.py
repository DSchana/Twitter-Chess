# Title:         Player.py
# Author:        Dilpreet S. Chana
# Description:   A class represemting a twitter chess player
# Last Modified: 21 Jan, 2017

class Player:
	def __init__(self, t_name, is_white):
		self.t_name = t_name
		self.is_white = is_white
		self.is_turn = is_white

	def toggleTurn(self):
		is_turn = !is_turn

	def getName(self):
		return self.t_name

	def getWhite(self):
		return self.is_white

	def getTurn(self):
		return self.is_turn
