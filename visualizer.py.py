import pygame
import random
import time


class Visualizer:	
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Selection Sort Visualizer - (r) to randomize (s) to sort')
		pygame_icon = pygame.image.load('algo.png')
		pygame.display.set_icon(pygame_icon)
		pygame.font.init()
		self.surface = pygame.display.set_mode((994,450))
		self.clock = pygame.time.Clock()
		self.col_heights = []
		self.col_spacing = []
		self.range = 83

		self.colors = {
			'BLACK': (0,0,0),
			'WHITE': (255,255,255),
			'RED': (255,0,0),
			'GREEN': (0,255,0)			
			}

		self.create_spacing()
		self.create_heights()
		self.main()

	def create_spacing(self):
		count = 0

		for i in range(self.range):
			if i == 0:
				self.col_spacing.append(i)
			else:
				count += 12
				self.col_spacing.append(count)

	def create_heights(self):

		for i in range(self.range):
			heights = random.randrange(50, 400)
			self.col_heights.append(heights)

	def randomize(self):
		self.col_heights = []
		self.surface.fill((0,0,0))

		for i in range(self.range):
			heights = random.randrange(50, 400)
			self.col_heights.append(heights)

		for i in range(self.range):		
			pygame.draw.rect(self.surface, self.colors['WHITE'], pygame.Rect(self.col_spacing[i], self.col_heights[i], 10, 450))
		
		pygame.display.update()

	def selection_sort(self):
		

		for i in range(self.range):
			#self.surface.fill(self.colors['BLACK'])
			pygame.display.update()
			mid_ = i

			for j in range(i+1, len(self.col_heights)):

				if self.col_heights[mid_] < self.col_heights[j]:
					mid_ = j

				self.col_heights[i], self.col_heights[mid_] = self.col_heights[mid_], self.col_heights[i]


				#self.surface.fill(self.colors['BLACK'])
				for k in range(self.range):

					pygame.draw.rect(self.surface, self.colors['WHITE'], pygame.Rect(self.col_spacing[k], self.col_heights[k], 10, 450))
					pygame.display.update()

	def main(self): 

		for i in range(self.range):
			pygame.draw.rect(self.surface, self.colors['WHITE'], pygame.Rect(self.col_spacing[i], self.col_heights[i], 10, 450))
			pygame.display.update()

		run = True

		while run:

			for event in pygame.event.get():

				if event.type == pygame.QUIT:
					run = False

				if event.type == pygame.KEYDOWN:

					if event.key == pygame.K_r:
						self.randomize()

					if event.key == pygame.K_s:
						self.selection_sort()

			self.clock.tick(30)
			
			pygame.display.update()

		pygame.quit()


if __name__ == '__main__':
	v = Visualizer()