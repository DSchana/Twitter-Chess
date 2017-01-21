#
# Shahir Chowdhury
# 2017-01-21
# This program manages a twitter bot to handle the twitter side of TwitterChess
#
# TO DO:
#	Methods:	update - Get new tweets and store in moves or games
#				getMoves - return moves if not empty else false (move must 4 to 5 characters long)
#				getGames - return games if not empty else false
#				sendMessage - Sends a message (takes in a string s)
#
#	Features: 	Ignore irrelavant tweets referencing realtwitChess
#				Calling self starts an AI game
#				Timestamping games to know latest board between two people
#
# 	Bonus:		Error messages for invalid actions
#				Game Displaying
#				Refresh Option

import tweepy

#Authorizing information to control account
consumer_key = "kdf50lNpawRUFy7K7NqEptWd2"
consumer_secret = "qOlsMFW5PdyP26ut6U9segE7ikWp0oifE36l8fvQKg713xBMGb"

access_token = "822095735411896325-dyVt5FAJ9PZ8lhTMZhuibO2YVpDKyHg"
access_token_secret = "5dvBevNb1MxpJw52dpgkfeto4cVqa48ihKv7UnJeoEe9j"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True #Stay safe and secure
api = tweepy.API(auth) #authorize the tweepy API
thisBot = api.get_user(screen_name = "@CurryKing622")

#
# Objective: Creates an object that manages input and output from twitter
# Input: A list to store moves in active games and a list to store games preparing to be made
# Output: Can post statuses or supply other objects with the games and moves list it stores
#
class Input:
	def __init__ (self,moves,games):
		self.moves = moves
		self.games = games

	#
	# Objective: Scans twitter feeds for mentions of the twitterchess bot and records relevant actions
	# Input: None
	# Output: Stores new games and planned moves 
	#
	def update(self):
		for tweet in tweepy.Cursor(api.search, q = '@realtwitchess ',count = 100,lang = ' ').items():
			try:
				text = str(tweet.text)
				textparts = str.split(text) #convert tweet into string array to disect

				for x, string in enumerate(textparts): 
					if (x < len(textparts)-1): #prevents error that arises with an incomplete call of the twitter bot to start a game
						if string == "gamestart" and textparts[x+1][:1] == "@": #find games
							otheruser = api.get_user(screen_name = textparts[2][1:]) #drop the @ sign (although it might not matter)
							print otheruser.id
							self.games.append((tweet.user.id,otheruser.id))
					elif (len(textparts[x]) == 4): #find moves
						newMove = Move(tweet.user.id,string)
						print newMove.getMove()
						self.moves.append(newMove)
				if tweet.user.id == thisBot.id: #ignore self tweets
					continue

			except tweepy.TweepError as e: 
				print(e.reason)
				sleep(10)
				continue
			except StopIteration: #stop iteration when last tweet is reached
				break

	def getMoves(self): #returns the list of moves in active games
		if not self.moves:
			return false
		return self.moves

	def getGames(self): #returns the list of games waiting to be made
		if not self.games:
			return false
		return self.games

	#
	# Objective: Scans twitter feeds for mentions of the twitterchess bot and records relevant actions
	# Input: None
	# Output: Stores new games and planned moves 
	#
	def sendMessage(self,s,ID1 = None, ID2 = None): #writes a status, mentioning 1, 2 or no other users
		if not ID1 and not ID2: #No person to be mentioned
			api.update_status(s)

		elif ID1 and not ID2: #Only one person is mentioned
			user = api.get_user(ID1)   
			try:
				api.update_status("@" + user.screen_name + " " + s)
			except tweepy.TweepError as e:
				pass

		elif ID1 and ID2: #Two people are mentioned
			user = api.get_user(ID1)  
			user2 = api.get_user(ID2)
			print user2.screen_name
			try:
				api.update_status("@" + user.screen_name + " @" + user2.screen_name + " " + s)
			except tweepy.TweepError as e:
				pass

class Move: #object contains the ID of the player and the move they are to make
	def __init__ (self,playerID,move):
		self.playerID = playerID
		self.move = move

	def getID(self):
		return self.playerID

	def getMove(self):
		return self.move

moveslist = []
gameslist = []
test = Input(moveslist, gameslist)
test.update()