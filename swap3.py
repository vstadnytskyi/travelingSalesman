import numpy as np
from random import shuffle, randrange, choice
from time import time
from numba import jit
from itertools import permutations

@jit
def algorithm(cities):

	order =  range( cities.shape[0] )
	shuffle(order)
	length = calcLength(cities, order)
	start = time()

	changed = True
	while changed:

		changed = False

		for a in range(cities.shape[0]):

			for b in range(a+1, cities.shape[0] - 1):

				c =  choice( list( range(b+1, cities.shape[0]) ) )

				a, b, c = choice( list( permutations( (a, b, c) ) ) )

				new_order = order[:a] + order[a:b][::-1] + order[b:c][::-1] + order[c:]
				new_length = calcLength(cities, new_order)

				if new_length < length:
					length = new_length
					order = new_order
					changed = True

	return order, length

@jit
def calcLength(cities, path):
	length = 0
	for i in range( len(path) ):
		length += dist( cities[ path[i-1] ], cities[ path[i] ] )

	return length

@jit
def dist(c1, c2):
	return np.hypot(c2[0] - c1[0], c2[1] - c1[1])
