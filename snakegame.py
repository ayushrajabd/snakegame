import pygame
import time
import random

pygame.init()

white=(255,255,255)
yellow=(255,255,102)
black=(0,0,0)
red=(213,50,80)
green=(0,255,0)
blue=(50,153,213)

dis_width=600
dis_height=400

dis=pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption( 'ayush snake game')

clock=pygame.time.Clock()

snake_block=10
snake_speed=15

font_style=pygame.font.SysFont("bahnschrift",25)
score_font=pygame.font.SysFont("comicsansms",35)
def Your_score(score):
    value=score_font.render("Your Score:"+str(score),True,yellow)
    dis.blit(value,[0,0])
    return value.get_height()

def highscore_show(score, y):
    value = score_font.render("Highscore:"+str(score), True, yellow)
    dis.blit(value, (0, y))

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,black,[x[0],x[1],snake_block,snake_block])

def message(msg,color):
    mesg=font_style.render(msg,True,color)
    dis.blit(mesg,[dis_width/6,dis_height/3])

def read_highscore(filename):
    try:
        with open(filename,"r")as f:
            highscore=int(f.read())
    except:
        highscore=0
    return highscore
def write_highscore(filename,highscore):
    try:
        
        with open(filename,"w")as f:
            f.write(str(highscore))
    except:
        print("error while writing to file")
filename="score.sc"

##write_highscore(filename,highscore)
def gameLoop():
    game_over=False
    game_close=False

    x1=dis_width/2
    y1=dis_height/2

    x1_change=0
    y1_change=0

    snake_List=[]
    Length_of_snake=1

    foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
    foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
    print(foodx, foody)
    highscore = read_highscore(filename)

    while not game_over:

        while (game_close and not game_over):
           dis.fill(blue)
           message("YOU LOST! press Q-Quit or C-play again ",red)
           pygame.display.update()

           for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     game_over = True
                 if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        game_over=True

                    if event.key==pygame.K_c:
                        gameLoop()    

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                   x1_change=-snake_block
                   y1_change=0
                elif event.key==pygame.K_RIGHT:
                   x1_change=snake_block
                   y1_change=0
                elif event.key==pygame.K_UP:
                   y1_change=-snake_block
                   x1_change=0
                elif event.key==pygame.K_DOWN:
                   y1_change=snake_block
                   x1_change=0

        if x1>=dis_width or x1<0 or y1>=dis_height or y1<0:
            game_close=True

        x1 +=x1_change
        y1+=y1_change
        dis.fill(blue)
        # print(foodx, foody)
        pygame.draw.rect(dis,green,[int(foodx),int(foody),snake_block,snake_block])
        snake_Head=[]
        snake_Head.append(x1)
        snake_Head.append(y1)
        # print(snake_Head)
        snake_List.append(snake_Head)
        # print(snake_List)
        if len(snake_List)>Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x==snake_Head:
                game_close=True
        our_snake(snake_block,snake_List)  
        yscore = Your_score(Length_of_snake-1)
        highscore_show(highscore, yscore+10)
        pygame.display.update()          
        # print(x1, y1, foodx, foody)
        if x1==foodx and y1==foody:
            foodx=round(random.randrange(0,dis_width-snake_block)/10.0)*10.0
            foody=round(random.randrange(0,dis_height-snake_block)/10.0)*10.0
            Length_of_snake+=1
            if (Length_of_snake-1 > highscore):
                highscore = Length_of_snake - 1
                write_highscore(filename, highscore)
            # print(foodx, foody)

        clock.tick(snake_speed)

      
      

    pygame.quit()
    quit()
gameLoop()
