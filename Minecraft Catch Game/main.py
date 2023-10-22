import pgzrun
import time
WIDTH = 800
HEIGHT = 600

start_time = time.time()
current_time = 0
print(start_time)


def draw():
    screen.blit("bg1", (0,0))
    screen.draw.text(f"{int(current_time)}", (10, 10))


def update():
    global current_time
    current_time = time.time() - start_time


pgzrun.go()