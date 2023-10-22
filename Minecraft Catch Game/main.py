import pgzrun

WIDTH = 1000
HEIGHT = 755

time = 100


def draw():
    screen.blit("bg3", (0, 0))
    # screen.fill("skyblue")
    screen.blit("grass1000", (0, 700))
    # screen.blit("01ground", (0, 0))
    # screen.blit("03distant_trees", (0, 0))
    # screen.blit("02trees", (0, 0))

    screen.draw.text(f"{int(time)}", (10, 10), fontsize=45)


def update():
    global time
    time -= 1 / 60


pgzrun.go()