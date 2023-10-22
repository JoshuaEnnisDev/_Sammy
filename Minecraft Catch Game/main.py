import pgzrun
import time
WIDTH = 1000
HEIGHT = 800

start_time = time.time()
current_time = 0
print(start_time)


def draw():
    screen.blit("bg1", (0, 0))
    screen.blit("grass1000", (0, 750))
    screen.draw.text(f"{int(current_time)}", (10, 10))


def update():
    global current_time
    current_time = time.time() - start_time


pgzrun.go()