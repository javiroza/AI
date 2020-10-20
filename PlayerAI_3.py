from random import randint
from BaseAI_3 import BaseAI

class PlayerAI(BaseAI): #It takes the class BaseAI as parent
    def getMove(self, grid):	
        (child,utility) = self.maximize(grid)
        return child

    def maximize(self, grid):
    	"""returns tuple of (grid, utility)"""
    	if self.terminal_test(grid):
    		return (None, self.utility(grid))

    	(maxchild,maxutility) = (None,-1.0) 

    	# here we have to find a way to make a move...
    	for child in self.children(grid):
    		(childprima, utility) = self.minimize(child)
    		if utility > maxutility:
    			(maxchild,maxutility) = (child, utility)

    	return (maxchild,maxutility)

    def minimize(self, grid):
    	"""returns tuple of (grid, utility)"""
    	if self.terminal_test(grid):
    		return (None, self.utility(grid))

    	(minchild,minutility) = (None,1e10) 

    	for child in self.children(grid)
    		(childprima, utility) = self.maximize(child)
    		if utility < minutilty:
    			(minchild,minutility) = (child, utility)

    	return (minchild,minutility)

# the next two methods are defined exclusively for clarity reasons
    def utility(self, grid):
    	"""Returns the tile with the maximum value"""
    	return grid.getMaxTile() 

    def terminal_test(self, grid):
    	"""Returns False if the given grid is a loss and True otherwise"""
    	return not grid.canMove()

    def children(self, grid):
    	"""Returns a list with the children grids of a given grid"""
    	children = []

    	
    	return children



