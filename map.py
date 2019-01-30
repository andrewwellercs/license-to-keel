import pygame
import random

class Map:
	def __init__(self, sizeIn, blocksIn):
		self.size = sizeIn
		
		self.textures=[]
		#texutres[0] is sand
		self.textures.append(pygame.image.load('textures/grass.png'))
		#textures[1] is grass
		self.textures.append(pygame.image.load('textures/sand.png'))

		self.blocks = blocksIn

	def draw(self, screen, pos):
		for r in range(0, self.size):
			for c in range(0,self.size):
				loc = (pos[0] + (25*c), pos[1] + (25*r))
				
				if self.blocks[r][c] != 0:
					screen.blit(self.textures[self.blocks[r][c]-1], loc)

def generate_map(size):
	# blocks = []
	# for i in range(0, size):
	# 	blocks.append([])
	# 	for j in range(0, size):
	# 		r = random.randint(0,2)
	# 		blocks[i].append(r)
	blocks = generate_blocks(size)
	m = Map(size, blocks)

	return m

def generate_blocks(size):
	blocks = []
	for i in range(0, size):
		blocks.append([])
		for j in range(0,size):
			blocks[i].append(-1)
	print(blocks[size-1][size-1])
	# #creating waters
	# for i in range(0,1):
	# 	randx = random.randint(0,size-1)
	# 	randy = random.randint(0,size-1)
	# 	blocks[randx][randy] = 0
	# #creating lands
	# for i in range(0,1):
	# 	randx = random.randint(0,size-1)
	# 	randy = random.randint(0,size-1)
	# 	blocks[randx][randy] = 1
	blocks[0][0] = 0
	blocks[0][size-1] = 0
	blocks[size-1][0] = 0
	blocks[size-1][size-1] = 0
	blocks[size/2][size/2] = 1

	print("1")

	done = False
	while not done:
		done = True
		for x in range(0, size):
			for y in range(0,size):
				if blocks[x][y] == -1:
					done = False
				elif blocks[x][y] == 0:
					rand = random.randint(0,4)
					try:
						if rand == 0:
							if blocks[x+1][y] == -1:
								blocks[x+1][y] = 0
						elif rand == 1:
							if blocks[x-1][y] == -1:
								blocks[x-1][y] = 0
						elif rand == 2:
							if blocks[x][y+1] == -1:
								blocks[x][y+1] = 0
						elif rand == 3:
							if blocks[x][y-1] == -1:
								blocks[x][y-1] = 0
					except:
						pass
				elif blocks[x][y] == 1:
					rand = random.randint(0,4)
					try:
						if rand == 0:
							if blocks[x+1][y] == -1:
								blocks[x+1][y] = 1
						elif rand == 1:
							if blocks[x-1][y] == -1:
								blocks[x-1][y] = 1
						elif rand == 2:
							if blocks[x][y+1] == -1:
								blocks[x][y+1] = 1
						elif rand == 3:
							if blocks[x][y-1] == -1:
								blocks[x][y-1] = 1
					except:
						pass

		tol = 2
		#these loops make the lands that are within 'tol' blocks
		#	of water turn to sand. kinda like minecraft
		ran = range(-1*tol,tol)
		#Looping over each element of blocks
		for x in range(0, size):
			for y in range(0,size):
				#if the blocks is land
				if blocks[x][y] == 1:
					#compare the blocks around it in the range ran
					for dx in ran:
						for dy in ran:
							#try to check a block, but it might be out of index...
							try:
								if blocks[x+dx][y+dy] == 0:
									blocks[x][y] = 2
							except:
								pass

	return blocks



def load_map(filename):
	file = open(filename)
	for line in file:
		print(line)