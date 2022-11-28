import pygame

# Připravíme PyGame
pygame.init()
pygame.display.set_caption(".....")
size = (1920, 720)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Připravíme si obrázek
background = (69, 255, 69)
auto = pygame.image.load("brr2.png")
auto = pygame.transform.scale(auto, (40, 40))

WIDTH = 17
HEIGHT = 14

zx = 1
zy = 1


def game_to_screen(x, y):
    return (x * 45, y * 45)


def animate(nx, ny):
    global zx, zy

    duration = 2000
    t = 0
    # Obrazovkove souradnice
    sx, sy = game_to_screen(zx, zy)
    ex, ey = game_to_screen(nx, ny)
    while t < duration:
        new = t / duration  # 0...1
        old = 1 - new
        x = old * sx + new * ex
        y = old * sy + new * ey
        screen.fill(background)
        draw_grid()
        screen.blit(rotated_turtle, (x, y))
        pygame.display.update()
        t = t + clock.tick()

    zx = nx
    zy = ny

def draw_grid():
    for x in range(WIDTH):
        for y in range(HEIGHT):                    
            color = (255, 255, 255)
            rect = (game_to_screen(x, y), (40, 40))
            pygame.draw.rect(screen, color, rect)

rotated_auto = pygame.transform.rotate(auto, 0)
while True:
    # Vykreslíme
    screen.fill(background)
    draw_grid()
    screen.blit(rotated_auto, game_to_screen(zx, zy))
    pygame.display.update()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            rotated_turtle = pygame.transform.rotate(auto, 270)
            if zx < WIDTH - 1:
                animate(zx + 1, zy)
        elif event.key == pygame.K_UP:
            rotated_turtle = pygame.transform.rotate(auto, 0)
            if zy > 0:
                animate(zx, zy - 1)
        elif event.key == pygame.K_LEFT:
            rotated_turtle = pygame.transform.rotate(auto, 90)
            if zx > 0:
                animate(zx - 1, zy)
        elif event.key == pygame.K_DOWN:
            rotated_turtle = pygame.transform.rotate(auto, 180)
            if zy < HEIGHT - 1:
                animate(zx, zy + 1)
