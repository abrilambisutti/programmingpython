
import pygame

import random


pygame.init()


# Pantalla

width, height = 640, 480

screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Snake Game")


# Colores

black = (0, 0, 0)

white = (255, 255, 255)

green = (0, 255, 0)

red = (255, 0, 0)


# Variables del juego

snake_pos = [100, 50]

snake_body = [[100, 50], [90, 50], [80, 50]]

food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]

food_spawn = True


score = 0

username = input("Ingrese su nombre de usuario: ")


# Reloj para controlar juego

clock = pygame.time.Clock()


# Loop principal del juego

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Movimiento de la serpiente
    keys = pygame.key.get_pressed()
    for key in keys:
        if keys[pygame.K_LEFT]:
            snake_pos[0] -= 0.01
        if keys[pygame.K_RIGHT]:
            snake_pos[0] += 0.01
        if keys[pygame.K_UP]:
            snake_pos[1] -= 0.01
        if keys[pygame.K_DOWN]:
            snake_pos[1] += 0.01

    # Asegurarse de que la serpiente no salga de la pantalla
    if snake_pos[0] < 0 or snake_pos[0] > width - 10 or snake_pos[1] < 0 or snake_pos[1] > height - 10:
        pygame.quit()
        quit()

    # Movimiento de la serpiente
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()
    
    if not food_spawn:
        food_pos = [random.randrange(1, (width//10)) * 10, random.randrange(1, (height//10)) * 10]
        food_spawn = True

    # Dibujar elementos en la pantalla
    screen.fill(black)
    for pos in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(screen, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    # Mostrar puntuación y nombre de usuario
    font = pygame.font.Font(None, 36)
    text = font.render("Puntuación: " + str(score), True, white)
    screen.blit(text, (5, 5))
    
    font = pygame.font.Font(None, 24)
    text = font.render("Usuario: " + username, True, white)
    screen.blit(text, (5, 40))
    
    pygame.display.flip()
    
    clock.tick(15)


pygame.quit()

quit()