import random

suits = ('Diamonds','Clubs','Hearts','Spades')
varis = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
			'Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6, 'Seven':7, 'Eight':8,
			'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':1}
game_on = True

class CardClass():
	def __init__(self, suit, vari):
		self.suit = suit
		self.vari = vari
		self.value = values[vari]
	def __str__(self):
		return f"{self.vari} of {self.suit}"

class DeckClass():
	def __init__(self):
		self.all_cards = []
		for suit in suits:
			for variety in varis:
				new_card = CardClass(suit,variety)
				self.all_cards.append(new_card)

	def shuffle(self):
		random.shuffle(self.all_cards)

	def deal_one(self):
		try:
			return self.all_cards.pop()
		except IndexError:
			self.reset_deck()
			return 	self.all_cards.pop()

	def reset_deck(self):
		self.all_cards = []
		for suit in suits:
			for variety in varis:
				new_card = CardClass(suit,variety)
				self.all_cards.append(new_card)	
		self.shuffle()

new_deck = DeckClass()
new_deck.shuffle()

class PlayerClass():
	def __init__(self, money):
		self.money = money
		self.hand = []

	def __str__(self):
		return f"Player {self.name} has {self.money} dollars."

	def draw_card(self):
		self.hand.append(new_deck.deal_one())

main_player = PlayerClass(500)
dealer = PlayerClass(500)

def play_game():

	print(f"\nYou currently have {main_player.money} dollars.")

	while True:
		try:
			bet_value = int(input("\nEnter the money you are willing to bet:"))
		except:
			print("\nI didnt get that, please enter a digit.")
			continue
		else:
			if bet_value > main_player.money:
				print("\nYou don't have enough money.")
				continue
			elif bet_value > dealer.money:
				print(f"\nThe dealer only has {dealer.money} dollars left.")
				continue
			else:
				main_player.money -= bet_value
				break

	main_player.draw_card()
	main_player.draw_card()
	main_player_value = main_player.hand[0].value + main_player.hand[1].value
	print(f"\nYour cards are {main_player.hand[0]} and {main_player.hand[-1]}.")

	print(f"\nThe total value of these cards are {main_player_value}")
	blackjack = False
	dealer_blackjack = False
	if main_player.hand[0].vari=='Ace':
		if main_player.hand[1].value==10:
			print('\nBlackjack!')
			blackjack = True
	if main_player.hand[1].vari=='Ace':
		if main_player.hand[0]==10:
			print('\nBlackjack!')
			blackjack = True

	for card in main_player.hand:
		if card.vari =='Ace' and not blackjack:
			userin = input("You drew an ace. Would you like to make its value 11 instead of 1? \nType enter for yes, or type anything else for no. ")
			if userin == "":
				main_player_value += 10
				print(f"\nYour new total value is {main_player.value}")

	dealer.draw_card()
	dealer.draw_card()

	if dealer.hand[0].vari=='Ace':
		if dealer.hand[1].value==10:
			dealer_blackjack = True
	if dealer.hand[1].vari=='Ace':
		if dealer.hand[0]==10:
			dealer_blackjack = True

	print(f"\nThe dealer has drawn a {dealer.hand[-1]} and another card, face down.")
	
	while not blackjack:
		move = input(f"\nPress enter to hit, or type a key to stand: ")
		
		if move == '':
			main_player.draw_card()
			main_player_value += main_player.hand[-1].value
			print(f"\nYou drew a {main_player.hand[-1]}.")
			print(f"Your total value is {main_player_value}.")
			if main_player_value > 21:
				print("\nBusted")
				break
			elif main_player_value == 21:
				break
		else:
			break
	dealer_value = dealer.hand[0].value + dealer.hand[1].value
	
	while dealer_value < 17:
		dealer.draw_card()
		dealer_value += dealer.hand[-1].value

	if dealer_blackjack and blackjack:
		print("\nDouble blackjack. This round is a draw.")
		main_player.money += bet_value
		return

	if main_player_value > 21 and dealer_value < 21:
		print("\nThe dealer wins this round.")
		dealer.money += bet_value

	if main_player_value < 21 and dealer_value > 21:
		print("\nYou win this round.")
		dealer.money -= bet_value
		main_player.money += bet_value*2

	if main_player_value == 21 and dealer_value != 21:
		print("\nYou win this round.")
		dealer.money -= bet_value
		main_player.money += bet_value*2

	if dealer_value == 21 and main_player_value != 21:
		print("\nThe dealer wins this round.")
		dealer.money += bet_value	

	if main_player_value < 21 and dealer_value < 21:
		if main_player_value > dealer_value:
			print("\nYou win this round.")
			dealer.money -= bet_value
			main_player.money += bet_value*2
		if dealer_value > main_player_value:
			print("\nThe dealer wins this round.")
			dealer.money += bet_value

	new_deck = DeckClass()
	new_deck.shuffle
	main_player.hand = []
	dealer.hand = []
	dealer_blackjack = False
	blackjack = False

print('\n\nWelcome to Blackjack.')

while True:
	if main_player.money==0 or dealer.money==0:
		if main_player.money > dealer.money:
			print("\nGame over. You win.")
		else:
			print("\nGame over, you lose.")
		userin2 = input("\nPress enter to play again, type anything else to quit: ")
		if userin2 == "":
			main_player.money = 500
			dealer.money = 500
			play_game()
		else:
			break
	play_game()
