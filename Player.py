import random
import math

class Player:
	def __init__(self, letter):
		self.letter = letter

	def get_move(self, game):
		pass


class RandomComputerPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_move(self, game):
		square = random.choice(game.available_moves())
		return square

class HumanPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_move(self, game):
		valid = False
		val = None

		while not valid:
			square = input(self.letter + "'s turn: ")

			try:
				val = int(square)
				if val not in game.available_moves():
					raise ValueError
				valid = True
			except ValueError:
				print('Invalid')

		return val

class AIPlayer(Player):
	def __init__(self, letter):
		super().__init__(letter)

	def get_move(self, game):
		if len(game.available_moves()) == 9:
			square = random.choice(game.available_moves())
		else:
			square = self.minimax(game, self.letter)['position']

		return square


	def minimax(self, state, letter):
		max_player = self.letter
		other_player = 'O' if letter == 'X' else 'X'

		if state.current_winner == other_player:
			return {'position': None, 'score': 1 * (state.num_of_empty() + 1) if other_player == max_player else -1 * (
                        state.num_of_empty() + 1)}
		elif not state.empty():
			return {'position': None, 'score': 0}

		if letter == max_player:
			best = {'position': None, 'score': -math.inf}
		else:
			best = {'position': None, 'score': math.inf}

		for possible_move in state.available_moves():
			state.make_move(possible_move, letter)
			sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move made above
			state.board[possible_move] = ' '
			state.current_winner = None
			sim_score['position'] = possible_move  # this represents the move optimal next move


			if letter == max_player:  # X is max player
				if sim_score['score'] > best['score']:
					best = sim_score
			else:
				if sim_score['score'] < best['score']:
					best = sim_score
		return best
