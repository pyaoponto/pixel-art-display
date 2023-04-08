import sys
import pygame
import click


@click.command()
@click.option("--fullscreen", is_flag=True, help="Pixel art will be fullscreen")
@click.argument("files", nargs=-1)
def main(fullscreen, files):
	run(files, fullscreen)


def listen():
	""" quit the window when user presses the red x button of the window """
	return [pygame.quit() for event in pygame.event.get() if event.type == pygame.QUIT]


def run(files, fullscreen):
	pygame.init()
	width, height = 650, 750
	window = pygame.display.set_mode((width, height))

	image_tv = pygame.image.load("tv.png")
	image_tv = pygame.transform.scale(image_tv, (width, height))
	image_sprite = []

	for file in files:
		image = pygame.image.load(file)
		if fullscreen:
			image = pygame.transform.scale(image, (560, 560))
		else:
			image = pygame.transform.scale(image, (350, 350))
		image_sprite.append(image)

	clock = pygame.time.Clock()
	value = 0

	while True:
		clock.tick(4)
		listen()
		if value >= len(image_sprite):
			value = 0

		image = image_sprite[value]
		x = 120
		y = 120
		if fullscreen:
			x = 50
			y = 50
		window.blit(image, (x, y))
		window.blit(image_tv, (0, 0))
		pygame.display.update()

		# Filling the window with black color
		window.fill((0, 0, 0))
		value += 1

if __name__ == "__main__":
	main()
