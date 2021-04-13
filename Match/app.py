import pygame as py
from pygame import display,event, image
import game_config as gc
from animal import Animals
from time import sleep

def find_index(x,y):
    row=y//gc.IMAGE_SIZE
    col=x//gc.IMAGE_SIZE
    index=row*gc.NUM_TILES_SIDE+col
    return index

py.init()
display.set_caption('My Game')
screen= display.set_mode((512,512))
path=r'E:\my python\game\New folder\other_assests\matched.png'
matched=image.load(path)
mm=py.transform.scale(matched,(512,512))


running=True
tiles=[Animals(i)for i in range(0,gc.NUM_TILES_TOTAL)]
current_images=[]

while running:
    current_events=event.get()
    for e in current_events:
        if e.type==py.QUIT:
            running=False
        if e.type==py.KEYDOWN:
            if e.key==py.K_ESCAPE:
                running=False
        if e.type==py.MOUSEBUTTONDOWN:
            mouse_x,mouse_y=py.mouse.get_pos()
            index=find_index(mouse_x,mouse_y)
            #to avoid matched when we click image twice
            if index not in current_images:
                current_images.append(index)
            if len(current_images)>2:
                current_images=current_images[1:]




    screen.fill((255,255,255))
    total_skipped=0
    for _,tile in enumerate(tiles):
        image_i=tile.image if tile.index in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i,(tile.col*gc.IMAGE_SIZE+gc.MARGIN,tile.row*gc.IMAGE_SIZE+gc.MARGIN))
        else:
            total_skipped+=1
    display.flip()
    if len(current_images)==2:
        idx1,idx2=current_images
        if tiles[idx1].name==tiles[idx2].name:
            tiles[idx1].skip=True
            tiles[idx2].skip=True
            sleep(0.5)
            screen.blit(mm,(0,0))

            
            display.flip()
            sleep(0.5)
            current_images=[]
    
    if total_skipped==len(tiles):
        running=False



print("Good Bye!!!")