import pygame

black = (0, 0, 0)
white = (255, 255, 255)
white2 = (255, 255, 255)
bGround = (20, 80, 240)
choose = (220, 200, 0)
dimensions = (800, 800)
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


def drawBoard(screen, dimension, initBoard, sizeFont, font, selection):
	'''
	# Funcion que dibuja el tablero
	screen: 		referencia del lienzo donde dibujar
	dimension: 		tamanio de los rectangulos
	p_inicio: 		coordenadas del punto de inicio del tablero
	tamanio_fuente: tamanio de fuente segun el tablero
	fuente: 		Objeto fuente 
	seleccion: 		rectangulo seleccionado 
	'''
	color = 0
	for i in range(8):
		for j in range(8):
			x = i * dimension + initBoard[0]
			y = j * dimension + initBoard[1]
			if color % 2 == 0:
				pygame.draw.rect(screen, black, [x, y, dimension, dimension], 0)
			else:
				pygame.draw.rect(screen, white, [x, y, dimension, dimension], 0)
			if selection[0] == letters[i] and j == selection[1] - 1:
				pygame.draw.rect(screen, choose, [x, y, dimension, dimension], 0)
			color += 1
		color += 1
		drawText(screen, letters[i], [i * dimension + initBoard[0], initBoard[1] - sizeFont], font)
		drawText(screen, str(i + 1), [initBoard[0] - sizeFont, i * dimension + initBoard[1]], font)


def drawText(screen, text, position, font):
    Text = font.render(text, 1, white2)
    screen.blit(Text, position)


def ajustarMedidas(tamanio_fuente):
    if dimensions[1] < dimensions[0]:
        ancho = int((dimensions[1] - (tamanio_fuente * 2)) / 8)
        inicio = ((dimensions[0] - dimensions[1]) / 2) + tamanio_fuente, tamanio_fuente
    else:
        ancho = int((dimensions[0] - (tamanio_fuente * 2)) / 8)
        inicio = tamanio_fuente, ((dimensions[1] - dimensions[0]) / 2) + tamanio_fuente
    return [inicio, ancho]


def obtenerPosicion(mouse, dimension, p_inicio, actual):
    xr, yr = mouse[0], mouse[1]
    for i in range(8):
        for j in range(8):
            x = i * dimension + p_inicio[0]
            y = j * dimension + p_inicio[1]
            if (xr >= x) and (xr <= x + dimension) and (yr >= y) and (yr <= y + dimension):
                actual = [letters[i], j + 1]
    return actual


def main():
    pygame.init()
    screen = pygame.display.set_mode(dimensions)
    pygame.display.set_caption("__Tablero__")
    game_over = False
    clock = pygame.time.Clock()
    tamanio_fuente = 30
    seleccion = ['Z', -1]
    fuente = pygame.font.Font(None, tamanio_fuente)
    puntoInicio, dimension = ajustarMedidas(tamanio_fuente)
    while game_over is False:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
        botones = pygame.mouse.get_pressed()
        if botones[0]:
            pos = pygame.mouse.get_pos()
            seleccion = obtenerPosicion(pos, dimension, puntoInicio, seleccion)
        screen.fill(bGround)
        drawBoard(screen, dimension, puntoInicio, tamanio_fuente, fuente, seleccion)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()