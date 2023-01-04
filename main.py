
from cairocffi import RadialGradient
import pygame
from constants import *
from math import *

def FieldToScreen(inputCoords):
    return [(-2.89*(float(inputCoords[0])))-(
                8*RADIUS)+310, (-3.5*float(inputCoords[1]))-(2*RADIUS)+300]

def ScreenToField(MousePos):
    return float(-((100*int(MousePos[0]))+(800*RADIUS)-31000)/289), float(-(
        (2*(int(MousePos[1])+(2*RADIUS)-300))/7))

pygame.init()

clock = pygame.time.Clock()

base_font = pygame.font.Font(None, 32)
font = pygame.font.Font('freesansbold.ttf', 20)

text = font.render(outputText, True, green, blue)

textStepsList=[]
textFGCS = font.render('', True, green)
textFGC = font.render(greenOutputText, True, blue, green)

textRect = text.get_rect()
greenTextRect = text.get_rect()
greenS = text.get_rect()

textRect.center = (X-(1.81*NEWX), Y-(.025*NEWY))
greenTextRect.center = (X-(1.81*NEWX), Y-(.025*NEWY)-20)
greenS.center=X,Y


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
coordsText=font.render('Click a point to get position', True, blue, green)
green2OutputText, green3OutputText, green4OutputText, green5OutputText = greenOutputText, greenOutputText, greenOutputText, greenOutputText
points = [False, False, False, False, False]
outputTL = [green5OutputText,green4OutputText,green3OutputText, green2OutputText, greenOutputText]
active=False
yactive = False
while True:

    rBMS = (pygame.mouse.get_pos()[0]+(RADIUS*e)), pygame.mouse.get_pos()[1]+(RADIUS*e)

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

    for coord in coords:
        screenCoord = FieldToScreen(coord)
        pygame.draw.circle(display_surface, green, screenCoord, RADIUS*4, width=2)
        greenS.center=screenCoord[0]+(RADIUS*pi), screenCoord[1]-RADIUS
        coordText = (f'X: {ScreenToField(screenCoord)[0]}'+f' Y: {ScreenToField(screenCoord)[1]}')
        textFGCS = font.render(str(stepList[step-2]), True, blue)
        coordsText = font.render(coordText, True, blue, green)
        print(stepList)
    

    pre_mouse = pygame.mouse.get_pos()

    pygame.draw.rect(display_surface, color, input_rect)
    text_surface = base_font.render(user_text, True, (255, 255, 255))
    display_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    display_surface.blit(text, textRect)

    display_surface.blit(textFGCS, greenS)
    display_surface.blit(coordsText, greenTextRect)

    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()

    clock.tick(60)
    for event in pygame.event.get():
        if active == False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                stepList.append(step)
                coords.append(ScreenToField(pygame.mouse.get_pos()))
                step+=1
                
                
            if event.type == pygame.KEYDOWN:

                if len(coords)>=1:
                    if event.key == pygame.K_DELETE:
                        coordText = "Click a point to get position"
                        textFGCS = font.render('', True, blue)
                        stepList.clear()
                        textStepsList.clear()
                        step=1
                        
                        
                        coords = []
                        coordsText = font.render(coordText, True, blue, green)

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
            print(coords)
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
                    try:
                        if len(inputCoords) == 2 or len(inputCoords) == 3:
                            if inputCoords[1] != '' and inputCoords[1] != '-':
                                yactive = True
                                if len(inputCoords) == 3:
                                    if inputCoords[2] != '' and inputCoords[2] != '-' and float(inputCoords[2]) <= 360 and float(inputCoords[2]) >= -360:
                                        pass
                                ptx, pty = (-2.89*(float(inputCoords[0])))-(
                                    8*RADIUS)+310, (-3.5*float(inputCoords[1]))-(2*RADIUS)+300
                                print('ptx:'+str(ptx)+' pty:'+str(pty))
                        else:
                            yactive=False
                    except:
                        pass

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        pygame.display.update()
