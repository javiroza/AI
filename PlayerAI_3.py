from random import randint
from BaseAI_3 import BaseAI
import time

class PlayerAI(BaseAI): #It takes the class BaseAI as parent
	def __init__(self):
		self.alpha = -1
		self.beta = 10000

	def getMove(self, grid):	
		""" returns the next move in a number"""
		(move,utility) = self.maximize(grid,None,0,time.perf_counter())
		return move

	def maximize(self, grid, move, counter, ctime):
		"""returns tuple of (grid, utility)"""
		counter += 1
		if self.terminal_test(grid) or counter > 5:
			return (move, self.utility(grid))

		(maxchild,maxutility) = (None,-1.0) 

		grids = self.children(grid)[0::2]
		moves = self.children(grid)[1::2]
		for child_grid in grids:
			if (ctime-time.perf_counter() <= 10):
				child_move = moves[grids.index(child_grid)]
				(childprima, utility) = self.minimize(child_grid,child_move,counter, time.perf_counter())
				if utility > maxutility:
					(maxchild,maxutility) = (child_move, utility)
			else:
				return (move, self.utility(grid))
			if maxutility >= self.beta:
				break
			if maxutility > self.alpha:
				self.alpha = maxutility

		return (maxchild,maxutility)

	def minimize(self, grid, move, counter,ctime):
		"""returns tuple of (grid, utility)"""
		counter += 1
		if self.terminal_test(grid) or counter > 5:
			return (move, self.utility(grid))

		(minchild,minutility) = (None,1e10) 

		grids = self.children(grid)[0::2]
		moves = self.children(grid)[1::2]
		for child_grid in grids:
			if (ctime-time.perf_counter() <= 10):
				child_move = moves[grids.index(child_grid)]
				(childprima, utility) = self.maximize(child_grid,child_move,counter,time.perf_counter())
				if utility < minutility:
					(minchild,minutility) = (child_move, utility)
			else:
				return(move, self.utility(grid))
			if minutility <= self.alpha:
				break
			if minutility > self.beta:
				self.beta = minutility


		return (minchild,minutility)

# the next two methods are defined exclusively for clarity reasons
	def utility(self, grid):
		"""Returns the tile with the maximum value"""
		return grid.getMaxTile() 

	def terminal_test(self, grid):
		"""Returns False if the given grid is a loss and True otherwise"""
		return not grid.canMove()

	def children(self, grid):
		"""Returns a list with the children nodes of a given grid"""
		children = []

		for move in grid.getAvailableMoves():
			gridcopy = grid.clone()
			gridcopy.move(move)
			children.append(gridcopy)
			children.append(move) 

		return children

############ Notes ###############
# Without alpha-beta pruning we can see that it hardly ever gets to do
# a "right" or "left" move, since they are checked last.

# Whith alpha-beta pruning we see many more of the moves mentioned above,
# which means that it can do so within the time limit.


