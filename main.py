import pgzrun

WIDTH = 800
HEIGHT = 500
speed = 1

alien = Actor("alien.png")

def draw():
  screen.fill("red")
  alien.draw()
  if alien.y < 0:
    print("game over")

def update():
  alien.x = alien.x + speed 

def on_mouse_down(pos):
  if alien.collidepoint(pos):
    set_alien_hurt()

def set_alien_normal():
  alien.image = "alien"

def set_alien_hurt():
  alien.image = "alien_hurt"

pgzrun.go()