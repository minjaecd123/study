import pygame as p

p.init()
w =(255,255,255)
size = (800,400)
sc = p.display.set_mode(size)
p.display.set_caption("게임판")
playing = True

while playing:
    
    for event in p.event.get():
        if event.type == p.QUIT:
            playing = False
            p.quit()
            quit()

    sc.fill(w)
    p.display.flip()
