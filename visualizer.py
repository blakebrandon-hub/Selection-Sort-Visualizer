import pygame
import random
import time


class Visualizer:	
	def __init__(self):
		pygame.init()
		pygame.display.set_caption('Selection Sort Visualizer - (r) to randomize (s) to sort')

		try:
			pygame_icon = pygame.image.load('algo.png')
			pygame.display.set_icon(pygame_icon)
		except pygame.error as e:
			print(f"Icon load failed: {e}")

		pygame.font.init()
		self.surface = pygame.display.set_mode((994, 450))
		self.clock = pygame.time.Clock()
		self.col_heights = []
		self.col_spacing = []
		self.range = 83

		self.colors = {
			'BLACK': (0, 0, 0),
			'WHITE': (255, 255, 255),
			'RED': (255, 0, 0),
			'GREEN': (0, 255, 0)
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
		for _ in range(self.range):
			heights = random.randrange(50, 400)
			self.col_heights.append(heights)

	def randomize(self):
		self.col_heights = []
		self.surface.fill(self.colors['BLACK'])

		for _ in range(self.range):
			heights = random.randrange(50, 400)
			self.col_heights.append(heights)

		self.surface.fill(self.colors['BLACK'])
		for i in range(self.range):		
			pygame.draw.rect(self.surface, self.colors['WHITE'], pygame.Rect(self.col_spacing[i], self.col_heights[i], 10, 450))
		
		pygame.display.update()

	def selection_sort(self):
		# LEFT TO RIGHT, finding the SMALLEST and placing it at position i
		for i in range(self.range):
			min_idx = i
			for j in range(i + 1, self.range):
				if self.col_heights[j] > self.col_heights[min_idx]:
					min_idx = j

			# Swap smallest found into current index i
			self.col_heights[i], self.col_heights[min_idx] = self.col_heights[min_idx], self.col_heights[i]

			# Visual update
			self.surface.fill(self.colors['BLACK'])
			for k in range(self.range):
				if k == i:
					color = self.colors['RED']      # current index
				elif k == min_idx:
					color = self.colors['GREEN']    # current min found
				else:
					color = self.colors['WHITE']
				pygame.draw.rect(self.surface, color, pygame.Rect(self.col_spacing[k], self.col_heights[k], 10, 450))

			pygame.display.update()
			time.sleep(0.05)

	def main(self): 
		self.surface.fill(self.colors['BLACK'])
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
