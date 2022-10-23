import sys
import pygame
import numpy
import json
import random

import button

with open('shape.json') as f:
    shape = json.load(f)

pygame.init()

backgroud_color = (0, 0, 0)
CellColor = (252, 201, 185)
CellSize = [10, 10]
CellNum = [80, 80]
Cell = numpy.zeros(CellNum)
play = False
frame=False

scale = 0
rotate = 0
last_xy=[-1,-1]
pre = []
dir = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
alive = []
status = 'add'
status_list = ['add', 'remove', 'glider', 'gun','generate', 'clean']


def add(xy):
    for i in xy:
        x, y = i[0], i[1]
        if Cell[x, y] == 0:
            alive.append([x, y])
            Cell[x, y] = 1


def remove(xy):
    for i in xy:
        x, y = i[0], i[1]
        if Cell[x, y]:
            alive.remove([x, y])
            Cell[x, y] = 0


def check():
    for x in range(CellNum[0]):
        for y in range(CellNum[1]):
            if [x, y] in alive:
                Cell[x, y] = 1
            else:
                Cell[x, y] = 0


def update():
    for x in range(CellNum[0]):
        for y in range(CellNum[1]):
            if [x, y] in pre:
                pygame.draw.rect(screen_image, (160, 160, 160), [x*10, y*10, 10, 10], 5)
            elif Cell[x, y]:
                pygame.draw.rect(screen_image, (255, 255, 255), [x*10, y*10, 10, 10], 5)
            else:
                pygame.draw.rect(screen_image, (0, 0, 0),[x*10, y*10, 10, 10], 5)
                pygame.draw.rect(screen_image, (100, 100, 100), [x*10, y*10, 10, 10], 1)
    alive_image = pygame.font.Font("font/msjh.ttc", 24).render("███████████████████", True, (0, 0, 0), (0, 0, 0))
    screen_image.blit(alive_image, (820, 50))
    alive_image = pygame.font.Font("font/msjh.ttc", 24).render(f'存活數量:{len(alive)}', True, (200, 200, 200), (0, 0, 0))
    screen_image.blit(alive_image, (820, 50))


screen_image = pygame.display.set_mode((1000, 800))
screen_rect = screen_image.get_rect()
pygame.display.set_caption('Conway\'s Game of Life')
screen_image.fill(backgroud_color)

play_img = pygame.image.load('images/play.png')
play_button = button.Button(945, 740, play_img, 55, screen_image)
frame_img = pygame.image.load('images/frame.png')
frame_button = button.Button(855, 740, frame_img, 55, screen_image)

def button_reset():
    for i in range(len(status_list)):
        globals()[status_list[i] +'_img'] = pygame.image.load('images/'+status_list[i]+'.png')
        globals()[status_list[i]+'_button'] = button.Button(900, 150 + i*100, globals()[status_list[i]+'_img'], 160, screen_image)


button_reset()
add_img = pygame.image.load('images/add_down.png')
button.Button(900, 150, add_img, 160, screen_image)

for x in range(CellNum[0]):
    for y in range(CellNum[1]):
        pygame.draw.rect(screen_image, (100, 100, 100),
                         [x*10, y*10, 10, 10], 1)


alive_image = pygame.font.Font("font/msjh.ttc", 24).render("存活數量:0", True, (200, 200, 200), (0, 0, 0))
screen_image.blit(alive_image, (820, 50))
pygame.display.flip()



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    MousePos = pygame.mouse.get_pos()
    Cell_x = MousePos[0]//10
    Cell_y = MousePos[1]//10
    if MousePos[0] >= 0 and MousePos[0] <= 800:
        if status in ['add', 'remove']:
            if last_xy!=[Cell_x,Cell_y]:
                pre.clear()
                for x in range(Cell_x-scale, Cell_x+scale+1):
                    for y in range(Cell_y-scale, Cell_y+scale+1):
                        pre.append([x % 80, y % 80])
            last_xy=[Cell_x,Cell_y]
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    if scale < 399:
                        scale += 1
                elif event.y == -1:
                    if scale > -1:
                        scale -= 1
                event.y = 0
                pre.clear()
                for x in range(Cell_x-scale, Cell_x+scale+1):
                    for y in range(Cell_y-scale, Cell_y+scale+1):
                        pre.append([x % 80, y % 80])
            if pygame.mouse.get_pressed()[1]:
                scale = -1
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:
                    if status == 'add':
                        status = 'remove'
                        button_reset()
                        remove_img = pygame.image.load('images/remove_down.png')
                        button.Button(900, 250, remove_img, 160, screen_image)
                    else:
                        status = 'add'
                        button_reset()
                        add_img = pygame.image.load('images/add_down.png')
                        button.Button(900, 150, add_img, 160, screen_image)
                event.button = 0
        else:
            scale = 0
            pre.clear()
            if status == "glider":
                for i in shape['glider']:
                    if rotate == 0:
                        x, y = Cell_x+i[0], Cell_y+i[1]
                    elif rotate == 1:
                        x, y = Cell_x+i[1], Cell_y-i[0]
                    elif rotate == 2:
                        x, y = Cell_x-i[0], Cell_y-i[1]
                    elif rotate == 3:
                        x, y = Cell_x-i[1], Cell_y+i[0]
                    pre.append([x % 80, y % 80])

            if status == "gun":
                for i in shape['gun']:
                    if rotate == 0:
                        x, y = Cell_x+i[0], Cell_y+i[1]
                    elif rotate == 1:
                        x, y = Cell_x+i[1], Cell_y-i[0]
                    elif rotate == 2:
                        x, y = Cell_x-i[0], Cell_y-i[1]
                    elif rotate == 3:
                        x, y = Cell_x-i[1], Cell_y+i[0]
                    pre.append([x % 80, y % 80])

            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    rotate += 1
                elif event.y == -1:
                    rotate -= 1
                event.y = 0
                rotate %= 4

    if pygame.mouse.get_pressed()[0]:
        if MousePos[0] >= 0 and MousePos[0] <= 800:
            if status == 'remove':
                remove(pre)
            elif status == 'add' or (not play):
                add(pre)

    if play:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if MousePos[0] >= 0 and MousePos[0] <= 800:
                if event.button == 1:
                    if status in ['glider', 'gun']:
                        add(pre)
                event.button = 0

    if play_button.down(screen_image):
        if play:
            play = False
            play_img = pygame.image.load('images/play.png')
        else:
            play = True
            play_img = pygame.image.load('images/stop.png')
        button.Button(945, 740, play_img, 55, screen_image)

    if frame_button.down(screen_image):
        frame=True
        if play:
            play_img = pygame.image.load('images/play.png')
        else:
            play = True
        button.Button(945, 740, play_img, 55, screen_image)

    if add_button.down(screen_image):
        status = 'add'
        button_reset()
        add_img = pygame.image.load('images/add_down.png')
        button.Button(900, 150, add_img, 160, screen_image)

    if remove_button.down(screen_image):
        status = 'remove'
        button_reset()
        remove_img = pygame.image.load('images/remove_down.png')
        button.Button(900, 250, remove_img, 160, screen_image)

    if glider_button.down(screen_image):
        status = 'glider'
        button_reset()
        glider_img = pygame.image.load('images/glider_down.png')
        button.Button(900, 350, glider_img, 160, screen_image)

    if gun_button.down(screen_image):
        status = 'gun'
        button_reset()
        gun_img = pygame.image.load('images/gun_down.png')
        button.Button(900, 450, gun_img, 160, screen_image)

    if generate_button.down(screen_image):
        for i in alive:
            Cell[i[0],i[1]]=0
        alive.clear()
        for x in range(CellNum[0]):
            a = [i for i in range(CellNum[0])]
            b = random.sample(a, random.randint(10, 30))
            for y in b:
                alive.append([x, y])
                Cell[x,y]=1

    if clean_button.down(screen_image):
        for i in alive:
            Cell[i[0],i[1]]=0
        alive.clear()
        play=False
        play_img = pygame.image.load('images/play.png')
        button.Button(945, 740, play_img, 55, screen_image)


    if play:
        for i in range(CellNum[0]):
            for j in range(CellNum[1]):
                neighbor = 0
                for d in dir:
                    if Cell[(i+d[0]) % 80, (j+d[1]) % 80]:
                        neighbor += 1
                if Cell[i, j]:
                    if neighbor < 2 or neighbor > 3:
                        alive.remove([i, j])
                else:
                    if neighbor == 3:
                        alive.append([i, j])
        check()
    update()

    if frame:
        play=False
        frame=False

    pygame.display.flip()
