import pgzrun
WIDTH = 800
HEIGHT = 600
TITLE = "Shootcarft"

gun = Actor("raygun")
player = Actor("alien")


def draw():
    gun.draw()
    alien.draw()


def update():
    gun.left = player.right - 20
    gun.y = player.y

pgzrun.go()