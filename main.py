import pygame
import random

# Připravíme PyGame
pygame.init()
pygame.display.set_caption("  Get fuel")
size = (320, 190)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Připravíme si obrázek
background = (200, 200, 200 )
turtle = pygame.image.load("turtle.png")
turtle = pygame.transform.scale(turtle, (40, 40))
pineapple = pygame.image.load("pineapple.png")
pineapple = pygame.transform.scale(pineapple, (40, 40))
Trava = pygame.image.load("Tráva.png")
Trava = pygame.transform.scale(Trava,(400, 265))
dlaždice = pygame.Surface((40, 40))
dlaždice.set_alpha(0)
dlaždice.fill((255, 255, 255))

# screen.blit(turtle, game_to_screen(zx, zy))
# screen.blit(pineapple, game_to_screen(0, 0))                                                                   

# Připravíme si obrázek

WIDTH = 4
HEIGHT = 4
zx = 2
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
        draw_scene()
        screen.blit(rotated_turtle, (x, y))
        pygame.display.update()
        t = t + clock.tick()
       
    zx = nx
    zy = ny
   

def draw_scene():
  screen.fill(background)
  screen.blit(Trava,(0, 0))
  for x in range(WIDTH):
        for y in range(HEIGHT):                    
           screen.blit(dlaždice,game_to_screen(x, y))          
  screen.blit(pineapple, game_to_screen(pa_x, pa_y))

  font =  pygame.font.Font(None, 42);
  text = font.render(f"Score: {score}", True, (0, 0, 0), (0, 250, 0))
  screen.blit(text, (0, 0))
 
pa_x = 0
pa_y = 0
score = 0

rotated_turtle = pygame.transform.rotate(turtle, 0)
while True:
    # Vykreslíme
    
    draw_scene()    
    screen.blit(rotated_turtle, game_to_screen(zx, zy))
    
    pygame.display.update()

    event = pygame.event.wait()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            rotated_turtle = pygame.transform.rotate(turtle, 180)
            if zx < WIDTH - 1:
                animate(zx + 1, zy)
        elif event.key == pygame.K_UP:
            rotated_turtle = pygame.transform.rotate(turtle, 270)
            if zy > 0:
                animate(zx, zy - 1)
        elif event.key == pygame.K_LEFT:
            rotated_turtle = pygame.transform.rotate(turtle, 0)
            if zx > 0:
                animate(zx - 1, zy)
        elif event.key == pygame.K_DOWN:
            rotated_turtle = pygame.transform.rotate(turtle, 90)
            if zy < HEIGHT - 1:
                animate(zx, zy + 1)

    if (zx, zy) == (pa_x, pa_y):
        pa_x = random.randrange(0, WIDTH)
        pa_y = random.randrange(0, HEIGHT)
        score = score + 1