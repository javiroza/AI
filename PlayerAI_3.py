from random import randint
from BaseAI_3 import BaseAI
import sys

sys.setrecursionlimit(10**9)

class PlayerAI(BaseAI): #It takes the class BaseAI as parent
    def getMove(self, grid):	
    	""" returns the next move in a number"""
    	(move,utility) = self.maximize(grid,-1.3)
    	return move

    def maximize(self, grid, move):
    	"""returns tuple of (grid, utility)"""
    	if self.terminal_test(grid):
    		return (move, self.utility(grid))

    	(maxchild,maxutility) = (None,-1.0) 

    	grids = self.children(grid)[0::2]
    	moves = self.children(grid)[1::2]
    	for child_grid in grids:
    		child_move = moves[grids.index(child_grid)]
    		(childprima, utility) = self.minimize(child_grid,child_move)
    		if utility > maxutility:
    			(maxchild,maxutility) = (child_move, utility)

    	return (maxchild,maxutility)

    def minimize(self, grid, move):
    	"""returns tuple of (grid, utility)"""
    	if self.terminal_test(grid):
    		return (move, self.utility(grid))

    	(minchild,minutility) = (None,1e10) 

    	grids = self.children(grid)[0::2]
    	moves = self.children(grid)[1::2]
    	for child_grid in grids:
    		child_move = moves[grids.index(child_grid)]
    		(childprima, utility) = self.maximize(child_grid,child_move)
    		if utility < minutilty:
    			(minchild,minutility) = (child_move, utility)

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



