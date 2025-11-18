import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img, True, False)
    koukaton_img = pg.image.load("fig/3.png")
    koukaton_img = pg.transform.flip(koukaton_img, True, False)
    kk_rct = koukaton_img.get_rect()
    kk_rct.center = 300, 200
    screen.blit(koukaton_img, kk_rct)
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr % 3200
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2, [-x + 1600, 0])
        screen.blit(bg_img, [-x + 3200, 0])
        kk_rct.move_ip(-1, 0)

        dx, dy = 0, 0

        key_list = pg.key.get_pressed()
        if key_list[pg.K_UP]:
            dy -= 1
        if key_list[pg.K_DOWN]:
            dy += 1
        if key_list[pg.K_RIGHT]:
            dx += 2
        if key_list[pg.K_LEFT]:
            dx -= 1

        kk_rct.move_ip(dx, dy)
        # if dx == 2:
        #     dx -= 2
        # if dx == -1:
        #     dx += 1
        # if dy == 1:
        #     dy -= 1
        # if dy == -1:
        #     dy += 1

        screen.blit(koukaton_img, kk_rct)
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()