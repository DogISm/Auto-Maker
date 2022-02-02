
from pickle import NEWOBJ_EX, TRUE
from time import sleep
from tkinter import LEFT
from unittest import BaseTestSuite
import pygame
from math import *

def distanceCal(x1,y1,x2,y2):
    distance = [sqrt(((x2-x1)**2)), sqrt(((y2-y1)**2))]
    return distance

pygame.init()

clock = pygame.time.Clock()

blue = (3, 123, 252)
green = (78, 237, 123)
yellow = (247, 190, 32)
outputText = 'Hello World'
greenOutputText = 'Click a point to get position'

base_font = pygame.font.Font(None, 32)
user_text = 'Go To:'
font = pygame.font.Font('freesansbold.ttf', 20)
text = font.render(outputText, True, green, blue)
textFGC3, textFGC4, textFGC5 = font.render(greenOutputText, True, blue, green),font.render(greenOutputText, True, blue, green),font.render(greenOutputText, True, blue, green)
textFGC2 = font.render(greenOutputText, True, blue, green)
textFGC = font.render(greenOutputText, True, blue, green)
textFGCL = [textFGC, textFGC2, textFGC3, textFGC4, textFGC5]
textRect = text.get_rect()
greenTextRect = text.get_rect()
green2TextRect = text.get_rect()
green3TextRect,green4TextRect,green5TextRect = text.get_rect(),text.get_rect(),text.get_rect()
textRectL = [greenTextRect, green2TextRect, green3TextRect,green4TextRect,green5TextRect]

X = 600
Y = 700
NEWX = X/2
NEWY = Y/2
RADIUS = 6.5

textRect.center = (X-(1.81*NEWX), Y-(.025*NEWY))
greenTextRect.center = (X-(1.81*NEWX), Y-(.025*NEWY)-20)
green2TextRect.center = (X-(1.81*NEWX), Y-(.025*NEWY)-40)
green3TextRect.center = (X-(1.81*NEWX), Y-(.025*NEWY)-(20*3))
green4TextRect.center = (X-(1.81*NEWX), Y-(.025*NEWY)-(20*4))
green5TextRect.center = (X-(1.81*NEWX), Y-(.025*NEWY)-(20*5))

input_rect = pygame.Rect(X/2-(X-(1.81*NEWX)), Y-(20*11.3), 200, 32)
color_active = pygame.Color('lightskyblue3')

color_passive = pygame.Color('chartreuse4')
color = color_passive

active = False

display_surface = pygame.display.set_mode((X, Y))

pygame.display.set_caption('RR Auto Maker')

image = pygame.image.load(r'C:\Users\maudi\Downloads\Dashboard.png')

pre_mouse = 0
pty, ptx = 0, 0
circlept = 0
toggle = False
betterMouseCoords = [0, 0]
betterMouseCoords2 = [0, 0]
betterMouseCoords3 = [0, 0]
betterMouseCoords4 = [0, 0]
betterMouseCoords5 = [0, 0]
coords = [betterMouseCoords, betterMouseCoords2, betterMouseCoords3, betterMouseCoords4, betterMouseCoords5]
point5, point4, point3, point2, point = False, False, False, False, False
active=False
yactive = False
while True:
    rBMS = (pygame.mouse.get_pos()[0]+(RADIUS*25)), pygame.mouse.get_pos()[1]+(RADIUS*25)

    display_surface.fill('#212020')
    pygame.draw.circle(display_surface, blue,
                       pygame.mouse.get_pos(), RADIUS*4, width=2)
    headingLine = pygame.draw.line(
        display_surface, blue, pygame.mouse.get_pos(), rBMS, width=4)
    headingLine
    # print(rBMS[1])
    display_surface.blit(image, (0, 0))
    circlept

    mousex, mousey = -((100*pygame.mouse.get_pos()[1])+(800*RADIUS)-31000)/289, -(
        (2*(pygame.mouse.get_pos()[0]+(2*RADIUS)-300))/7)
    outputText = 'X: '+str(mousex)+' Y: '+str(mousey)
    text = font.render(outputText, True, green, blue)
    if yactive:
        yellowCircle = pygame.draw.circle(display_surface, yellow, [
            pty, ptx], RADIUS*4, width=2)

    pre_mouse = pygame.mouse.get_pos()
    if point5:
        circlept5 = pygame.draw.circle(
            display_surface, green, betterMouseCoords5, RADIUS*4, width=2)
    if point4:
        circlept4 = pygame.draw.circle(
            display_surface, green, betterMouseCoords4, RADIUS*4, width=2)
    if point3:
        circlept3 = pygame.draw.circle(
            display_surface, green, betterMouseCoords3, RADIUS*4, width=2)
    if point2:
        circlept2 = pygame.draw.circle(
            display_surface, green, betterMouseCoords2, RADIUS*4, width=2)
    if point:
        circlept = pygame.draw.circle(
            display_surface, green, betterMouseCoords, RADIUS*4, width=2)
    pygame.draw.rect(display_surface, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    display_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    display_surface.blit(text, textRect)

    display_surface.blit(textFGC, greenTextRect)
    display_surface.blit(textFGC2, green2TextRect)
    display_surface.blit(textFGC3, green3TextRect)
    display_surface.blit(textFGC4, green4TextRect)
    display_surface.blit(textFGC5, green5TextRect)

    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()

    clock.tick(60)
    for event in pygame.event.get():
        if active == False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_5:
                    point5 = True
                    betterMouseCoords5 = list(pygame.mouse.get_pos())
                    green5OutputText = 'X: '+str(-((100*betterMouseCoords5[1])+(
                        800*RADIUS)-31000)/289)+' Y: '+str(-((2*(betterMouseCoords5[0]+(2*RADIUS)-300))/7))
                    textFGC5 = font.render(green5OutputText, True, blue, green)
                if event.key == pygame.K_4:
                    point4 = True
                    betterMouseCoords4 = list(pygame.mouse.get_pos())
                    green4OutputText = 'X: '+str(-((100*betterMouseCoords4[1])+(
                        800*RADIUS)-31000)/289)+' Y: '+str(-((2*(betterMouseCoords4[0]+(2*RADIUS)-300))/7))
                    textFGC4 = font.render(green4OutputText, True, blue, green)
                if event.key == pygame.K_3:
                    point3 = True
                    betterMouseCoords3 = list(pygame.mouse.get_pos())
                    green3OutputText = 'X: '+str(-((100*betterMouseCoords3[1])+(
                        800*RADIUS)-31000)/289)+' Y: '+str(-((2*(betterMouseCoords3[0]+(2*RADIUS)-300))/7))
                    textFGC3 = font.render(green3OutputText, True, blue, green)
                if event.key == pygame.K_2:
                    point2 = True
                    betterMouseCoords2 = list(pygame.mouse.get_pos())
                    green2OutputText = 'X: '+str(-((100*betterMouseCoords2[1])+(
                        800*RADIUS)-31000)/289)+' Y: '+str(-((2*(betterMouseCoords2[0]+(2*RADIUS)-300))/7))
                    textFGC2 = font.render(green2OutputText, True, blue, green)
                if event.key == pygame.K_1:
                    point = True
                    betterMouseCoords = list(pygame.mouse.get_pos())
                    greenOutputText = 'X: '+str(-((100*betterMouseCoords[1])+(
                        800*RADIUS)-31000)/289)+' Y: '+str(-((2*(betterMouseCoords[0]+(2*RADIUS)-300))/7))
                    textFGC = font.render(greenOutputText, True, blue, green)
                coords = [betterMouseCoords,betterMouseCoords2,betterMouseCoords3,betterMouseCoords5]
                if point or point2 or point3 or point4 or point5:
                    if event.key == pygame.K_DELETE:
                        print(distanceCal(pygame.mouse.get_pos()[1],pygame.mouse.get_pos()[0],betterMouseCoords2[1],betterMouseCoords2[0]))
                        green5OutputText,green4OutputText,green3OutputText, green2OutputText, greenOutputText = 'Click a point to get position', 'Click a point to get position', 'Click a point to get position', 'Click a point to get position', 'Click a point to get position'
                        # greenOTL = greenOutputText,green2OutputText,green3OutputText, green4OutputText, green5OutputText
                        # greenOTL = list(greenOTL)
                        # for i in range(len(textFGCL)):
                        #     textFGCL[i] = font.render(greenOTL[i], True, blue, green)
             
                        textFGC = font.render(greenOutputText, True, blue, green)
                        textFGC2 = font.render(green2OutputText, True, blue, green)
                        textFGC3 = font.render(green3OutputText, True, blue, green)
                        textFGC4 = font.render(green4OutputText, True, blue, green)
                        textFGC5 = font.render(green5OutputText, True, blue, green)

                        point5, point4, point3, point2, point = False, False, False, False, False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(display_surface, color, input_rect)
  
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        display_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            pass
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
            pass
        if event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
            pass
        if active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
                    inputCoords = user_text[6:].split(',')
                    print(inputCoords)
                    if len(inputCoords) == 2 or len(inputCoords) == 3:
                        yactive = True
                        if inputCoords[1] != '' and inputCoords[1] != '-':
                            if len(inputCoords) == 3:
                                if inputCoords[2] != '' and inputCoords[2] != '-' and float(inputCoords[2]) <= 360 and float(inputCoords[2]) >= -360:
                                    pass
                            ptx, pty = (-2.89*(float(inputCoords[0])))-(
                                8*RADIUS)+310, (-3.5*float(inputCoords[1]))-(2*RADIUS)+300
                            print('ptx:'+str(ptx)+' pty:'+str(pty))
                    else:
                        yactive=False

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
